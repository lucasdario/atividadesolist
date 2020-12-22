from function import *

menu = True
while menu:
    show_menu()
    option = input("=>")
    if check_int(option):
        if int(option) == 1:
            number_one_ = input("Informe o 1° valor para soma:\n=>")
            number_two_ = input("Informe o 2° valor para soma:\n=>")
            sum(number_one_, number_two_)
        elif int(option) == 2:
            number_one_ = input("Informe o 1° valor para subtração:\n=>")
            number_two_ = input("Informe o 2° valor para subtração:\n=>")
            subtract(number_one_, number_two_)
        elif int(option) == 3:
            number_one_ = input("Informe o 1° valor para multiplicação:\n=>")
            number_two_ = input("Informe o 2° valor para multiplicação:\n=>")
            multiply(number_one_, number_two_)
        elif int(option) == 4:
            number_one_ = input("Informe o 1° valor para divisão:\n=>")
            number_two_ = input("Informe o 2° valor para divisão:\n=>")
            division(number_one_, number_two_)
        else:
            menu = False
    else:
        print_info("Valor informado é inválido! Tente novamente.")
