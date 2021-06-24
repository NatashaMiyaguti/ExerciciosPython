#Faça um programa, com uma função que necessite de um parametro. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def positivo_negativo(n1):
    if n1 >= 1:
        return f' O numero {n1} é positivo'
    else:
        return f' O numero {n1} é negativo'

numero = int(input('Digite um numero: '))
print(positivo_negativo(numero))

