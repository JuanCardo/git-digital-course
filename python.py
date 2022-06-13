class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocarCor(self, cor):
        self.cor = trocar
        print(f'A Cor Trocou para {cor}')

#Programa Principal
bola = Bola('Azul', '2', 'ferro')
print(bola.cor)
while True:
    resp = input('Quer trocar a cor da bola(s/n):')
    if resp == 's':
        trocar = input(f'Troque a Cor de {bola.cor} para:')
        bola.trocarCor(trocar)
    else:
        break
print(bola.cor)
