ipt = [int(i) for i in input().split()]
a = ipt[0]
b = ipt[1]
if(a>=b):
    print(f'O JOGO DUROU {(24-a+b)} HORA(S)')
else:
    print(f'O JOGO DUROU {(b-a)} HORA(S)')
