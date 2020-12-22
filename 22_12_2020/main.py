from functions import *

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
        if int(option) == 0:
            menu = False
    else:
        print_info("Valor informado é inválido!Tente novamente.")
