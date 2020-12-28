from os import read
from textwrap import dedent
from random import *
from processing_data import *


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
    # list = ['Casas Bahia', 'Ponto Frio', 'Extra',
    #         'Mercado Libre', 'Americanas']
    list = readfiles(0)
    return list


def list_category():
    # list = ['Eletrônicos', 'Eletrodomésticos', 'Brinquedos',
    #         'Móveis', 'Informática', 'Telefonia', 'Serviços', 'Ofertas TV', 'Áudio', 'Bebês']
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
    # list = ['Smartphone', 'PC', 'Notebook', 'Sofá', 'Geladeira', 'Freezer',
    #         'Lava e Seca', 'Bonecos', 'Pelúcias', 'Cama', 'Impressora', 'HD Externo',
    #         'PenDrive', 'Carrinho de bebê', 'Chupeta', 'Fraldas']
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
