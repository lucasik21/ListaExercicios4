# Implemente um programa em Python para imprimir na tela o somatório dos N primeiros números inteiros a partir do 1. Sendo N lido do teclado
n = int(input('Digite a quantidade de números que quer somar: '))
if n < 1:
    n = int(input('Digite novamente: '))
total = 0
for i in range(1, n + 1):
    total += i
print('A soma destes números deu {}'.format(total))