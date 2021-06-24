# Faça um programa em Python com uma função que necessite de três parametros, e que forneça:
# A soma desses três parametros através de uma função.
# Seu script também deve fornecer a média dos três números,  através de uma segunda função que chama a primeira.

def soma (n1, n2, n3):
    total = n1 + n2 + n3
    return total

def media (n1,n2,n3):
    media = soma(n1,n2,n3) /3
    return media 

numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite um numero: '))
numero3 = int(input('Digite um numero: '))

print (f' A soma dos numeros : {numero1}, {numero2}, {numero3} é igual a {soma(numero1,numero2,numero3)}\n E a média é {media(numero1,numero2,numero3)}')

### OUTRA FORMA DE FAZER###

def soma (n1, n2, n3):
    total = n1 + n2 + n3
    return total

def media(soma):
    media = soma /3
    return media 

def menu():
    numero1 = int(input('Digite um numero: '))
    numero2 = int(input('Digite um numero: '))
    numero3 = int(input('Digite um numero: '))
    somar = soma(numero1,numero2,numero3)
    print(media(somar))