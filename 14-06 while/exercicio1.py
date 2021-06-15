# 01 - Faça um programa que leia o sexo biológico de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
#  Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = 'FM'
pergunta = str(input('Digite seu sexo biólogico: ')).upper().strip()[0]

while pergunta not in sexo:
  print('Sexo inválido')
  pergunta = str(input('Digite seu sexo biólogico: ')).upper().strip()[0]
print (f' Seu sexo é {pergunta}')