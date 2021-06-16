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

while operacao > 5 or operacao < 1:
    print('Operação inválida')
    operacao = int(input('Digite o numero da operação que deseja fazer: '))

if operacao == 1: 
     conta = valor1 + valor2
 
 
