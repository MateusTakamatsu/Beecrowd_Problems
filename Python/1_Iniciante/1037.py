num = round(float(input()),2)

piso = 100
intervalos = ['Fora de intervalo','Intervalo (75,100]','Intervalo (50,75]','Intervalo (25,50]','Intervalo [0,25]','Fora de intervalo']

for i in range (len(intervalos)):
    if (num > piso) or (piso==0==num) or (piso==-25 and num<0):
        print(intervalos[i])
        break
    else:
        piso = piso - 25
