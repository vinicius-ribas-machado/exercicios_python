n1 = float(input('qual o primeiro  numero? '))
n2 = input('qual operaçao? ')
n3 = float(input('qual o segundo numero? '))

if n2 == '+':
    print(n1+n3)
elif n2 == '-':
    print(n1-n3)
elif  n2 == '*':
    print(n1*n3)
elif  n2 == '/':
    print(n1/n3)

else:
    print()
    print('''Operações invalida tente:
[+] multiplicação
[-] subtração 
[*] multiplicação 
[/] divisao''')
