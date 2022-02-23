import functions as func

x = float(input('Digite um numero: '))
y = float(input('Digite outro numero: '))

print('\n *** ESCOLHA UMA OPÇÃO ***\n')
print('1 - Somar')
print('2 - Subtrair')
print('3 - Multiplicar')
print('4 - Dividir')
option = int(input(': '))

if option == 1:
    print(func.somar(x, y))
elif option == 2:
    print(func.subtrair(x, y))
elif option == 3:
    print(func.mult(x, y))
else:
    print(func.div(x, y))
