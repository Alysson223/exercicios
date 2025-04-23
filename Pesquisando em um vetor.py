from random import randint

q = []

for x in range(20):
    numero = randint(0, 1000)
    q.append(numero)

maior = -1
pos_maior = -1
menor = 1000
pos_menor = -1

for i in range(len(q)):
    if q[i] > maior:
        maior = q[i]
        pos_maior = i
    if q[i] < menor:
        menor = q[i]
        pos_menor = i

print(q)
print(f'O maior valor é {maior} e sua posição é {pos_maior}')
print(f'O menor valor é {menor} e sua posição é {pos_menor}')