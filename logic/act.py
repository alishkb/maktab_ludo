from random import randrange
from logic.move import *


def dice():
    return randrange(1, 7)


def player_home(players_num):
    if players_num == 2:
        return [0, 12]
    elif players_num == 3:
        return [0, 6, 12]
    else:
        return [0, 6, 12, 18]


def player_out(players_num):
    if players_num == 2:
        return ['s1', 's3']
    elif players_num == 3:
        return ['s1', 's2', 's3']
    else:
        return ['s1', 's2', 's3', 's4']


def player_win(players_num):
    if players_num == 2:
        return ['f1', 'f3']
    elif players_num == 3:
        return ['f1', 'f2', 'f3']
    else:
        return ['f1', 'f2', 'f3', 'f4']


def check_final(user, pos, user_win):
    for i in range(1, 5):
        if pos[f'{user}{i}'] != user_win:
            return False
    return True


def check_end(users, pos, end_list):
    for n in range(len(users)):
        for i in range(1, 5):
            if pos[f'{users[n]}{i}'] != end_list[n]:
                return False
    return True


def check_marks(user, chance, pos, home):
    for choice in range(1, 5):
        if check_mark(user, choice, chance, pos, home):
            return True
    return False

    # pos_test = pos
    # if check_marks(user, chance, pos_test, home):
    #     print(pos)
    #     print(pos_test)
    #     print('you should choose another mark!')
    # else:
    #     k += 1
    #     break


def check_mark(user, choice, chance, pos, home):
    now = pos[f'{user}{choice}']
    if home in [(now + i) % 24 for i in range(1, chance + 1)] and now != -1:
        if go_win(user, pos):
            return "WIN"
        else:
            return True
    else:
        cell = (now + chance) % 24
        if now == -1:
            if chance == 6:
                if check(user, home, pos):
                    return True
                else:
                    return False
            else:
                return False
        elif now == 100:
            return False
        elif check(user, cell, pos):
            return True
        else:
            return False

# def check_marks(user, chance, pos_test, home):
#     for i in range(1, 5):
#         if moving(user, i, chance, pos_test, home):
#             return True
#     return False
