# #04 - Desenvolva um programa que leia seis números inteiros e mostre a soma
# apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
# Mostre também quantos valores pares foram digitados.

par =  0
soma = 0

for c in range (0,6):
    numeros = int(input('Digite um número: '))
    if numeros % 2 == 0:
        par += 1
        soma = soma + numeros
   


print (f'Foram digitados {par} pares, e a soma deles é {soma}')
