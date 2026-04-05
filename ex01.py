# Implemente um programa em Python para ler do teclado a nota de um aluno. Verifique se o valor lido é uma nota válida (entre 0 e 10). Se não for, ler este valor até que a mesma seja válida;
s = int(input('Digite sua nota: '))
while s > 10 or s < 0:
    print('Inválido, tente novamente.')
    s = int(input('Digite sua nota novamente: '))
print('Válido.')