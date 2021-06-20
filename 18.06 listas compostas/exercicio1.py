# Crie uma lista composta que recebe 5 nomes e 5 idades de clientes, utilizando o for e o if,
#  verifique quais clientes são maiores de idade e quais são menores de idade e mostre na tela a
#  seguinte frase para cada um deles: 'Fulano é maior de idade' ou 'Fulana é menor de idade' e  
# também quantos são maiores e quantos são menores de idade.

maior = menor = 0
lista =[]

for p in (5):
    nome = input('Digite o {p+1}° nome:').capitalise() #para colocar a primeira letra em maiuscula
    idade = int(input('Digite a idade do(a) {nome}: '))
    lista.append([nome, idade])

    if p[1] >= 18:
        maior += 1 
        print(f' {p[0]} é maior')
    else:
        menor += 1
        print (f'{p[0]} é de menor')

for p in lista:
        if p[1] >= 18:
            print(f'{p}[0] é maior de idade.')
            maior += 1
        else:
            print(f'{p[0]} é menor de idade.')
            menor +=1 

print (f'\n{maior} pessoas são maiores, e {menor} pessoas são menores de idade')