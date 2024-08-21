ipt = input().split()
a = int(ipt[0])
b = int(ipt[1])
c = int(ipt[2])

def maior(x,y):
    return (x+y+abs(x-y))/2

maior1 = maior(a,b)
maiorFinal = int(maior(maior1,c))
print(f'{maiorFinal} eh o maior')
