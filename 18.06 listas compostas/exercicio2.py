# #01 - Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
#  No final, mostre a matriz na tela, com essa formatação:

# [  1  ][  2  ][  3  ]
# [  4  ][  5  ][  6  ]
# [  7  ][  8  ][  9  ] 

# matriz = [
# [1, 2, 3], 
# [4, 5, 6], 
# [7, 8, 9]
# ]

# #02 - Aprimore o desafio anterior, mostrando no final:
#    A) A soma de todos os valores pares digitados.
#    B) A soma dos valores da terceira coluna. 
#    C) O maior valor da segunda linha.

matriz = []

 

for l in range (3):
    linha = []
    for c in range (3):
        valor = (int(input(f'Digite o valor da {l+1} linha e da {c+1} coluna: ')))
        linha.append(valor)
    matriz.append(linha)
print('\nA matriz declarada foi:\n')
for l in matriz:
    print(f'   [ {l[0]} ]  [ {l[1]}  ]  [ {l[2]} ] ')

#modo2

matriz = []

for l in range (3):
    linha = []
    for c in range (3):
        valor = (int(input(f'Digite o valor da {l+1} linha e da {c+1} coluna: ')))
        linha.append(valor)
    matriz.append(linha)
print('\nA matriz declarada foi:\n')
for l in matriz:
    print()
    for c in l:
        print(f'  [  {c}  ]', end='')

         


