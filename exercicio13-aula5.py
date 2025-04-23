salario = float(input('Coloque seu salario mensal: '))
if 0 < salario <= 2000:
    print('Seu salario está isento de imposto')
elif 2000.01 <= salario <= 3500:
    salario = salario/10
    print(f'Com o seu salario o valor ser pago de imposto é de R${salario} ')
elif 3500 < salario:
    salario = salario * 15 / 100
    print(f'Com o seu salario o valor ser pago de imposto é de R${salario} ')
else:
    print('Valor Invalido')