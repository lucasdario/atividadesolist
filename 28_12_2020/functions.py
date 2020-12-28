from os import read, readlink
from textwrap import dedent
from random import *
from processing_data import *
import datetime as datetime


def boot():
    createfile()


def show_menu():
    print(dedent('''
                    #######################
                    ######MARKETPLACES#####
                    #######################
                    #
                    Escolha uma das opções abaixo:
                    1 - Lista de Marketplaces
                    2 - Lista de categorias por Marketplaces
                    3 - Lista de sub categorias
                    0 - Sair
    '''))


def list_martkeplaces():
    log('list_marketplaces')
    list = readfiles(0)
    return list


def list_category():
    log('list_category')
    list = readfiles(1)
    random_list = []
    index = 0

    while index < 3:
        random_ = int(random_number(len(list)))
        for i, name in enumerate(list):
            if i == random_:
                random_list.append(name)
        index += 1
    return random_list


def list_sub_category():
    log('list_sub_category')
    list = readfiles(2)
    random_list = []
    index = 0

    while index < 5:
        random_ = int(random_number(len(list)))
        for i, name in enumerate(list):
            if i == random_:
                random_list.append(name)
        index += 1
    return random_list


def check_int(var):
    try:
        int(var)
    except ValueError:
        return False
    return True


def print_info(message: str):
    print(dedent(
        f'''
        ***********************
        => {message}
        ***********************
    '''))


def random_number(max: int):
    return randrange(0, int(max))


def log(function_name: str):
    root = 'files/'
    file = open(f'{root}log.txt', 'a')
    data = datetime.datetime.now()
    file.write(data.strftime(
        f"%d/%m/%Y às %H:%M:%S => Acesso a função {function_name}\n"))
    file.close()


def link(user_option: int, operation_type: int):
    marketplace_name = ''
    category_name = ''
    category_position = ''
    sub_category_position = ''
    sub_category_name = ''
    lst_final = []

# ESTE BLOCO LOCALIZA O NOME DO MARKEPLACE
    lst_martkeplaces = list_martkeplaces()
    for i in lst_martkeplaces:
        temp_ = i.split(',')
        if temp_[0] == str(user_option):
            marketplace_name = temp_[1]

# ESTE BLOCO LOCALIZA A CATEGORIA e SUBCATEGORIA RELACIONADA COM O MARKETPLACE
    lst_link = readfiles(3)
    for j in lst_link:
        temp_ = j.split(',')
        if temp_[0] == str(user_option):
            category_position = temp_[1]

    for o in lst_link:
        temp_ = o.split(',')
        if temp_[0] == str(user_option):
            sub_category_position = temp_[2]

# ESTE BLOCO LOCALIZA O NOME DA CATEGORIA
    lst_category = list_category()
    for p in lst_category:
        temp_ = p.split(',')
        if temp_[0] == str(category_position):
            category_name = temp_[1]

# ESTE BLOCO LOCALIZA O NOME DA SUBCATEGORIA
    lst_sub_category = list_sub_category()
    for y in lst_sub_category:
        temp_ = y.split(',')
        if temp_[0] == str(sub_category_position):
            sub_category_name = temp_[1]

    print(f'{marketplace_name} - {category_name} - {sub_category_name}')


#link(0, 0)
