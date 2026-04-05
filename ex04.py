# Escreva um programa que receba 10 números do teclado e exiba a quantidade de números pares e ímpares lidos.
contador = 0
par = 0
impar = 0
while contador < 10:
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1
    contador += 1
print("Quantidade de números pares: {}".format(par))
print("Quantidade de números ímpares: {}".format(impar))