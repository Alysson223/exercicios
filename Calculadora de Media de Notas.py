notas = []
soma = 0
while True:
    nota = float(input("Digite a nota do aluno (digite -1 para encerrar): "))
    if nota == -1:
        break
    notas.append(nota)

for x in notas:
    soma += x

if len(notas) > 0:
    media = soma / len(notas)
    print(f'Notas: {notas}, Media: {media}')
else:
    print('Nenhuma nota no sistema')