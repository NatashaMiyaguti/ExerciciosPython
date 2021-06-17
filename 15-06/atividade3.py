# #03 - Crie um programa que leia o nome e o preço de vários produtos. O programa
# deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# (C) Qual é o nome do produto mais barato.


valor_total = valor_alto = 0
produto_barato = 100000
nome_barato = ''

while True:
    produto = str(input('Digite o produto: '))
    valor = float(input('Digite o valor do produto : '))
    valor_total = valor_total + valor
    if valor > 1000:
        valor_alto += 1
    if valor < produto_barato: 
        nome_barato = produto 
        produto_barato = valor

    continuar = str(input('Deseja continuar [S/N]: ')). upper().strip()[0]
    if continuar == ('N'):
            break


print(f'''
O valor total de gastos é R$ {valor_total}
{valor_alto} produtos custam mais que R$1000,00
O produto mais barato é: {nome_barato}
''')
    
