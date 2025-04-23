x = float(input('Digite o primeiro lado do triangulo: '))
y = float(input('Digite o segundo lado do triangulo: '))
z = float(input('Digite o terceiro lado do triangulo: '))

if x == y == z:
    print('O triangulo é equilátero')
elif x != y != z:
    print('O triangulo é escaleno')
else:
    print('O triangulo é Isósceles')