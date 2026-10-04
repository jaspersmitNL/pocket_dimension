scoreboard players reset @s pocket_dimension.leave_game
execute unless dimension pocket_dimension:realm run return fail

data modify storage pocket_dimension:temp register_exit.UUID set from entity @s UUID
function pocket_dimension:read_exit_register_follow with storage pocket_dimension:temp register_exit
