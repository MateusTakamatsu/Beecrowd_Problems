ipt = input().split()
x = float(ipt[0])
y = float(ipt[1])

tabelaCondicaoOutput = [[(x==y==0),'Origem'],[(y==0!=x),'Eixo X'],[(x==0!=y),'Eixo Y'],[(x>0<y),'Q1'],[(x<0<y),'Q2'],[(x<0>y),'Q3'],[(x>0>y),'Q4']]

while True:
    for i in range (len(tabelaCondicaoOutput)):
        if (tabelaCondicaoOutput[i][0]):
            print(tabelaCondicaoOutput[i][1])
            break
    break
