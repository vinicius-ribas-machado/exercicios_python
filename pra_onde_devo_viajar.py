#bibliotecas
import random

#qual clima vc prefere?
print('Vamos começar sua viagem!')
idioma = int(input('''Tem preferencia de idioma?
 [1]Ingles
 [2]Espanhol
 [3]Portugues
Qual: '''))

clima = int(input('''Tem preferencia de clima para o pais?
 [1]Frio
 [2]Quente
Qual: '''))
print()

paises_frio_ingles = ('Canadá')
paises_frio_espanhol = ('Argentina')
paises_frio_portugues = ('Sul do Brasil')

paises_quente_ingles = ('Austrália')
paises_quente_espanhol = ('Mexico')
paises_quente_portugues = ('Moçambique')


if idioma == 1:
    if clima == 1:
        print('Voce pode ir para,  {}, otimo lugar'.format(paises_frio_ingles))
    elif clima == 2:
        print('Voce pode ir para,  {}, otimo lugar'.format(paises_quente_ingles))

if idioma == 2:
    if clima == 1:
        print('Voce pode ir para,  {}, otimo lugar'.format(paises_frio_espanhol))
    elif clima == 2:
        print('Voce pode ir para,  {}, otimo lugar'.format(paises_quente_espanhol))

if idioma == 3:
    if clima == 1:
        print('Voce pode ir para,  {}, otimo lugar'.format(paises_frio_portugues))
    elif clima == 2:
        print('Voce pode ir para,  {}, otimo lugar'.format(paises_quente_portugues))

