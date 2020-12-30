import datetime as datetime


def createfile() -> None:
    root = 'files/'
    file = open(f'{root}list_marketplace.txt', 'w')
    file.write('Casas Bahia;Ponto Frio;Extra;Mercado Libre;Americanas')
    #file.write('0,Casas Bahia;1,Ponto Frio')
    file.close()
    file = open(f'{root}list_category.txt', 'w')
    file.write(
        'Eletrônicos;Eletrodomésticos;Brinquedos;Móveis;Informática;Telefonia;Serviços;Ofertas TV;Áudio;Bebês')
    # file.write('0,Eletrônicos;1,Eletrodomésticos;2,Móveis;3,Informática;')
    file.close()
    file = open(f'{root}list_subcategory.txt', 'w')
    file.write(
        'Smartphone;PC;Notebook;Sofá;Geladeira;Freezer;Lava e Seca;Bonecos;Pelúcias;Cama;Impressora;HD Externo;PenDrive;Carrinho de bebê;Chupeta;Fraldas')
    # file.write('1,Smartphone;2,PC;3,Notebook;4,Mesa')
    file.close()

    file = open(f'{root}list_general.txt', 'w')
    file.write('0,0,1;1,3,2;0,2,4')
    file.close()


def readfiles(type: int) -> list:
    root = 'files/'
    file = ''
    clean_list = []
    clean_line = []
    if type == 0:
        file = open(f'{root}list_marketplace.txt', 'r')
    elif type == 1:
        file = open(f'{root}list_category.txt', 'r')
    elif type == 2:
        file = open(f'{root}list_subcategory.txt', 'r')
    elif type == 3:
        file = open(f'{root}list_general.txt', 'r')

    if file:
        for line in file:
            line = line.strip()
            clean_line = line.split(';')

        file.close()

        for value in clean_line:
            clean_list.append(value)

    return clean_list


def writefiles(value: str, type: int) -> bool:
    root = 'files/'
    file = ''
    if type == 0:
        file = open(f'{root}list_marketplace.txt', 'a')
    elif type == 1:
        file = open(f'{root}list_category.txt', 'a')
    elif type == 2:
        file = open(f'{root}list_subcategory.txt', 'a')
    try:
        file.write(';'+str(value))
        return True
    except Exception as e:
        return False
    finally:
        file.close()


def log(function_name: str):
    root = 'files/'
    file = open(f'{root}log.txt', 'a')
    data = datetime.datetime.now()
    file.write(data.strftime(
        f"%d/%m/%Y às %H:%M:%S => Acesso a função {function_name}\n"))
    file.close()
