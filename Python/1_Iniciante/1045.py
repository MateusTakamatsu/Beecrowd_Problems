ipt = [float(i) for i in input().split()]
ipt.sort(reverse=True)
a = ipt[0]
b = ipt[1]
c = ipt[2]

tabelaCondicaoOutput = [[(a>=(b+c)),'NAO FORMA TRIANGULO'],[(a**2==(b**2+c**2)),'TRIANGULO RETANGULO'],[(a**2>(b**2+c**2)),'TRIANGULO OBTUSANGULO'],[(a**2<(b**2+c**2)),'TRIANGULO ACUTANGULO'],[(a==b==c),'TRIANGULO EQUILATERO'],[(a==b!=c or a!=b==c or a==c!=b),'TRIANGULO ISOSCELES']]

while True:
    for i in range (len(tabelaCondicaoOutput)):
        if(tabelaCondicaoOutput[i][0]):
            print(tabelaCondicaoOutput[i][1])
            if(i==0):
                break
    break
