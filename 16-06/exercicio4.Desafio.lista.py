# Desafio da noite:
# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".

lista = list()

pergunta1 = str(input('Você telefonou para a vítima [S/N]? ')).strip().upper()[0]
pergunta2 = str(input('Você esteve no local do crime[S/N]? ')).strip().upper()[0]
pergunta3 = str(input('Você mora perto da vítima [S/N]? ')).strip().upper()[0]
pergunta4 = str(input('Você devia para a vítima [S/N]? ')).strip().upper()[0]
pergunta5 = str(input('Você já trabalhou com a vítima [S/N]?')).strip().upper()[0]

lista.append(pergunta1)
lista.append(pergunta2)
lista.append(pergunta3)
lista.append(pergunta4)
lista.append(pergunta5)

conta = lista.count('S')

if conta == 2:
  print ('"Você é Suspeito"')

elif conta == 3 or conta == 4:
  print ('"Você é Cúmplice"')

elif conta == 5:
  print ('"Você é o Assassino"')

else:
  print ('"Você é inocente"')


