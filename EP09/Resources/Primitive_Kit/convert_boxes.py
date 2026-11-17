# SPDX-License-Identifier: GPL-3.0-or-later
"""Convert this lesson's explicit Y-up box list. All source is provided with the kit."""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from pathlib import Path
import struct
import sys
sys.dont_write_bytecode=True
from miliastra_core.export.builder import build_gia

def fields(data):
    result=[];p=0
    def varint():
        nonlocal p
        value=shift=0
        while p<len(data):
            v=data[p];p+=1;value|=(v&127)<<shift
            if v<128:return value
            shift+=7
            if shift>70:raise ValueError('Invalid varint')
        raise ValueError('Truncated varint')
    while p<len(data):
        tag=varint();number,wire=tag>>3,tag&7
        if wire==0:value=varint()
        elif wire==2:n=varint();value=data[p:p+n];p+=n
        elif wire in {1,5}:n=8 if wire==1 else 4;value=data[p:p+n];p+=n
        else:raise ValueError('Unsupported wire type')
        if not number or p>len(data):raise ValueError('Invalid field')
        result.append((number,value))
    return result
def one(data,n,default=None):
    values=[v for k,v in fields(data) if k==n]
    if len(values)>1:raise ValueError('Duplicate singular field')
    if not values:
        if default is None:raise ValueError('Missing field '+str(n))
        return default
    return values[0]
def vec(data):return [struct.unpack('<f',one(data,n,b'\0'*4))[0] for n in [1,2,3]]
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('input',type=Path);parser.add_argument('output',type=Path);args=parser.parse_args()
    if args.output.suffix.lower()!='.gia':raise ValueError('Output must end in .gia')
    outputs=[args.output,args.output.with_suffix('.readback.json')]
    if any(p.exists() for p in outputs):raise FileExistsError('Choose fresh output names; existing resources are preserved')
    data=json.loads(args.input.read_text(encoding='utf-8'));objects=data['objects']
    if not 1<=len(objects)<=32:raise ValueError('Expected1..32 explicit boxes')
    normal=[]
    for i,source in enumerate(objects):
        x=dict(source)
        if x['template_id']!=10009001:raise ValueError('Only tagged native boxes are supported in this lesson')
        for name in ['position','rotation','scale']:
            if len(x[name])!=3 or not all(math.isfinite(float(v)) for v in x[name]):raise ValueError('Invalid transform')
        if min(x['scale'])<=0 or any(abs(v)>1e-6 for v in x['rotation']):raise ValueError('Positive scales and zero rotations required')
        if len(x['color'])!=4 or x['color'][3]!=100 or any(int(v)!=v or not 0<=v<=255 for v in x['color'][:3]):raise ValueError('Opaque byte RGB required')
        x.update(entity_id=1078609000+i,collision=False,climb=False,enable_collision=False,enable_climb=False,enable_out_of_range_run=False,out_of_range_display_mode=0)
        normal.append(x)
    template=Path(__file__).resolve().parent/'Template/box_template.gia'
    args.output.parent.mkdir(parents=True,exist_ok=True)
    # The writer receives a fresh temporary placement list, retained for reproducibility.
    normal_path=args.output.with_suffix('.objects.json')
    if normal_path.exists():raise FileExistsError(normal_path)
    normal_path.write_text(json.dumps(normal,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    build_gia(template_path=template,objects_path=normal_path,output_path=args.output,summary_path=None,entity_id_start=1078609000,decoration_packaging=False,no_transparency_export=True)
    raw=args.output.read_bytes();size=int.from_bytes(raw[16:20],'big')
    if len(raw)!=24+size or int.from_bytes(raw[:4],'big')!=len(raw)-4:raise ValueError('Container size mismatch')
    assets=[v for n,v in fields(raw[20:20+size]) if n==1]
    if len(assets)!=len(normal):raise ValueError('Object count mismatch')
    checks=[]
    for asset,x in zip(assets,normal):
        entity=one(asset,12);core=one(entity,1);components={one(v,1):v for n,v in fields(core) if n==6};transform=one(components[1],11)
        actual=[vec(one(transform,n,b'')) for n in [1,2,3]]
        expected=[x['position'],x['rotation'],x['scale']]
        if not all(math.isclose(a,z,rel_tol=2e-6,abs_tol=2e-6) for av,zv in zip(actual,expected) for a,z in zip(av,zv)):raise ValueError('Transform readback mismatch')
        if one(entity,4)!=10009001 or one(core,1)!=x['entity_id']:raise ValueError('Identity mismatch')
        if one(asset,3).decode('utf-8')!=x['name']:raise ValueError('Object name mismatch')
        display=one(components[22],32);rgb=(x['color'][0]<<16)|(x['color'][1]<<8)|x['color'][2]
        if one(display,3,0)!=(0xff000000|rgb) or one(display,5,0)!=rgb or struct.unpack('<f',one(display,4,b'\0'*4))[0]!=100:raise ValueError('Opaque colour readback mismatch')
        if one(display,6,0)!=6700:raise ValueError('Expected native display-mode field6700; this is not a Blender material/shader import')
        collider=one(components[5],15)
        if one(collider,1,0)!=0 or one(collider,2,0)!=0:raise ValueError('Decoration-only collider mismatch')
        checks.append({'name':x['name'],'position':actual[0],'scale':actual[2],'template_id':10009001,'collision':False})
    report={'status':'PASS_STATIC_GIA_READBACK_ONLY','input':args.input.name,'output':args.output.name,'sha256':digest(args.output),'primitive_count':len(normal),'records':checks,
        'native_imported':False,'arbitrary_mesh_import':False,'note':'Native appearance, axis, scale and gameplay checks are separate from this structural conversion.'}
    outputs[1].write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:report[k] for k in ['status','output','sha256','primitive_count']}))
if __name__=='__main__':main()
