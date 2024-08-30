# Solução escrita antes de eu saber que ^ fazia a operação bit por bit
import sys
res = []
for line in sys.stdin:
    # Formata as entradas como binário em um array de strings sem os zeros à esquerda. Exemplo: ['1','0','1','0']
    ipt = line.split()
    x,y = [list(bin(int(i))) for i in ipt]
    del x[0:2]
    del y[0:2]

    # Descobre o comprimento de cada entrada e define qual é a maior entrada
    lenx = len(x)
    leny = len(y)
    if(lenx>=leny):
        maiorLen = lenx
    else:
        maiorLen = leny

    # Pega a menor entrada e adiciona zeros à esquerda até ter o mesmo tamanho da maior
    for i in range (lenx-leny):
        y.insert(0,'0')
    for i in range (leny-lenx):
        x.insert(0,'0')

    # Inicia o preenchimento da resposta com zeros antes do comprimento da maior entrada. Exemplo: ['0','0','0',...,'0']
    preRes = []
    for i in range (32-maiorLen):
        preRes.append('0')

    # Compara apenas as partes essenciais das duas entradas e coloca na resposta
    for i in range(maiorLen):
        a = x[(i)]
        b = y[(i)]
        if(a==b):
            preRes.append('0')
        else:
            preRes.append('1')
    res.append(int(''.join(preRes),2))

for i in res:
    print(i)
