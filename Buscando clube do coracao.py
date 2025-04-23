seleçoes = [
    'Malaria',
    'Peste Bubonica',
    'Ebola',
    'Dengue'
]

seleçao = input('Digite a seleção desejada: ')
find = False

for x in range(len(seleçoes)):
    if seleçao.upper() == seleçoes[x].upper():
        find = True

if find:
    print('Achei')
else:
    print('Não Achei')