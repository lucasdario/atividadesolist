from textwrap import dedent
from random import *
from .processing_data import *


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
                    4 - Cadastrar um marketplace
                    5 - Cadastrar um categoria
                    6 - Cadastrar um subcategoria                                        
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
    # return list


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
    # return list


def add_marketplace(name: str,) -> bool:
    log('add_marketplace')
    if writefiles(name, 0):
        return True
    return False


def add_category(name: str,) -> bool:
    log('add_category')
    if writefiles(name, 1):
        return True
    return False


def add_subcategory(name: str,) -> bool:
    log('add_subcategory')
    if writefiles(name, 2):
        return True
    return False


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


def link(user_option: int, operation_type: int):
    marketplace_name = []
    category_name = []
    sub_category_name = []
    category_position = []
    sub_category_position = []
    final_list = []

# ESTE BLOCO LOCALIZA O NOME DO MARKEPLACE
    lst_martkeplaces = list_martkeplaces()
    for i in lst_martkeplaces:
        temp_ = i.split(',')
        if temp_[0] == str(user_option):
            marketplace_name.append(temp_[1])

# ESTE BLOCO LOCALIZA A CATEGORIA e SUBCATEGORIA RELACIONADA COM O MARKETPLACE
    lst_link = readfiles(3)
    for j in lst_link:
        temp_ = j.split(',')
        if temp_[0] == str(user_option):
            category_position.append(temp_[1])

    for o in lst_link:
        temp_ = o.split(',')
        if temp_[0] == str(user_option):
            sub_category_position.append(temp_[2])

# ESTE BLOCO LOCALIZA O NOME DA CATEGORIA
    lst_category = list_category()
    for c in category_position:
        for p in lst_category:
            temp_ = p.split(',')
            if temp_[0] == str(c):
                category_name.append(temp_[1])

# ESTE BLOCO LOCALIZA O NOME DA SUBCATEGORIA
    lst_sub_category = list_sub_category()
    for t in sub_category_position:
        for y in lst_sub_category:
            temp_ = y.split(',')
            if temp_[0] == str(t):
                sub_category_name.append(temp_[1])

    print('teste')


# link(0, 0)
