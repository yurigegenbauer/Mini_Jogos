import random

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def Iniciar(self):
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()
        try:
            while self.tentar_novamente == True:
                if int(self.valor_do_chute) > self.valor_aleatorio:
                    print('Escolha um número mais baixo!')
                    self.PedirValorAleatorio()
                elif int(self.valor_do_chute) < self.valor_aleatorio:
                    print('Escolha um número mais alto!')
                    self.PedirValorAleatorio()
                if int(self.valor_do_chute) == self.valor_aleatorio:
                    self.tentar_novamente = False
                    print('Boa, acertou!')
        except:
            print('FAVOR DIGITAR APENAS NÚMEROS :)')
            self.Iniciar()


    def PedirValorAleatorio(self):
        self.valor_do_chute = input('Escolha um número de 0 a 100: ')

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo,self.valor_maximo)

chute = ChuteONumero()
chute.Iniciar()






'''


FOI USANDO WHILE PRA FICAR FALANDO PARA CHUTAR UM NUMERO INFINITAMENTE
ATÉ ACERTAR O VALOR


'''