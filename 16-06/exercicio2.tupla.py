# 02 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.

valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
valor3 = int(input('Digite o terceiro valor: '))
valor4 = int(input('Digite o quarto valor: '))

tupla = (valor1, valor2, valor3,valor4)

print (f'''O valor 9 apareceu {tupla.count(9)} vezes.
E o primeiro valor 3 foi digitado na posição: {tupla.index(3)}

''')
