peca1 = input().split()
num1 = int(peca1[1])
valor1 = float(peca1[2])

peca2 = input().split()
num2 = int(peca2[1])
valor2 = float(peca2[2])

preco = (num1*valor1) + (num2*valor2)

print(f'VALOR A PAGAR: R$ {preco:.2f}')
