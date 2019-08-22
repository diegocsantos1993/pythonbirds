
class Carro:
    def __init__(self, direcao,Motor):
        self.Motor = Motor
        self.direcao = direcao

    def calcular_a_velocidade(self):
        return self.Motor.velocidade()

    def acelerar(self):
        return self.Motor.acelerar()

    def frear(self):
        return self.Motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor()

    def girar_a_direita(self):
        self.direcao.rotacao_a_direita_dct()

    def girar_a_esquerda(self):
        self.direcao.rotacao_a_esquerda_dct_dct()








NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'

class direcao:
    rotacao_a_direita_dct={
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE
    }

    rotacao_a_esquerda_dct = {
        NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL
    }
    def __init__(self):

     def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]

     def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]


class Motor():
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade +=1

    def frear(self):
        self.velocidade -=1
        self.velocidade = max(0, self.velocidade)


