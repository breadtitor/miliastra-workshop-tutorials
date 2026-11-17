EP06 native resources

Woodland_EP06_TimedRun.gil is the complete exported timed lesson. EP06_Round_Controller.gia is the Player controller graph only: it requires the matching Player flags, timer definition/component, HUD and actual Start instance ID. It does not replace the RoundActive gate in the coin graph.

Timer: Round Timer / Countdown120seconds. UI source Player Themself. Player Global Timer component has no automatic timer reference. Standard Player Boolean RoundStarted and RoundActive defaultNo. Preserve existing Coins0, ProgressMin0 and CoinGoal5 Integers.

Single-player tests covered before-Start pickup gating, repeated Start, natural120-second Victory/Coins5, Retry initial0 and natural120-second Failed/Coins0. Exact exported files were not reimported in this episode. Preserve source cards and test imports separately.
