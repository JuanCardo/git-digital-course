class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocarCor(self, cor):
        self.cor = trocar

    def mostrarCor(self, cor):
        print(f'A Cor da Bola é {cor}')

#Programa Principal
bola = Bola('Azul', '2', 'ferro')

while True:
    resp = input('Quer trocar a cor da bola(s/n):')
    if resp == 's':
        trocar = input(f'Troque a Cor de {bola.cor} para:')
        bola.trocarCor(trocar)
        continue
    else:
        resp = input('Mostrar a Cor da bola(s/n):')
        if resp == 's':
            bola.mostrarCor(bola.cor)
        break
