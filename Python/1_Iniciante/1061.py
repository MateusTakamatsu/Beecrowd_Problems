# imports
import math

# inputs
diaInicio = int([i for i in input().split()][1])
arrayHoraInicio = [i for i in input().split()]
diaFim = int([i for i in input().split()][1])
arrayHoraFim = [i for i in input().split()]


# calcula a duracao total em segundos
horaInicio = int(arrayHoraInicio[0])*3600+int(arrayHoraInicio[2])*60+int(arrayHoraInicio[4])
horaFim = int(arrayHoraFim[0])*3600+int(arrayHoraFim[2])*60+int(arrayHoraFim[4])

if(horaInicio>=horaFim):
    duracaoTotal = (86400-horaInicio+horaFim) + (diaFim-diaInicio-1)*86400
else:
    duracaoTotal = horaFim-horaInicio + (diaFim-diaInicio)*86400


# calcula e printa a resposta
tabela = [[86400,'dia(s)'],[3600,'hora(s)'],[60,'minuto(s)'],[1,'segundo(s)']]
anterior = 0

for i in tabela:
    res = int(math.floor(duracaoTotal-anterior)/i[0])
    anterior += res*i[0]
    print(f'{res} {i[1]}')
