# #01 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi
# o maior e o menor peso lidos.

maior = 0
menor = 1000
for c in range (0,5):#44, 33
    peso = float(input('Digite seu peso: '))
    if maior < peso:
        maior = peso
    if menor > peso:
        menor = peso

print (f' O maior peso é {maior}, e o menor peso é {menor}')
