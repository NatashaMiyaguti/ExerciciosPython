# #04 (DESAFIO) Crie um jogo onde o computador vai “pensar” em um número entre
# 0 e 10. O jogador vai tentar adivinhar qual número foi escolhido até acertar, entre os
# palpites diga ao jogador se o número do computador é maior ou menor ao que ele
# digitou,no final mostre quantos palpites foram necessários para vencer.

from random import randint

numero = randint(0,10)

adivinha = int(input('Digite um numero [0/10]: '))
conta= 0

while adivinha != numero:
    conta += 1

    if adivinha < numero:
        print ('Mais... Tente novamente')
        adivinha = int(input('Digite um numero [0/10]: '))
    elif    adivinha > numero:
        print ('Menos... Tente novamente')
        adivinha = int(input('Digite um numero [0/10]: '))
    
print(f' Você acretou. Em {conta} palpites')



