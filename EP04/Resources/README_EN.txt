EP04 native resources

Woodland_EP04_FiveCoins.gil is the complete original lesson save.
EP04_Coin_Enter_Minimal.gia is the two-node event/print graph.
EP04_Coin_Pickup_Complete.gia is the tested original pickup graph.
EP04_Coin_Pickup_Readable.gia is the equivalent graph exported from an independently copied save after node positions were arranged for reading. The original export is preserved.

Graph-only .gia files do not create the required Player/coin variables or trigger component for you. Define Player standard Coins Integer0, each Adventure Coin PickedUp BooleanNo, character-only Collision Trigger Sphere radius1, Initially EffectiveYes. Mount the intended Server Entity graph on each coin. Generated IDs can differ in your save.

The complete original and readable examples have bounded single-player pickup/log evidence. Exact exported files were not separately reimported. Keep your source card and first test reused resources in a separate copy. No multiplayer, permanent currency, natural settlement or isolated no-destruction guard stress test is claimed.
