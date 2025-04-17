notas = []
soma = 0
while True:
    nota = float(input("Digite a nota do aluno (digite -1 para encerrar): "))
    if nota == -1:
        break
    elif 0 <= nota <=10:
        notas.append(nota)
    else:
        print(f'O valor {nota} é invalido.')

for x in notas:
    soma += x

if len(notas) > 0:
    media = soma / len(notas)
    print(f'Notas: {notas}, Media: {media}')
else:
    print('Nenhuma nota no sistema')
