ipt = input().split()
cod = int(ipt[0])
quant = int(ipt[1])

tabela = [4,4.5,5,2,1.5]

print(f'Total: R$ {quant*tabela[cod-1]:.2f}')
