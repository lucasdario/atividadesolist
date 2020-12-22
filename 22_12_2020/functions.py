from textwrap import dedent


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
    list = ['Casas Bahia', 'Ponto Frio', 'Extra', 'Mercado Libre']
    return list


def list_category():
    list = ['Eletrônicos', 'Eletrodomésticos', 'Brinquedos']
    return list


def list_sub_category():
    list = ['Smartphone', 'Geladeira', 'Freezer',
            'Lava e Seca', 'Bonecos', 'Pelúcias']
    return list


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
