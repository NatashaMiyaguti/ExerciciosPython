# #02 - Crie um programa que vai ler vários números e colocar em uma lista. Depois
# disso, crie duas listas extras que vão conter apenas os valores pares e os valores
# ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas
# geradas.

lista = list()
par = list()
impar = list()

while True:
    numero = int (input('Digite um numero: '))
    lista.append(numero)
    sair =  str(input('Deseja continuar: [S/N]')).strip().upper()[0]
    if sair == 'N':
         break
    if numero % 2 == 0: 
        par.append(numero)
    if numero % 2 != 0:
        impar.append(numero)

print(f'''
 Minha lista é {lista}
 Minha lista par {par}
 Minha list impar {impar}
 ''')

    




