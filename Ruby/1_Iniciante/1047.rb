ipt = gets.split().map(&:to_i)
a = 60*ipt[0]
b = ipt[1]
c = 60*ipt[2]
d = ipt[3]

horaInicio = (a+b)
horaFim = (c+d)

if horaInicio >= horaFim
    duracaoTotal = (1440-(horaInicio)+horaFim)
else
    duracaoTotal = horaFim-horaInicio
end

puts "O JOGO DUROU #{(duracaoTotal/60).truncate} HORA(S) E #{duracaoTotal%60} MINUTO(S)"
