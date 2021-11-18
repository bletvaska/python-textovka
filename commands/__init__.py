from .about import cmd as cmd_about
from .inventory import cmd as cmd_inventory
from .drop import cmd as cmd_drop
from .take import cmd as cmd_take
from .examine import cmd as cmd_examine
from .quit import cmd as cmd_quit
from .look_around import cmd as cmd_look_around
from .commands import cmd as cmd_commands

commands = [
    cmd_about,
    cmd_inventory,
    cmd_drop,
    cmd_take,
    cmd_examine,
    cmd_quit,
    cmd_look_around,
    cmd_commands
]
