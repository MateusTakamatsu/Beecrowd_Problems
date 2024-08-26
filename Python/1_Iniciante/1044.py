ipt = [int(i) for i in input().split()]
ipt.append(ipt[0])

for i in range (len(ipt)):
    div = ipt[i]/ipt[(i+1)]
    if ((div - round(div)) == 0):
        print('Sao Multiplos')
        break
    elif(i==1):
        print('Nao sao Multiplos')
        break
