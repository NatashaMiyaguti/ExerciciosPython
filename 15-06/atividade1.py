# #01 - Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso. (utilizar while
# sem break)

conta = 0
valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite o segundo valor: '))

print ('''
 [ 1 ] somar
 [ 2 ] multiplicar
 [ 3 ] maior
 [ 4 ] novos números
 [ 5 ] sair do programa
''')

operacao = int(input('Digite o numero da operação que deseja fazer: '))

while operacao != 5:

    while operacao > 5 or operacao < 1:
        print('Operação inválida')
        operacao = int(input('Digite o numero da operação que deseja fazer: '))

    if operacao == 1: 
        conta = valor1 + valor2
        print (f'A soma do {valor1} com o {valor2} é: {conta}')
    elif operacao == 2: 
        conta = valor1 * valor2
        print (f'A multiplicação do {valor1} com o {valor2} é:  {conta}')
    elif operacao == 3: 
        if valor1 > valor2:
            print (f' O maior valor entre {valor1} e {valor2} é: {valor1}')
        else:
            print(f' O maior valor entre {valor1} e {valor2} é:  {valor2}')
    elif operacao == 4:
        valor1 = int(input('Digite um valor: '))
        valor2 = int(input('Digite o segundo valor: '))

    print ('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    ''')

    operacao = int(input('Digite o numero da operação que deseja fazer: '))

     
        

        
     


 
 
