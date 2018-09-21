import discord
import random
import math
import requests
import src

TOKEN = src.__TOKEN_BAKA_
client = discord.Client()

# midety, infernion, Freddy_Krueger, Oretachi (лсм) [Максим]

me_list = ['268063167299584001']

member_list = ['262139393203109890',
               '357202311187136512',
               '295946057152593930',
               '219113291706925056']


# TODO: Added Veronic


def send_invites(author, invite_link):
    message = 'Здравствуй, путник. Пишу тебе, так как нуждаюсь в твоей помощи. Недавно я и мои братья смогли отыскать ' \
              'давно затерянную шахту. Это не просто шахта, для нас и для всего материка Фаэруна она несёт огромную ' \
              'ценность. Но, о подробностях позже. Я буду ждать тебя в таверне Гнилое Яблоко, что в Невервинтере, ' \
              'приходи, если хочешь увековечить своё имя в истории Фаэруна.'

    embed = discord.Embed(title='Рудники Фанделвера', description=message, color=0x35af1a)
    embed.set_thumbnail(url=author.avatar_url)
    embed.add_field(name='Подпись', value='Гандрен Роксикер', inline=True)
    embed.add_field(name='Таверна Гнилое Яблоко', value=invite_link)
    return embed


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
        return show_gold_help(get_help_response())
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
    print(dice)
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


def get_help_response():
    data = requests.post('http://taskbox.zzz.com.ua/execCommand.php', data={'from': 'Discord', 'cmd': 'help'})
    print(data)
    return data


def show_help():
    _r = requests.post('http://taskbox.zzz.com.ua/execCommand.php', data={'from': 'Discord', 'cmd': 'help'})
    _res = show_roll_help(_r)
    _res += show_attack_help(_r)
    _res += show_chrs_help(_r)
    _res += show_gold_help(_r)
    _res += '\nMessage from ' + _r.json()['text'][0]['from']
    return _res


def show_roll_help(req):
    _res = '```dsconfig\n'
    _res += req.json()['text'][0]['roll']
    _res += '```\n'
    return _res


def show_attack_help(req):
    _res = '```dsconfig\n'
    _res += req.json()['text'][0]['attack']
    _res += '```\n'
    return _res


def show_chrs_help(req):
    _res = '```dsconfig\n'
    _res += req.json()['text'][0]['chrs']
    _res += '```\n'
    return _res


def show_gold_help(req):
    _res = '```dsconfig\n'
    _res += req.json()['text'][0]['gold']
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


def show_base_info():
    step1 = '```\nОСТОРОЖНО, МНОГО ТЕКСТА\n```'
    step2 = 'Прежде чем создавать своего персонажа, потратьте немного времени на то, чтобы представить кем бы вы ' \
            'хотели играть, не взирая на то какие классы и расы есть в dnd\n' \
            'В игре нет ограничений по типу "За определённую расу могут играть определённые классы", каждый играет ' \
            'кого и как хочет\n' \
            'Через некоторое время я скину вам необходимую инфу для того, чтобы создать персонажа и ознакомиться с ' \
            'правилами в целом\n' \
            'Всё это будет описано в книге под названием "Книга игрока" на 330 страниц, я скину pdf(изменено)\n' \
            'Не пугайтесь объёма информации в том руководстве, ибо в нём расписано абсолютно всё, что вам будет ' \
            'необходимо\n' \
            'Хочу заметить, что лучше всего изучать эту книгу в процессе создания персонажа\n' \
            'Когда я скину вам книгу, вам нужно будет:\n' \
            '1. Выбрать расу\n' \
            '2. Выбрать класс\n' \
            '3. Придумать предысторию\n' \
            '4. Придумать характер\n\n' \
            '1 и 2 пункт вы можете выполнять прямо сейчас\n'

    return step1 + step2


def modif_parse(modif, chrs):
    for k, v in chrs.items():
        tmp = v.split(' ')[1].replace('(', '').replace(')', '')
        modif[k] = tmp

    return modif


def skills_roll(chrs):
    modif = {'Сила': 0, 'Мудрость': 0, 'Интеллект': 0, 'Ловкость': 0, 'Телосложение': 0, 'Харизма': 0}
    modif = modif_parse(modif, chrs)
    for k, v in modif.items():
        print(k + ': ' + v)

    skills = {'Акробатика': modif['Ловкость'], 'Обман': modif['Харизма'], 'Медицина': modif['Мудрость'],
              'Анализ': modif['Интеллект'], 'Ловкость рук': modif['Ловкость'], 'Атлетика': modif['Сила'],
              'Внимательность': modif['Мудрость'], 'Выживание': modif['Мудрость'], 'Выступление': modif['Харизма'],
              'Запугивание': modif['Харизма'], 'История': modif['Интеллект'], 'Проницательность': modif['Мудрость'],
              'Религия': modif['Интеллект'], 'Скрытность': modif['Ловкость'], 'Убеждение': modif['Харизма'],
              'Уход за животными': modif['Мудрость']}
    mes = '\n`Навыки:`\n\n'
    for k, v in skills.items():
        mes += k + ': ' + v + '\n'
    mes += 'Не забудьте добавить + Бонус мастерства выбранным навыкам'
    return mes


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    target = message.channel
    msg = ''

    if message.content.startswith('!check'):
        msg = show_base_info()

    if message.content.startswith('!help'):
        msg = show_help()
        target = message.author

    if message.content.startswith('!invite'):
        can_permission = False
        for r in message.author.roles:
            if r.name != 'Dungeon master':
                msg = 'У вас нет прав для отправки этой команды'
            else:
                can_permission = True
                msg = ''
                break

        if can_permission is True:
            role = []
            for r in message.server.roles:
                if r.id == '491859757460881408':  # Role "Dungeon Player"
                    role.append(r)
            for m in range(len(me_list)):  # TODO: change me_list on member_list
                _t = message.server.get_member(me_list[m])  # TODO: change me_list on member_list
                await client.add_roles(_t, *role)

            channel = client.get_channel('491860222495686676')  # Channel "Гнилое Яблоко"
            invite_link = await client.create_invite(destination=channel)
            embed_author = await client.get_user_info('474484991485673472')  # User "Dungeon Master"
            users = []
            for m in me_list:  # TODO: change me_list on member_list
                users.append(await client.get_user_info(m))

            embed = send_invites(embed_author, invite_link)

            for u in users:
                await client.send_message(u, embed=embed)

    if message.content.startswith('!attack'):
        a = message.content.split(' ')
        if len(a) == 5:
            msg = attack(a[1], a[2], a[3], a[4])
        elif len(a) == 6:
            msg = attack(a[1], a[2], a[3], a[4], a[5])
        else:
            msg = show_attack_help(get_help_response())
            target = message.author

    if message.content.startswith('!gold'):
        a = message.content.split(' ')
        if len(a) == 2:
            msg = gold(a[1])
        else:
            target = message.author
            msg = show_gold_help(get_help_response())

    if message.content.startswith('!frog'):
        msg = send_frog()

    if message.content.startswith('!chrs'):
        a = message.content.split(' ')
        if len(a) == 1:
            msg = chrs_roll()
        elif len(a) == 2:
            chrs = {'Сила': '', 'Ловкость': '', 'Телосложение': '', 'Интеллект': '', 'Мудрость': '', 'Харизма': ''}

            if a[1] == 'full':
                chrs['Сила'] = chrs_roll()
                chrs['Ловкость'] = chrs_roll()
                chrs['Телосложение'] = chrs_roll()
                chrs['Интеллект'] = chrs_roll()
                chrs['Мудрость'] = chrs_roll()
                chrs['Харизма'] = chrs_roll()

                for k, v in chrs.items():
                    msg += k + ': ' + v + '\n'

                msg += skills_roll(chrs)
            else:
                msg = a[1] + ': ' + chrs_roll()
        elif len(a) > 2:
            target = message.author
            msg = show_chrs_help(get_help_response())

    if message.content.startswith('!roll'):
        _c = message.content.split(' ')
        if len(_c) == 1:
            msg = show_roll_help(get_help_response())
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
