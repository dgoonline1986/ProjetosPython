class BatataClass:

    def __init__(self, qnt : int):
        self.__quantidade = qnt
        self.__lista_batatas  = []

    def add_batata_list(self, qnt):
        self.__lista_batatas.append(f'{qnt} batata adicionada')

    def loop_add_batatas(self):
        for item in range(0,self.__quantidade) :
            self.add_batata_list(item)

    def get_lista_batatas(self):
        return str(self.__lista_batatas)


teste_batata = BatataClass(5)
teste_batata.loop_add_batatas()
print(teste_batata.get_lista_batatas())