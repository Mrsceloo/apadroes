class CalcCubo:
    '''Classe que permite calcular o cubo de um número (docstring)'''
    # Comentário
    def __init__(self, valor):
        self.x = valor
        print('Objeto criado!')

    def calcula_cubo(self):
        self.cubo = self.x * self.x * self.x
        return 'Cubo calculado: ' + str(self.cubo)