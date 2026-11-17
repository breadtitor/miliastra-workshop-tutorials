# SPDX-License-Identifier: GPL-3.0-or-later
"""Session-local Blender 4.2 export menu for this lesson's explicit, axis-aligned boxes.

Run this text once in Blender, then File > Export > Miliastra Boxes (.json).
No preference installation, network access, arbitrary-mesh conversion or game scripting.
"""
import bpy
import json
import math
from pathlib import Path
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, FloatProperty

class EXPORT_SCENE_OT_miliastra_boxes(bpy.types.Operator, ExportHelper):
    bl_idname='export_scene.miliastra_boxes'
    bl_label='Export Miliastra Boxes'
    bl_options={'PRESET'}
    filename_ext='.json'
    filter_glob:StringProperty(default='*.json',options={'HIDDEN'})
    origin_x:FloatProperty(name='Game origin X',default=8.0)
    origin_y:FloatProperty(name='Game origin Y (up)',default=0.0)
    origin_z:FloatProperty(name='Game origin Z',default=16.0)
    def execute(self,context):
        collection=bpy.data.collections.get('Miliastra Boxes')
        if collection is None:self.report({'ERROR'},'Missing Miliastra Boxes collection');return {'CANCELLED'}
        objects=[]
        for obj in sorted(collection.objects,key=lambda x:x.name):
            if obj.type!='MESH' or int(obj.get('ugc_native_box',0))!=10009001:
                self.report({'ERROR'},'Each lesson object must be an explicitly tagged native box');return {'CANCELLED'}
            if obj.parent or obj.modifiers or len(obj.data.vertices)!=8 or len(obj.data.polygons)!=6:
                self.report({'ERROR'},'Only eight-corner boxes, no parent or modifiers, are supported');return {'CANCELLED'}
            loc,rot,scale=obj.matrix_world.decompose()
            if abs(rot.angle)>1e-5 or min(scale)<=0:
                self.report({'ERROR'},'Use zero object rotation and positive scales');return {'CANCELLED'}
            corners={tuple(round(float(v),5) for v in vertex.co) for vertex in obj.data.vertices}
            axes=[sorted({x[i] for x in corners}) for i in range(3)]
            if any(len(x)!=2 for x in axes):
                self.report({'ERROR'},'Mesh vertices must remain the corners of an axis-aligned box');return {'CANCELLED'}
            if any(abs((a[0]+a[1])/2)>1e-5 for a in axes):
                self.report({'ERROR'},'Keep each box mesh centred on its object origin');return {'CANCELLED'}
            d=[float(x) for x in obj.dimensions]
            if not all(math.isfinite(x) and x>0 for x in d):
                self.report({'ERROR'},'Invalid box dimensions');return {'CANCELLED'}
            colour=[round(max(0,min(1,float(c)))*255) for c in obj.color[:3]]+[100]
            objects.append({'name':obj.name,'template_id':10009001,
                'position':[loc.x+self.origin_x,loc.z+self.origin_y,-loc.y+self.origin_z],
                'rotation':[0,0,0],'scale':[d[0],d[2],d[1]],'color':colour,
                'collision':False,'climb':False,'enable_collision':False,'enable_climb':False,
                'enable_out_of_range_run':False,'out_of_range_display_mode':0})
        if not 1<=len(objects)<=32:self.report({'ERROR'},'This lesson supports 1 to 32 boxes');return {'CANCELLED'}
        dest=Path(self.filepath)
        if dest.exists():self.report({'ERROR'},'Choose a new filename; existing exports are preserved');return {'CANCELLED'}
        dest.write_text(json.dumps({'format':'miliastra-lesson-boxes-v1','basis':'Blender X,Y,Z -> game X,Z,-Y; dimensions X,Z,Y; zero rotations',
            'scale_contract':'One Blender unit is represented by one native box scale unit; no arbitrary mesh or metre-size claim.',
            'origin_game':[self.origin_x,self.origin_y,self.origin_z],'objects':objects},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        self.report({'INFO'},f'Exported {len(objects)} explicit native boxes');return {'FINISHED'}

def menu(self,context):self.layout.operator(EXPORT_SCENE_OT_miliastra_boxes.bl_idname,text='Miliastra Boxes (.json)')
def register():
    old=getattr(bpy.types,'EXPORT_SCENE_OT_miliastra_boxes',None)
    if old:
        try:bpy.utils.unregister_class(old)
        except RuntimeError:pass
    bpy.utils.register_class(EXPORT_SCENE_OT_miliastra_boxes)
    bpy.types.TOPBAR_MT_file_export.append(menu)
if __name__=='__main__':register()
