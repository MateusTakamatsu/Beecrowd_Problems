linha1 = input()
linha2 = input()
array1 = linha1.split()
array2 = linha2.split()

num1 = int(array1[1])
valor1 = float(array1[2])
num2 = int(array2[1])
valor2 = float(array2[2])

preco = (num1*valor1) + (num2*valor2)

print(f'VALOR A PAGAR: R$ {preco:.2f}')
