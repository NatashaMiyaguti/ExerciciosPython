# #03 - Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são
# maiores.

ano= 2021
maior = menor = 0

for a in range (0,7):
    nascimento = int(input('Qual o ano do seu nascimento: '))
    if ano - nascimento  > 18:
        maior += 1
    if  ano - nascimento < 18:
        menor += 1

print (f'{maior} atingiram a maioridade, e {menor} não atingiram a maioridade')
