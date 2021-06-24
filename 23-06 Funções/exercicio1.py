# Faça um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições:

def voto(ano):
    idade = 2021- ano
    if idade < 16:
        return f' Com {idade} anos o voto NEGADO.'
    elif 16 <= idade >= 70:
        return f'Com a {idade} anos o voto Opcional'
    else:
        return f'Com a {idade} anos o voto OBRIGATORIO'


nasc = (int(input('Digite o ano do seu nascimento: ')))
print(voto(nasc))

