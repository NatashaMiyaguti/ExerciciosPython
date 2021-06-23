#Faça um programa que leia nome e média de um aluno, guardando também a situação
# em um dicionário. No final, mostre o conteúdo da estrutura na tela. A média para
# aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é
# reprovado.

aluno = dict()
aluno ['nome'] = str(input('nome: ')).title()
aluno ['média'] = float(input(f'média do(a) aluno {aluno["nome"]}:'))

if aluno['média'] >= 7:
    aluno['situacao'] = 'aprovado'
elif aluno['média'] >=5 and aluno['média'] < 7:
    aluno['situacao'] = 'recuperação'
else :
    aluno['situacao'] ='reprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')



    