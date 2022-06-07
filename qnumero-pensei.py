from random import randint
from time import sleep

pc = randint(1,5)
print('-='*20)
print('VAMOS JOGAR UM JOGO, EM Q NUMERO PENSEI?')
print('-='*20)
sleep(1)

jogador = int(input('Escolha um numero ae entre 1 e 5: '))
print ('processando...')
sleep(1)

if jogador == pc:
    print("vc realmente é bom nisso, eu pensei em {}".format(pc))
else:
    print('Mais sorte da proxima, eu pensei em {}'.format(pc))
###