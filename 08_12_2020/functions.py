def show_menu():
    return print('==========================\nEscolha uma das opções abaixo:\n'
                 + '1 - Novo cadastro de produtos\n2 - Novo cadastro de categorias\n'
                 + '3 - Listar produtos cadastrados\n4 - Listar categorias cadastradas\n'
                 + '5 - Atualizar um produto\n6 - Atualizar uma categoria\n'
                 + '7 - Deletar um produto\n8 - Deletar uma categoria\n'
                 + '9 - Sair\n'
                 + '==========================\nSua opção ->')


def check_int(var):
    try:
        int(var)
    except ValueError:
        return False
    return True


def check_float(var, noprice):
    try:
        if int(noprice) == 1:
            float(var)
        else:
            float(var)
            if float(var) >= 14:
                return True
            else:
                return False
    except ValueError:
        return False
    return True


def check_description(var):
    if len(var) >= 20:
        return True
    else:
        return False
