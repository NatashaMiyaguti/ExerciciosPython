# #02 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada
# pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não
# continuar. No final, mostre:
# A) Quantas pessoas têm mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres têm menos de 20 anos.

ano = 2021
maior = mulher20 = 0
feminino = 0
masculino = 0

while True:
    sexo = str(input('Qual seu sexo biológico [F/M]: ')).strip().upper()[0]
    if sexo == 'F':
         feminino += 1
    else:
         masculino += 1
    nascimento = int(input('Digite o ano do seu nascimento: '))
    if ano - nascimento  > 18:
        maior += 1
    if ano - nascimento < 20 and sexo == 'F':
        mulher20 +=1

    pergunta = str(input(' Você deseja continuar {[S/N]: ')).strip().upper()[0]
    if pergunta == 'N':
        break
    
print (f'''
{maior} pessoas têm mais de 18 anos.
{masculino} homens foram cadastrados.
{mulher20} mulheres têm menos de 20 anos.
''')
  
