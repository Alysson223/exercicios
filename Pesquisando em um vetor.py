from random import randint

q = []

for x in range(20):
    y = randint(0, 1000)
    q.append(y)

maior = max(q)
menor = min(q)

pos_maior = q.index(maior)+1
pos_menor = q.index(menor)+1

print(q)
print(f'O Maior valor é {maior} e sua posição é {pos_maior}')
print(f'O Menor valor é {menor} e sua posição é {pos_menor}')