class Product:
    _id: int
    _name: str
    _description: str
    _category: str
    _price: float

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name

    def get_description(self) -> str:
        return self._description

    def set_description(self, description: str) -> None:
        self._description = description

    def get_category(self) -> str:
        return self._category

    def set_category(self, category: str) -> None:
        self._category = category

    def get_price(self) -> float:
        return self._price

    def set_price(self, price: float) -> None:
        self._price = price


option = 0
listproduct = []
controlid = 0

while(option != '5'):
    print('==========================')
    print('Escolha uma das opções abaixo:')
    print('1 - Novo cadastro de produtos')
    print('2 - Listar produtos cadastrados')
    print('3 - Atualizar um produto')
    print('4 - Deletar um produto')
    print('5 - Sair')
    print('==========================')
    print('Sua opção -> ')
    option = input()
    
    if option == '1':
        prod = Product()
        controlid += 1
        prod._id = controlid

        print('Informe o nome do produto')
        tempname = input()
        prod._name = tempname

        print('Informe a descrição')
        tempdescription = input()
        prod._description = tempdescription

        print('Informe a categoria')
        tempcategory = input()
        prod._category = tempcategory

        print('Informe o preço')
        tempprice = input()
        prod._price = tempprice

        listproduct.append(
            (prod._id, prod._name, prod._description, prod._category, prod._price))

    elif option == '2':
        for id, name, desc, cate, price in listproduct:
            print('ID:' + str(id) + '| Nome: ' + name + '| Descrição: ' +
                  desc + '| Categoria: ' + cate + '| Preço ' + str(price))

    elif option == '3':
        print('Informe o ID do produto que deseja atualizar')
        tempupdate = input()

        print('Informe o nome do produto')
        tempname = input()
        prod._name = tempname

        print('Informe a descrição')
        tempdescription = input()
        prod._description = tempdescription

        print('Informe a categoria')
        tempcategory = input()
        prod._category = tempcategory

        print('Informe o preço')
        tempprice = input()
        prod._price = tempprice

        listproduct[int(tempupdate)-1] = (
            (prod._id, prod._name, prod._description, prod._category, prod._price))

    elif option == '4':
        print('Informe o ID do produto que deseja deletar')
        tempdel = input()
        del(listproduct[int(tempdel)-1])
