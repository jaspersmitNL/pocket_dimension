$execute if data storage pocket_dimension:exit_register list[{UUID:$(UUID)}] run return run function pocket_dimension:leave_pocket_follow with storage pocket_dimension:exit_register list[{UUID:$(UUID)}]

# Recover at the saved world spawn when the player has no exit record.
function pocket_dimension:leave_rift_follow with storage pocket_dimension:temp world_spawn
