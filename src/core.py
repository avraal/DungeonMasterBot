import re
import datetime
import discord
import random
import math
import requests
import sys
sys.path.append('../')
import src
from src.botcommands import BotCommands

TOKEN = src.__TOKEN_MASTER_
client = discord.Client()


def send_invites(author, invite_link, module_name, desc, channel_name):
    embed = discord.Embed(title=module_name, description=desc, color=0x35af1a)
    embed.set_thumbnail(url=author.avatar_url)
    embed.add_field(name='Подпись', value=channel_name, inline=True)
    embed.add_field(name="DungeonMaster", value=invite_link)
    return embed


def send_frog():
    frog = ':frog::frog::frog::frog::frog::frog::frog:\n' + ':frog::frog::frog::frog::frog::frog::frog::frog::frog:\n' + ':frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog:\n' + ':frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog:\n' + ':frog::frog::white_circle:️:black_circle:️:black_circle:️:white_circle:️:frog::frog::frog::white_circle:️:black_circle:️:black_circle:️:white_circle:️\n' + ':frog::white_circle:️:black_circle:️:black_circle:️:white_circle:️:black_circle:️:white_circle:️:frog::white_circle:️:black_circle:️:black_circle:️:white_circle:️:black_circle:️:white_circle:️\n' + ':frog::white_circle:️:black_circle:️:white_circle:️:black_circle:️:black_circle:️:white_circle:️:frog::white_circle:️:black_circle:️:white_circle:️:black_circle:️:black_circle:️:white_circle:️\n' + ':frog::frog::white_circle:️:black_circle:️:white_circle:️:white_circle:️:frog::frog::frog::white_circle:️:black_circle:️:white_circle:️:white_circle:️\n' + ':frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog:\n' + ':red_circle::red_circle::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog:\n' + ':frog::red_circle::red_circle::frog::frog::frog::frog::frog::frog::frog::frog::frog:\n' + ':frog::frog::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle:\n' + ':frog::frog::frog::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle::red_circle:\n' + ':frog::frog::frog::frog::frog::frog::frog::frog::frog::frog::frog:\n' + ':frog::frog::frog::frog::frog::frog::frog::frog::frog::frog:\n' + ':frog::frog::frog::frog::frog::frog::frog::frog::frog: '
    return frog


def send_face():
    face = ':new_moon::new_moon::new_moon::new_moon::new_moon::new_moon::new_moon::new_moon:\n' + ':new_moon::new_moon::new_moon::new_moon::new_moon::new_moon::new_moon::new_moon:\n' + ':new_moon::new_moon::new_moon::waxing_crescent_moon::full_moon::waning_gibbous_moon::new_moon::new_moon:\n' + ':new_moon::waxing_crescent_moon::full_moon::full_moon::full_moon::full_moon::waning_gibbous_moon::new_moon:\n' + ':new_moon::waxing_gibbous_moon::eye::nose::eye::full_moon::full_moon::last_quarter_moon:\n' + ':new_moon::full_moon::full_moon::lips::full_moon::full_moon::full_moon::ear:\n' + ':new_moon::waxing_gibbous_moon::full_moon::full_moon::full_moon::full_moon::full_moon::full_moon:\n' + ':new_moon::waxing_crescent_moon::full_moon::full_moon::full_moon::full_moon::full_moon::full_moon:\n' + ':new_moon::new_moon::full_moon::full_moon::full_moon::full_moon::full_moon::full_moon:\n'
    return face


def gold(player_class):
    if not player_class:
        return 0

    class_list = ['бард 5d4', 'варвар 2d4', 'воин 5d4', 'волшебник 4d4',
                  'друид 2d4', 'жрец 5d4', 'колдун 4d4', 'монах 5d4',
                  'паладин 5d4', 'плут 4d4', 'следопыт 5d4', 'чародей 3d4']
    player_class = player_class.lower()
    match = [s for s in class_list if player_class in s.split(' ')[0]]
    if not match:
        return show_help(BotCommands.GOLD)
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
        res = 'Критическое попадание по ' + target + "\n"
        res += send_face()
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
        _tmp = int(random.uniform(1, int(_d[1]) + 1))
        _text_info += _d[0] + 'd' + _d[1] + ' = ' + str(_tmp) + '\n'
        _result += _tmp

    _text_info += str(_result)
    return _text_info


def get_help_response():
    data = requests.post(src.__exec_command_url__, data={'from': 'Discord', 'cmd': 'help'})
    return data


def show_help():
    _r = requests.post(src.__exec_command_url__, data={'from': 'Discord', 'cmd': 'help'})
    _res = ""

    for r in BotCommands:
        _res += show_help(r, _r)
    _res += '\nMessage from ' + _r.json()['text'][0]['from']
    return _res


def show_help(command_name, req=get_help_response()):
    _res = '```dsconfig\n'
    _res += req.json()['text'][0][command_name.value]
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
        _res += int(random.uniform(1, int(_d[1]) + 1))

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
    mes = '\nНавыки:\n\n'
    for k, v in skills.items():
        mes += k + ': ' + v + '\n'
    mes += 'Не забудьте добавить + Бонус мастерства выбранным навыкам'
    return mes


def new_module(module_name, author_id):
    r = requests.post(src.__create_dnd_module__url__, data={'name': module_name, 'author_d_id': author_id})
    if r.json()["code"] == 1:
        msg = 'Модуль ' + module_name + ' успешно зарегистрирован\n'
    elif r.json()["code"] == 2:
        msg = 'У вас уже есть модуль с таким именем'
    elif r.json()["code"] == 0:
        msg = 'Не удалось добавить модуль'
    else:
        msg = 'Не удалось присоедениться к базе данных'
    return msg


def add_user_to_module(module_id, user_discord_id):
    r = requests.post(src.__create_dnd_user_url__, data={'discord_id': user_discord_id, 'module_id': module_id})
    # print(r.content)
    return r.json()["code"]


def get_list_of_modules(author_id):
    r = requests.post(src.__get_dnd_modules_url__, data={'author_d_id': author_id})
    # print(r.content)
    return r.json()["modules"]


def get_users_info():
    r = requests.post(src.__get_dnd_users_url__)
    # print(r.content)
    return r.json()["users"]


def parse_invite_text(splitted_text):
    result_array = ""
    for i in range(len(splitted_text)):
        if splitted_text[i].startswith('\"'):
            result_array += splitted_text[i]
            if splitted_text[i].endswith('\"'):
                splitted_text.remove(splitted_text[i])
                break
            splitted_text.remove(splitted_text[i])
            current_position = i
            while not splitted_text[current_position].endswith("\""):
                result_array += ' ' + splitted_text[current_position]
                splitted_text.remove(splitted_text[current_position])
            result_array += ' ' + splitted_text[current_position]
            splitted_text.remove(splitted_text[current_position])
            break
    return re.sub('\"', '', result_array)


def parse_channel_name(channel_name):
    name = channel_name[1:]
    name = name.replace('-', ' ')
    name = name.title()
    return name


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    try:
        target = message.channel
        msg = ''

        if message.content.startswith(BotCommands.HELP.value):
            _res = ""
            target = message.author
            for r in BotCommands:
                _res = show_help(r)
                await client.send_message(target, _res)
            msg = "Получен весь список команд"

        if message.content.startswith(BotCommands.INVITE.value):
            a = message.content.split(' ')

            can_permission = False
            try:
                for r in message.author.roles:
                    if r.name != 'Dungeon master':
                        msg = 'У вас нет прав для отправки этой команды'
                    else:
                        can_permission = True
                        msg = ''
                        break
            except AttributeError:  # Если пользователь напишет это боту в лс
                msg = 'Эту команду необходимо вводить на сервере'
                target = message.author

            if not can_permission:
                pass
            else:
                command = message.content
                found = False
                role = []
                for r in message.server.roles:
                    if r.name == 'Dungeon Player':  # Role "Dungeon Player"
                        role.append(r)
                        found = True
                        break
                if not found:
                    msg = "На сервере отсутствует необходимая роль\n"
                    msg += show_help(BotCommands.INVITE)
                    target = message.author
                else:
                    embed_author = await client.get_user_info('474484991485673472')  # User "Dungeon Master"
                    module_name = ""
                    module_desc = ""
                    player_id = re.sub('<|>|@!', " ", a[1])
                    player_id = player_id.replace(" ", "")
                    u = message.server.get_member(player_id)
                    await client.add_roles(u, *role)

                    if command.count('\"') == 2 or command.count('\"') == 4:
                        module_name = parse_invite_text(a)
                        module_desc = parse_invite_text(a)
                        channel_id = re.sub("[<>#]", " ", a[2])
                        channel_id = channel_id.replace(" ", "")
                        channel = client.get_channel(channel_id)
                        channel_link = await client.create_invite(destination=channel, max_age=86400, unique=False)
                        embed = send_invites(embed_author, channel_link, module_name, module_desc, channel.name)
                        u = await client.get_user_info(player_id)
                        await client.send_message(u, embed=embed)
                    elif len(a) == 5:
                        channel_id = re.sub("[<>#]", " ", a[4])
                        channel_id = channel_id.replace(" ", "")
                        channel = client.get_channel(channel_id)
                        channel_link = await client.create_invite(destination=channel, max_age=86400, unique=False)
                        embed = send_invites(embed_author, channel_link, a[2], a[3], channel.name)
                        u = await client.get_user_info(player_id)
                        await client.send_message(u, embed=embed)
                    else:
                        msg = show_help(BotCommands.INVITE)
                        target = message.author

        if message.content.startswith(BotCommands.ATTACK.value):
            a = message.content.split(' ')
            if len(a) == 5:
                msg = attack(a[1], a[2], a[3], a[4])
            elif len(a) == 6:
                msg = attack(a[1], a[2], a[3], a[4], a[5])
            else:
                msg = show_help(BotCommands.ATTACK)
                target = message.author

        # TODO: Change signature to '!add_user <@user> <module>'
        if message.content.startswith(BotCommands.ADD_USER.value):
            a = message.content.split(' ')
            name = ""
            if message.content.count('\"') == 2:
                name = parse_invite_text(a)
                print(name)
            elif message.content.count('\"') == 0:
                name = a[1]
                a.remove(a[1])
            print(name)
            print(a)
            if len(a) == 2:
                try:
                    user_id = re.sub('<|>|@!', " ", a[1])
                    m_list = get_list_of_modules(message.author.id)
                    if len(m_list) != 0:
                        for m in m_list:
                            if name == m['name']:
                                msg = add_user_to_module(m['id'], user_id)
                                print(msg)
                                if msg == 1:
                                    msg = 'Пользователь добавлен к модулю'
                                elif msg == 2:
                                    msg = 'Этот пользователь уже учавствует в указаном модуле'
                                break
                            else:
                                msg = 'У вас нет модуля под названием ' + name
                    else:
                        msg = 'У вас нет модулей'
                except AttributeError:
                    msg = 'Пользователь с таким ником не найден'
            else:
                target = message.author
                msg = show_help(BotCommands.ADD_USER)

        if message.content.startswith(BotCommands.NEW_MODULE.value):
            a = message.content.split(' ')
            name = ""
            if message.content.count('\"') == 2:
                name = parse_invite_text(a)
                msg = new_module(name, message.author.id)
            else:
                target = message.author
                msg = show_help(BotCommands.NEW_MODULE)

        if message.content.startswith(BotCommands.GOLD.value):
            a = message.content.split(' ')
            if len(a) == 2:
                msg = gold(a[1])
            else:
                target = message.author
                msg = show_help(BotCommands.GOLD)

        if message.content.startswith(BotCommands.FROG.value):
            msg = send_frog()

        if message.content.startswith(BotCommands.FACE.value):
            msg = send_face()

        if message.content.startswith(BotCommands.SHOW_MODULES.value):
            lst = get_list_of_modules(message.author.id)
            for m in lst:
                msg += '```\nНазвание: ' + m['name'] + '\nМастер: ' + message.author.name + '\n```\n'

        if message.content.startswith(BotCommands.SHOW_USERS.value):
            users_info = get_users_info()
            user_wrap = []
            current_user_discord_id = 0
            count = 0
            for i in users_info:
                if i["DiscordID"] == current_user_discord_id:
                    user_wrap[count - 1]['Modules'].append(i['ModuleName'])
                else:
                    current_user_discord_id = i["DiscordID"]
                    count += 1
                    user_wrap.append({'UserID': current_user_discord_id, 'Modules': []})
                    user_wrap[count - 1]['Modules'].append(i['ModuleName'])
            for u in user_wrap:
                user = await client.get_user_info(u['UserID'])
                msg += '```\nНик: ' + user.name + '\n'
                if len(u['Modules']) != 0:
                    msg += 'Модули: '
                    for m in u['Modules']:
                        msg += m
                        if len(u['Modules']) > 1 and m != u['Modules'][-1]:
                            msg += ', '
                else:
                    msg += 'Пользователь не участвует ни в одном модуле\n'
                msg += '\n```\n'

        if message.content.startswith(BotCommands.CHRS.value):
            a = message.content.split(' ')
            if len(a) == 1:
                msg = show_help(BotCommands.CHRS)
                print(msg)
            elif len(a) == 2:
                chrs = {'Сила': '', 'Ловкость': '', 'Телосложение': '', 'Интеллект': '', 'Мудрость': '', 'Харизма': ''}

                if a[1] == 'full':
                    chrs['Сила'] = chrs_roll()
                    chrs['Ловкость'] = chrs_roll()
                    chrs['Телосложение'] = chrs_roll()
                    chrs['Интеллект'] = chrs_roll()
                    chrs['Мудрость'] = chrs_roll()
                    chrs['Харизма'] = chrs_roll()
                    msg += '```'
                    for k, v in chrs.items():
                        msg += k + ': ' + v + '\n'

                    msg += skills_roll(chrs)
                    msg += '```'
                else:
                    msg = a[1] + ': ' + chrs_roll()
            elif len(a) > 2:
                target = message.author
                msg = show_help(BotCommands.CHRS)

        if message.content.startswith(BotCommands.ROLL.value):
            _c = message.content.split(' ')
            if len(_c) == 1:
                msg = show_help(BotCommands.ROLL)
                target = message.author
            elif len(_c) > 1:
                msg = roll(_c)

        if msg:
            await client.send_message(target, msg)
    except Exception as e:
        print(e.__doc__)
        error_log = open("logs.txt", "a")
        log = str(datetime.datetime.now()) + " [ERROR]: " + str(e.__doc__) + '\n'
        error_log.write(log)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')
    game = discord.Game(name='Dungeon & Dragons')
    await client.change_presence(game=game)


client.run(TOKEN)
