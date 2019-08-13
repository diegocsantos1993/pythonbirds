class pessoa:
    olhos = "2"

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
    diego.olhos = "3"
    del (diego.olhos)
    del (diego.filhos)
    print(diego.sobrenome)
    print(diego.__dict__)
    print(dainaria.__dict__)
    print(diego.olhos)
    print(dainaria.olhos)
    print(pessoa.olhos)
    print(id(diego.olhos), id(dainaria.olhos), id (pessoa.olhos))