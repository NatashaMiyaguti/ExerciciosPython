#01 - Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já esteja lá dentro, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
# crescente.

numeros = list()
while True:
    num = int(input('Digite um valor: '))
    if num not in numeros:
        numeros.append(num)

    resp = input ('Você quer continuar?[S/N] ').strip().upper()[0]
    if resp == 'N':
        break
numeros.sort()
print(f' A lista ordenada é: {numeros}')
