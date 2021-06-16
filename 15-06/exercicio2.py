#  #02 - Crie um programa que pergunte ao usuário um número inteiro e faça a
# tabuada desse número.

numero = int(input('Qual tabuada você quer fazer? '))
for t in range (1,11):
    print(f'{t} x {numero} = {t*numero}')