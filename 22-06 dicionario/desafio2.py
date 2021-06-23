# # Desafio: Continuando o exercício 3 crie agora um boletim escolar, seu programa deve receber 5 notas de 15 alunos, assim como o nome desses alunos, o programa tem que
# calcular a média desse aluno e mostrar a situação dele, seguindo os mesmos critérios
# apresentados no exercício 3. No final apresente todos nomes, as 5 notas, as médias e as
# situações dos 15 alunos de uma vez só

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
