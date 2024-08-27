ipt = float(input())
op = ipt
res = 0

tabela = [[4500,0.28],[3000,0.18],[2000,0.08]]

for i in tabela:
    if(op>i[0]):
        res = res + round(((op-i[0])*i[1]),2)
        op = i[0]

if(ipt<=2000):
    print('Isento')
else:
    print(f'R$ {res:.2f}')
