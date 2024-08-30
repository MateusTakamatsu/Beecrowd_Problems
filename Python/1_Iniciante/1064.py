res = 0
soma = 0
for i in range (6):
    a = float(input())
    if(a>0):
        res+=1
        soma += a
print(f'{res} valores positivos')
print(round(soma/res,1))
