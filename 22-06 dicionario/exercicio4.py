# #Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastreos (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário
# receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade
# , com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve
# contribuir por 35 anos para se aposentar



registro = dict()

registro['Nome'] = str(input('Digie seu nome: ')).title()
registro['Ano'] = int(input('Digite o ano do seu nascimento: '))
idade = 2021 - registro['Ano']
registro['idade'] = idade
registro['Carteira'] = int(input('Digite o número da sua carteira: '))
if registro['Carteira'] != 0:
    registro['Contratacao'] = int(input('Digite o ano de contratação: '))
    registro['Salario'] = float(input('Digite o valor do salario: '))
    comecou_trabalhar = registro['Contratacao']- registro['Ano']
    registro['Aposentar'] = comecou_trabalhar + 35

print (registro)