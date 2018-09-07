import discord
import random
import math
import src

TOKEN = src.__TOKEN_MASTER_
client = discord.Client()


def send_frog():
    frog = ':frog::frog::frog::frog::frog::frog::frog:\n' + ':frog::frog::frog::frog::frog::frog::frog::frog::frog:\n' + ':frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog:\n' + ':frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog:\n' + ':frog::frog::white_circle:️:black_circle:️:black_circle:️:white_circle:️:frog::frog::frog::white_circle:️:black_circle:️:black_circle:️:white_circle:️\n' + ':frog::white_circle:️:black_circle:️:black_circle:️:white_circle:️:black_circle:️:white_circle:️:frog::white_circle:️:black_circle:️:black_circle:️:white_circle:️:black_circle:️:white_circle:️\n' + ':frog::white_circle:️:black_circle:️:white_circle:️:black_circle:️:black_circle:️:white_circle:️:frog::white_circle:️:black_circle:️:white_circle:️:black_circle:️:black_circle:️:white_circle:️\n' + ':frog::frog::white_circle:️:black_circle:️:white_circle:️:white_circle:️:frog::frog::frog::white_circle:️:black_circle:️:white_circle:️:white_circle:️\n' + ':frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog:\n' + ':red_circle::red_circle::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog:\n' + ':frog::red_circle::red_circle::frog::frog::frog::frog::frog::frog::frog::frog::frog:\n' + ':frog::frog::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle:\n' + ':frog::frog::frog::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle:\n' + ':frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog:\n' + ':frog::frog::frog::frog::frog::frog::frog::frog::frog::frog:\n' + ':frog::frog::frog::frog::frog::frog::frog::frog::frog: '
    return frog


def gold(player_class):
    if not player_class:
        return 0

    class_list = ['бард 5d4', 'варвар 2d4', 'воин 5d4', 'волшебник 4d4',
                  'друид 2d4', 'жрец 5d4', 'колдун 4d4', 'монах 5d4',
                  'паладин 5d4', 'плут 4d4', 'следопыт 5d4', 'чародей 3d4']
    player_class = player_class.lower()
    match = [s for s in class_list if player_class in s.split(' ')[0]]
    if not match:
        return show_gold_help()
    _tmp = match[0].split(' ')
    gold_count = just_roll(_tmp[1])
    if _tmp[0] == str.lower('монах'):
        return gold_count
    else:
        return gold_count * 10


def attack(who, damage, target, target_ac, modifier=0):
    res = 'Type mismatch'
    if not isinstance(who, str):
        return res + ': who'

    if not isinstance(target, str):
        return res + ': target'

    if not target_ac.isdigit():
        return res + ': КД цели'

    # if not isinstance(modifier, int):
    #     return res + ': Модификатор'

    _d = damage.split('d')
    _dmg = 0
    if len(_d) == 2:
        for x in range(int(_d[0])):
            _res = int(random.uniform(1, int(_d[1])))
            _dmg += _res
        damage = str(_dmg)

    miss_list = ['{} усердно бросается скверными словечками в {}, но промахивается'.format(who, target),
                 'Замахиваясь мечём {} задумался о смысле жизни. Пока думал, {} ушёл по своим делам'.format(who,
                                                                                                            target),
                 '{} испугался {}, и {} его пожалел'.format(target, who, who),
                 '{} сделал выпад своим оружием, но {} в этом не заинтересован'.format(who, target),
                 'Мощное заклинание полетело в {}... А нет, не полетело'.format(target),
                 'Когда {} попытался атаковать {}, с неба послышался голос: \"Не бей, подумай\", и {} подумал'.format(
                     who, target, who),
                 '{} нанёс пацифистическую атаку в 0 урона'.format(who),
                 '{} наносил огромное количество урона по {}, а потом проснулся'.format(who, target),
                 'Пафосно хвастаясь своим оружием, {} подбросил его в воздух, но оно так и не вернулось. С неба '
                 'послышалось тихое: \"Ай.\"'.format(who),
                 'Нет',
                 '{} кувыркался как мог'.format(target),
                 '{} сел на пегаса и улетел'.format(target),
                 '{} увернулся, потому что может'.format(target),
                 'Запуская магический шар в {}, шар летел так долго, что он обрёл разум, и когда он был возле {}, '
                 'шар решил полететь по своим делам'.format(target, target),
                 'Купил {} шляпу на бонус к уворотам, а она ему как раз'.format(target)]

    attack_list = ['{} сначала не мог попасть по {}, а потом как смог. Аж на {} урона'.format(who, target, damage),
                   '{} нанёс {} урона, а потом проснулся. А потом снова нанёс {} урона'.format(who, damage, damage),
                   '{} слишком сильно уворачивался, что нанёс сам себе {} урона'.format(target, damage),
                   '{} докувыркался на {} урона'.format(target, damage),
                   '{} в этот раз выбрал пики. ({} урона)'.format(target, damage),
                   'Ну, что ты {} притих... {} урона в груди'.format(target, damage),
                   'Атакуя мизинцем по тумбочке, {} нанёс {} урона и {}'.format(who, damage, target),
                   '{} угостил {} шаурмой. Пищёвое отравление в {} урона'.format(who, target, damage),
                   '{} выпил зелье здоровья 2 раза. Как известно, плюс на плюс даёт минус. {} получает {} урона'.format(
                       target, target, damage),
                   '{} мастерски пытался уворачиваться, но сегодня кубики не на его стороне аж на {} урона'.format(
                       target, damage),
                   'Путь к сердцу {} лежит через {} урона'.format(target, damage),
                   '{} роняет не только запад, но и {} на {} урона'.format(who, target, damage)]

    if modifier == '666':
        res = ''
        for x in range(len(miss_list)):
            res += str(x) + ')' + miss_list[x] + '\n'
        res += '\n'
        for x in range(len(attack_list)):
            res += str(x) + ')' + attack_list[x] + '\n'
        return res

    m = int(random.uniform(1, 20))
    print(m)

    if (m + modifier) > int(target_ac):
        res = attack_list[(int(random.uniform(0, len(attack_list))))]
    else:
        res = miss_list[int(random.uniform(0, len(miss_list)))]

    if m == 20:
        res = 'Критическое попадание по ' + target
    elif m == 1:
        res = 'Критический промах\n'
        res += send_frog()

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
    _res += show_gold_help()
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
    _res += '`!chrs full` позволит вам получить полный набор характеристик\n'
    _res += '```\n'
    return _res


def show_gold_help():
    _res = '```dsconfig\n'
    _res += 'Быстрая генерация количества золота для вашего персонажа\n'
    _res += 'Используйте `!gold <класс>` чтобы узнать сколько у вас золота\n'
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
        elif len(a) == 6:
            msg = attack(a[1], a[2], a[3], a[4], a[5])
        else:
            msg = show_attack_help()
            target = message.author

    if message.content.startswith('!gold'):
        a = message.content.split(' ')
        if len(a) == 2:
            msg = gold(a[1])
        else:
            target = message.author
            msg = show_gold_help()

    if message.content.startswith('!frog'):
        msg = send_frog()

    if message.content.startswith('!chrs'):
        a = message.content.split(' ')
        if len(a) == 1:
            msg = chrs_roll()
        elif len(a) == 2:
            if a[1] == 'full':
                msg = 'Сила: ' + chrs_roll() + '\n'
                msg += 'Ловкость: ' + chrs_roll() + '\n'
                msg += 'Телосложение: ' + chrs_roll() + '\n'
                msg += 'Интеллект: ' + chrs_roll() + '\n'
                msg += 'Мудрость: ' + chrs_roll() + '\n'
                msg += 'Харизма: ' + chrs_roll()
            else:
                msg = a[1] + ': ' + chrs_roll()
        elif len(a) > 2:
            target = message.author
            msg = show_chrs_help()

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
