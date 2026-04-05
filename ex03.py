# Implemente um programa em Python para ler do teclado números. Caso o usuário forneça um número igual a -1, o programa deve fornecer a média dos números e encerrar;
soma = 0
quantidade = 0
numero = float(input("Digite um número (-1 para encerrar): "))
while numero != -1:
    soma += numero
    quantidade += 1
    numero = float(input("Digite um número (-1 para encerrar): "))
if quantidade > 0:
    media = soma / quantidade
    print("Média dos números: {}".format(media))
else:
    print("Nenhum número válido foi digitado.")