from enum import Enum, unique


@unique
class BotCommands(Enum):
    ROLL = '!roll'
    ATTACK = '!attack'
    CHRS = '!chrs'
    GOLD = '!gold'
    NEW_MODULE = '!new_module'
    INVITE = '!invite'
    HELP = '!help'
    ADD_USER = '!add_user'
    FACE = '!face'
    SHOW_USERS = '!show_users'
    SHOW_MODULES = '!show_modules'
    FROG = '!frog'
