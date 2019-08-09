class pessoa:
    def __init__(self, *filhos,nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return "Ola"

if __name__ == '__main__':

    dainaria = pessoa(nome="Day")
    diego = pessoa(dainaria, nome="Diego")
    print(dainaria.cumprimentar())
    print(diego.nome)
    print(dainaria.nome)
    print(diego.idade)
    print(diego.filhos)
    for filhos in diego.filhos:
        print(filhos.nome)
    diego.sobrenome = "Costa"
    del (diego.filhos)
    print(diego.sobrenome)
    print(diego.__dict__)
    print(dainaria.__dict__)
