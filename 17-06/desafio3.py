# Desafio: Faça um programa que ajude um jogador da MEGA SENA a criar
# palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import sample
lista = list()


jogos = int(input('Quantos jogos você deseja fazer: '))
for conta in range (jogos):

    nu = sample(range(1, 60) , 6)
    lista.append(nu)


print(lista)

