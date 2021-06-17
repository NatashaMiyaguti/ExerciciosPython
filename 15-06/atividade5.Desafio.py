# #05 (DESAFIO) Em uma eleição presidencial existem quatro candidatos. Os votos
# são informados por meio de código.
# Os códigos utilizados são:
# 1 , 2, 3 - Votos para os respectivos candidatos
# (você deve montar a tabela ex: 1 - José / 2- João / etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos

soma = 0

voto1 = 0
voto2 = 0
voto3 = 0
voto4 = 0
voto5 = 0
voto6 = 0

print ('''
    [ 1 ] José
    [ 2 ] João
    [ 3 ] Maria
    [ 4 ] Ana
    [ 5 ] Nulo
    [ 6 ] Branco
    [ 7 ] Break
    ''')

while True:
    votacao = int(input('Vote no seu cantidado: '))
    if votacao == 1:
        voto1 +=1
    elif votacao == 2:
        voto2 +=1
    elif votacao == 3:
        voto3 +=1
    elif votacao == 4:
        voto4 +=1
    elif votacao == 5:
        voto5 +=1
    elif votacao == 6:
        voto6 += 1
    else:
        break

soma = voto1 + voto2 + voto3 + voto4 + voto5 + voto6 
porcentagem_nulos = voto5 / soma * 100
porcentagem_branco = voto6 /soma * 100

print(f'''
Candidato 1 : {voto1} votos.
Candidato 2 : {voto2} votos.
Candidato 3 : {voto3} votos.
Candidato 4 : {voto4} votos.
O total de votos nulos é: {voto5}
O total de votos em branco é: {voto6}
A percentagem de votos nulos sobre o total de votos é: {porcentagem_nulos:.2f}%
A percentagem de votos em branco sobre o total de votos é: {porcentagem_branco:.2f}%

''')

    




