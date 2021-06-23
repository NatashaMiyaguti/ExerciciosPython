# Desafio: Faça um programa que ajude um jogador da MEGA SENA a criar
# palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

# from random import sample
# lista = list()


# jogos = int(input('Quantos jogos você deseja fazer: '))
# for conta in range (jogos):

#     nu = sample(range(1, 60) , 6)
#     lista.append(nu)


# print(lista)

from random import randint

jogos = list()
numeroJogos = int(input('\n\nQTD Jogos: '))

for l in range(numeroJogos):
    cont = 0
    jogo = list()
    while True:
        numero = randint(1,60)
        if numero not in jogo:
            jogo.append(numero)
            cont += 1
        if cont == 6:
            break
    
    jogo.sort()
    jogos.append(jogo)

print(f'''\n\n
Seus número da sorte (ou não) são...
------------------------------------
''')
for (i, v) in enumerate(jogos):
    print('{} Jogo: {}'.format(i+1, v))