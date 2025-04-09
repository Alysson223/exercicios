numero = int(input('Digite um numero: '))
#For
print('------For------')
for m in range(1, 11):
    resultado = numero * m
    print(f'{numero} x {m} = {resultado}')

#While
print('------While------')
ciclos = 1
while ciclos <= 10:
    resultado = numero * ciclos
    print(f'{numero} x {ciclos} = {resultado}')
    ciclos += 1