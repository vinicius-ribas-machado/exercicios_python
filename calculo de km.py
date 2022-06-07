#crie um projeto q faça o preço de ter alugado o carro

# Um Carros que, em média fazem pelo menos 8 km/l...
# Custa 60 reais o dia...

carro = int(input('quantos km vc foi sua viagem? '))
dia = int(input('por quantos dias vc alugou o carro? '))

print('O valor final ficou em ${}'.format((dia*60)+(carro*8)))
