velo = int(input('qual velocidade vc estava? '))

valor =(velo - 80)*7

if velo > 80:
    print('vc deve pagar a multa de {}'.format(valor))
elif velo < 80:
    print('vc nao precisa pagar nd')

