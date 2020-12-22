import textwrap as tw


def show_menu():
    print(tw.dedent('''
                    #######################
                    ######CALCULADORA######
                    #######################
                    #             
                    Escolha uma das opções abaixo:
                    1 - Soma
                    2 - Subtração
                    3 - Multiplicação
                    4 - Divisão
                    0 - Sair
    '''))


def sum(number_one: float, number_two: float) -> float:
    if check_float(number_one) and check_float(number_two):
        result = float(number_one)+float(number_two)
        # return print_info(f"Seu resultado é: {result:.2f}")
        return result
    else:
        print_info("Valor informado é inválido")


def subtract(number_one: float, number_two: float) -> float:
    if check_float(number_one) and check_float(number_two):
        result = float(number_one)-float(number_two)
        # return print_info(f"Seu resultado é: {result:.2f}")
        return result
    else:
        print_info("Valor informado é inválido")


def multiply(number_one: float, number_two: float) -> float:
    if check_float(number_one) and check_float(number_two):
        result = float(number_one)*float(number_two)
        # return print_info(f"Seu resultado é: {result:.2f}")
        return result
    else:
        print_info("Valor informado é inválido")


def division(number_one: float, number_two: float) -> float:
    if check_float(number_one) and check_float(number_two):
        if check_value_zero(number_one) and check_value_zero(number_two):
            result = float(number_one)/float(number_two)
            # return print_info(f"Seu resultado é: {result:.2f}")
            return result
        else:
            print_info("Divisão por 0 não é válida!Tente novamente.")
    else:
        print_info("Valor informado é inválido")


def check_float_(number: float) -> bool:
    if isinstance(number, float):
        return True
    raise ValueError(f"O valor {number} não é válido!\nTente novamente.")


def check_float(var):
    try:
        float(var)
    except ValueError:
        return False
    return True


def check_int(var):
    try:
        int(var)
    except ValueError:
        return False
    return True


def check_value_zero(number: float) -> bool:
    if float(number) != 0:
        return True


def print_info(message: str):
    print(f'''
#######################
{message}
#######################
    ''')
