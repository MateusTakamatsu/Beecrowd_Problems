ipt = input().split()
a = int(ipt[0])
b = int(ipt[1])
c = int(ipt[2])
d = int(ipt[3])

condicoes = [(b>c),(d>a),((c+d)>(a+b)),(c>0),(d>0),((a%2)==0)]

for i in range (len(condicoes)):
    if (condicoes[i]):
        if i == (len(condicoes)-1):
            print('Valores aceitos')
    else:
        print('Valores nao aceitos')
        break
