# signos

# input dos dados do usuario
dia = int(input('que dia voce nasceu? '))
mes = str(input('em q mes vc nasceu? '))

# evitar falhas, transforma o texto em maiúsculo, evitando erros de digitaçap
dados = ('{}'.format(mes.upper()))

# uma tabela de IF pra ver o mes e o dia
if dados == 'DEZEMBRO':
    if dia <= 21:
        print('Sagitário')
    elif dia <= 31:
        print('Capricórnio')

if dados == 'JANEIRO':
    if dia <= 19:
        print('Capricórnio')
    elif dia <= 31:
        print('Aquário ')

if dados == 'FEVEREIRO':
    if dia <= 18:
        print('Aquário')
    elif dia <= 29:
        print('Peixe')

if dados == 'MARÇO':
    if dia <= 20:
        print('Peixe')
    elif dia <= 31:
        print('Áries')

if dados == 'ABRIL':
    if dia <= 19:
        print('Áries')
    elif dia <= 30:
        print('Touro')

if dados == 'MAIO':
    if dia <= 20:
        print('Touro')
    elif dia <= 31:
        print('Gêmeos')

if dados == 'JUNHO':
    if dia <= 20:
        print('Gêmeos')
    elif dia <= 30:
        print('Câncer')

if dados == 'JULHO':
    if dia <=22:
        print('Câncer')
    elif dia <= 31:
        print('Leão')

if dados == 'AGOSTO':
    if dia <= 22:
        print('Leão')
    elif dia <= 31:
        print('Virgem ')

if dados == 'SETEMBRO':
    if dia <= 22:
        print('Virgem')
    elif dia <= 30:
        print('Libra ')

if dados == 'OUTUBRO':
    if dia <= 22:
        print('Libra')
    elif dia <= 31:
        print('Escorpião')

if dados == 'NOVEMBRO':
    if dia <= 22:
        print('Escorpião')
    elif dia <= 30:
        print('Sagitário ')

