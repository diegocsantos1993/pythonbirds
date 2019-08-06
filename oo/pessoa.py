class pessoa:
    def __init__(self, nome=None, idade=35):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return "Ola"

if __name__ == '__main__':

    p = pessoa("Fernando")
    print(p.cumprimentar())
    print(p.nome)
    p.nome = "Diego"
    print(p.nome)
    print(p.idade)