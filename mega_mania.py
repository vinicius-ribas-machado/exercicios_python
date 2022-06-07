# criar a base do programa q simule a mega mania

# bibliotecas:
import time
from random import randint

# numeros aleatorios
num1 =randint(1,6)
num2 =randint(1,6)
num3 =randint(1,6)

pc1 =randint(1,6)
pc2 =randint(1,6)
pc3 =randint(1,6)

# numeros q vc vai receber
print('=-'*7,'MEGA MANIA','=-'*8)
print('Você ganhou esses numeros da sorte: {} {} {}'.format(num1, num2, num3))
print('=-'*21)

#jogada do bot
print()
print('sorteando numeros...')
time.sleep(3)

#numeros da maquina
print('os numeros sorteados foram {} {} {}'.format(pc1, pc2, pc3))
print()

# variavel de vitoria ou derrota
if num1 == pc1 and num2 ==pc2 and num3 ==pc3:
    print('VC GANHOUUUUUUUUUUUUU!!!!!!!!!!!!' )
else:
    print('Mais sorte da proxima vez!')
