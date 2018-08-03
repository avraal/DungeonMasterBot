import discord
import random
import math
import src

TOKEN = src.__TOKEN__
client = discord.Client()


def attack(who, damage, target, target_ac, modifier=0):
    res = 'Type mismatch'
    if not isinstance(who, str):
        return res + ': who'

    if not isinstance(target, str):
        return res + ': target'

    if not isinstance(int(target_ac), int):
        return res + ': target ac'

    if not isinstance(int(modifier), int):
        return res + ': modifier'

    _d = damage.split('d')
    _dmg = 0
    print(_d)
    if len(_d) == 2:
        for x in range(int(_d[0])):
            _res = int(random.uniform(1, int(_d[1])))
            print(_res)
            _dmg += _res
        damage = str(_dmg)

    print(damage)
    m = random.uniform(1, 20)
    if (m + int(modifier)) > int(target_ac):
        res = who + ' нанёс ' + target + ' ' + damage + ' урона'
    else:
        res = who + ' промазал'

    return res


def dice_parse(dice):
    _d = dice[1].split('d')
    if len(_d) != 2:
        _d = dice[1].split('к')
        if len(_d) != 2:
            return None

    if _d[0] == '' or _d[1] == '':
        return None

    _result = 0
    _text_info = ''
    for x in range(int(_d[0])):
        _tmp = int(random.uniform(1, int(_d[1])))
        _text_info += _d[0] + 'd' + _d[1] + ' = ' + str(_tmp) + '\n'
        _result += _tmp

    _text_info += str(_result)
    return _text_info


def show_help():
    _res = show_roll_help()
    _res += show_attack_help()
    _res += show_chrs_help()
    return _res


def show_roll_help():
    _res = '```dsconfig\n'
    _res += 'Используйте команду !roll для генерации случайных значений\n'
    _res += 'Возможные варианты использования этой команды:\n'
    _res += '!roll 2d4\n!roll 4d8 +2\n!roll 1d10 1\n!roll 1d20 -3\n'
    _res += 'Букву `d` можно заменить на букву `к`\n'
    _res += '```\n'
    return _res


def show_attack_help():
    _res = '```dsconfig\n'
    _res += 'Команда !attack позволит вам воспроизвести простую сцену с нанесением урона\n'
    _res += 'Формат: `!attack <инициатор> <урон> <цель> <КД цели> [<модификатор>]`\n'
    _res += 'Например:\n'
    _res += '!attack Трактирщик 5 Гоблин 10\n'
    _res += '!attack Гоблин 9 Трактирщик 8 +2\n'
    _res += '!attack Трактирщик 2d4 Таракан 4\n'
    _res += '```\n'
    return _res


def show_chrs_help():
    _res = '```dsconfig\n'
    _res += 'Команда `!chrs` позволяет посчитать значение вашей характеристики и модификатор для неё\n'
    _res += 'Используйте `!chrs Телосложение` для того, чтобы высчитать значение вашей характеристики\n'
    _res += 'Или `!chrs` чтобы получить значение для анонимной характеристики\n'
    _res += '```\n'
    return _res


def roll_charac():
    _res = just_roll('4d6')
    if _res is None:
        return

    _m = (_res - 10) / 2
    _m = int(_m)
    return str(_res) + ' (' + str(_m) + ')'


def chrs_roll():
    vals = [0] * 10
    for x in range(4):
        vals[x] = int(random.uniform(1, 6))

    _min = min(vals)
    vals.remove(_min)

    _sum = sum(vals)
    _m = int(math.floor((_sum - 10) / 2))
    _r = str(_m)
    if _m > 0:
        _r = '+' + str(_m)
    return str(_sum) + ' (' + _r + ')'


def just_roll(dice):
    _d = dice.split('d')
    if len(_d) != 2:
        _d = dice.split('к')
        if len(_d) != 2:
            return None

    if _d[0] == '' or _d[1] == '':
        return None

    _res = 0
    for x in range(int(_d[0])):
        _res += int(random.uniform(1, int(_d[1])))

    return _res


def roll(c):
    res = 0
    msg = ''
    text_res = ''
    if c[1] == '':
        msg = 'Не верно указан дайс'

    else:
        text_res = dice_parse(c)
        if text_res is not None:
            res = text_res.split('\n')[-1]
            if len(c) > 2:
                _m = int(c[2])
                s = ''
                if _m >= 0:
                    s = '+'
                res += s + str(_m) + ' = ' + str(int(res) + int(c[2]))
            else:
                res = ''
            msg = text_res + '\n' + res
        else:
            msg = 'Не верно введена команда. Используйте `!roll` для получения информации'
    return msg


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    target = message.channel
    msg = ''

    if message.content.startswith('!help'):
        msg = show_help()
        target = message.author

    if message.content.startswith('!attack'):
        a = message.content.split(' ')
        if len(a) == 5:
            msg = attack(a[1], a[2], a[3], a[4])
            print(msg)
        elif len(a) == 6:
            msg = attack(a[1], a[2], a[3], a[4], a[5])
        else:
            msg = show_attack_help()
            target = message.author

    if message.content.startswith('!chrs'):
        a = message.content.split(' ')
        if len(a) == 1:
            msg = chrs_roll()
        elif len(a) == 2:
            msg = a[1] + ': ' + chrs_roll()
        else:
            show_chrs_help()

    if message.content.startswith('!roll'):
        _c = message.content.split(' ')
        if len(_c) == 1:
            msg = show_roll_help()
            target = message.author
        elif len(_c) > 1:
            msg = roll(_c)

    if msg:
        await client.send_message(target, msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')
    game = discord.Game(name='Dungeon & Dragons')
    await client.change_presence(game=game)


client.run(TOKEN)
