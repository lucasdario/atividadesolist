from product import Product
from category import Category
from functions import check_description, check_float, check_int, show_menu

option = 0
listproduct = []
listcategory = []
controlid_prod = 0
controlid_cate = 0

while(option != '9'):
    show_menu()
    option = input()

    if check_int(option):
        if option == '1':
            if len(listcategory) > 0:
                prod = Product()
                controlid_prod += 1
                prod.set_id(controlid_prod)

                print('Informe o nome do produto')
                prod.set_name(input())

                descriptionOk = True
                while(descriptionOk):
                    print('Informe a descrição')
                    prod.set_description(input())
                    if check_description(prod.get_description()):
                        descriptionOk = False
                    else:
                        print(
                            'Ei, sua descrição precisa conter no mínimo 20 caracteres')

                print('Informe a ID da categoria')
                tempoption = input()
                if check_int(tempoption):
                    prod.set_idCategory(int(tempoption))
                else:
                    prod.set_idCategory(0)

                print('Informe o peso do produto')
                tempweight = input()
                if check_float(tempweight, 1):
                    prod.set_weight(float(tempweight))
                else:
                    prod.set_weight(0.00)

                print('Informe a altura do produto')
                tempheight = input()
                if check_float(tempheight, 1):
                    prod.set_height(float(tempheight))
                else:
                    prod.set_height(0.00)

                print('Informe a largura do produto')
                tempwidth = input()
                if check_float(tempwidth, 1):
                    prod.set_width(float(tempwidth))
                else:
                    prod.set_width(0.00)

                print('Informe a profundidade do produto')
                tempdepth = input()
                if check_float(tempdepth, 1):
                    prod.set_depth(float(tempdepth))
                else:
                    prod.set_depth(0.00)

                print('Informe o preço')
                tempprice = input()
                if check_float(tempprice, 0):
                    prod.set_price(tempprice)
                else:
                    prod.set_price(14.00)
                    print(
                        'Preço informado é inválido, é permitido apenas preços com valor superior a R$14.\nSeu produto foi cadastrado com o valor padrão de R$14.')

                listproduct.append(
                    (prod.get_id(), prod.get_name(), prod.get_description(), prod.get_idCategory(), prod.get_weight(), prod.get_height(), prod.get_width(), prod.get_depth(), prod.get_price()))

                print('Produto cadastrado com sucesso!')
            else:
                print('Ops! Parece que você não tem nenhuma categoria cadastrada.')

        elif option == '2':
            cate = Category()
            controlid_cate += 1
            cate.set_id(controlid_cate)

            print('Informe o nome da categoria')
            cate.set_name(input())

            print('Deseja cadastrar um sub categoria? S -> SIM | N -> NÃO')
            tempoption = input()
            if tempoption == 'S' or tempoption == 's':
                print('Informe o nome da sub categoria')
                cate.set_subname(input())
            else:
                cate.set_subname('ñ cadastrada')

            listcategory.append(
                (cate.get_id(), cate.get_name(), cate.get_subname()))

        elif option == '3':
            for id, name, desc, cate, weight, height, width, depth, price in listproduct:
                desccate = ''
                subdesccate = ''
                for idcate, namecate, subnamecate in listcategory:
                    if int(idcate) == int(cate):
                        desccate = namecate
                        subdesccate = subnamecate
                    else:
                        desccate = 'Não localizada'
                        subdesccate = 'Não localizada'

                print('>>>ID:'+str(id)+'| NOME: '+name+'| DESCRIÇÃO: ' + desc+'\n| CATEGORIA: ' +
                      desccate + '| SUBCATEGORIA: '+subdesccate+'| PESO: '+str(weight)+'| ALTURA: ' +
                      str(height)+'\n| LARGURA: '+str(width) + '| PROFUNDIDADE: '+str(depth)+'| PREÇO ' + str(price)+'\n')

        elif option == '4':
            for id, name, subname in listcategory:
                print('ID:'+str(id)+'| CATEGORIA: ' +
                      name + '| SUBCATEGORIA: ' + subname)

        elif option == '5':
            prod = Product()
            print('Informe o ID do produto que deseja atualizar')
            tempid = input()

            if check_int(tempid):
                for value in listproduct:
                    if int(value[0]) == int(tempid):
                        prod.set_id(tempid)

                        print('Informe o nome do produto')
                        prod.set_name(input())

                        descriptionOk = True
                        while(descriptionOk):
                            print('Informe a descrição')
                            prod.set_description(input())
                            if check_description(prod.get_description()):
                                descriptionOk = False
                            else:
                                print(
                                    'Ei, sua descrição precisa conter no mínimo 20 caracteres')

                        print('Informe a ID da categoria')
                        tempoption = input()
                        if check_int(tempoption):
                            prod.set_idCategory(int(tempoption))
                        else:
                            prod.set_idCategory(0)

                        print('Informe o peso do produto')
                        tempweight = input()
                        if check_float(tempweight, 1):
                            prod.set_weight(float(tempweight))
                        else:
                            prod.set_weight(0.00)

                        print('Informe a altura do produto')
                        tempheight = input()
                        if check_float(tempheight, 1):
                            prod.set_height(float(tempheight))
                        else:
                            prod.set_height(0.00)

                        print('Informe a largura do produto')
                        tempwidth = input()
                        if check_float(tempwidth, 1):
                            prod.set_width(float(tempwidth))
                        else:
                            prod.set_width(0.00)

                        print('Informe a profundidade do produto')
                        tempdepth = input()
                        if check_float(tempdepth, 1):
                            prod.set_depth(float(tempdepth))
                        else:
                            prod.set_depth(0.00)

                        print('Informe o preço')
                        tempprice = input()
                        if check_float(tempprice, 0):
                            prod.set_price(tempprice)
                        else:
                            prod.set_price(14.00)
                            print(
                                'Preço informado é inválido, é permitido apenas preços com valor superior a R$14.\nSeu produto foi cadastrado com o valor padrão de R$14')

                        listproduct[int(prod.get_id())-1] = (
                            (prod.get_id(), prod.get_name(), prod.get_description(), prod.get_idCategory(), prod.get_weight(), prod.get_height(), prod.get_width(), prod.get_depth(), prod.get_price()))
                        break
                    # print('ID informado não encontrado') ###RESOLVA ISSO
            else:
                print('ID informada não é um valor valido')

        elif option == '6':
            cate = Category()
            print('Informe o ID da categoria que deseja atualizar')
            tempid = input()

            if check_int(tempid):
                for value in listcategory:
                    if int(value[0]) == int(tempid):
                        cate.set_id(tempid)

                        print('Informe o nome da categoria')
                        cate.set_name(input())

                        print('Deseja atualizar a sub categoria? S -> SIM | N -> NÃO')
                        tempoption = input()
                        if tempoption == 'S' or tempoption == 's':
                            print('Informe o nome da sub categoria')
                            cate.set_subname(input())
                        else:
                            cate.set_subname('ñ cadastrada')

                        listcategory[int(cate.get_id())-1] = (
                            (cate.get_id(), cate.get_name(), cate.get_subname()))
            else:
                print('ID informada não é um valor valido')

        elif option == '7':
            print('Informe o ID do produto que deseja deletar')
            tempdel = input()
            if check_int(tempdel):
                for value in listproduct:
                    if value[0] == int(tempdel):
                        del(listproduct[int(tempdel)-1])
            else:
                print('ID informada não é um valor valido')

        elif option == '8':
            print('Informe o ID da categoria que deseja deletar')
            tempdel = input()
            if check_int(tempdel):
                for value in listcategory:
                    if value[0] == int(tempdel):
                        del(listcategory[int(tempdel)-1])
            else:
                print('ID informada não é um valor valido')

    else:
        print('O valor digitado é inválido')
