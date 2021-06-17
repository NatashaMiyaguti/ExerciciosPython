# 01 - Crie um programa que vai gerar cinco números aleatórios de 1 a 50 e colocar em uma  tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla. Sem utilizar repetições.
# Dica: utilizar a biblioteca random do Python.

from random import randint
numero1 = randint (1,50)
numero2 = randint (1,50)
numero3 = randint (1,50)
numero4 = randint (1,50)
numero5 = randint (1,50)

tupla = (numero1, numero2, numero3,numero4,numero5)

ordemtupla = sorted(tupla)
conta = len(tupla)
maior = ordemtupla[conta -1]
menor = ordemtupla [0]

print (f''' {tupla}
O maior numero é: {maior}
O menor numero é: {menor}

''')