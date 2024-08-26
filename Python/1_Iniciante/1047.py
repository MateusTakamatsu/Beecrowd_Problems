import math
ipt = [int(i) for i in input().split()]
a = 60*ipt[0]
b = ipt[1]
c = 60*ipt[2]
d = ipt[3]

horaInicio = (a+b)
horaFim = (c+d)

if(horaInicio>=horaFim):
    duracaoTotal = (1440-(horaInicio)+horaFim)
else:
    duracaoTotal = horaFim-horaInicio

print(f'O JOGO DUROU {math.trunc(duracaoTotal/60)} HORA(S) E {duracaoTotal%60} MINUTO(S)')
