# 01 - Dada a lista l = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
# a) tamanho da lista.
# b) maior valor da lista.
# c) menor valor da lista.
# d) soma de todos os elementos da lista.
# e) lista em ordem crescente.
# f) lista em ordem decrescente.

lista1 = [5, 7, 2, 9, 4, 1, 3]
print (f'O tamanho da lista é:(len(lista1)')
maior = max(lista1)
print (f'O maior valor é: {maior}')
menor = min(lista1)
print (f'O menor valor é: {menor}')
soma = sum (lista1)
print (f'A soma da lista é: {soma}')
lista1.sort()
print (f'Crescente: {lista1}')
lista1.reverse()
print (f'Decresecente: {lista1}')