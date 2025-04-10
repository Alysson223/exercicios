arquivo_txt = 'arquivo.txt'

numero = int(input('Digite um numero: '))

with open(arquivo_txt, 'w', encoding='utf-8') as arquivo:
    for m in range(1, 11):
        resultado = numero * m
        arquivo.write(f'{numero} x {m} = {resultado}')
print('---Programa Finalizado---')