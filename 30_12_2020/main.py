from functions import *

boot()
menu = True
while menu:
    show_menu()
    option = input("=>")
    if check_int(option):
        if int(option) == 1:
            list = list_martkeplaces()
            print_info('Lista de Marketplaces')
            for i in list:
                print(f'=>{i}\n')
        if int(option) == 2:
            list = list_category()
            print_info('Lista de Categorias')
            for i in list:
                print(f'=>{i}\n')
        if int(option) == 3:
            list = list_sub_category()
            print_info('Lista de SubCategorias')
            for i in list:
                print(f'=>{i}\n')
        if int(option) == 4:
            name_ = input('Insira o nome do Marketplace:\n=>')
            if add_marketplace(name_):
                print_info('Marketplace cadastrado com sucesso')
            else:
                print_info(
                    'Tivemos um problema aqui,\ntente novamente mais tarde')
        if int(option) == 5:
            name_ = input('Insira o nome da Categoria:\n=>')
            if add_category(name_):
                print_info('Categoria cadastrado com sucesso')
            else:
                print_info(
                    'Tivemos um problema aqui,\ntente novamente mais tarde')
        if int(option) == 6:
            name_ = input('Insira o nome do Sub Categoria:\n=>')
            if add_subcategory(name_):
                print_info('Sub Categoria cadastrado com sucesso')
            else:
                print_info(
                    'Tivemos um problema aqui,\ntente novamente mais tarde')
        if int(option) == 0:
            menu = False
    else:
        print_info("Valor informado é inválido!Tente novamente.")
