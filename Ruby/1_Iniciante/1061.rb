# inputs
diaInicio = gets.split()[1].to_i
arrayHoraInicio = gets.split()
diaFim = gets.split()[1].to_i
arrayHoraFim = gets.split()


# calcula a duracao total em segundos
horaInicio = arrayHoraInicio[0].to_i*3600+arrayHoraInicio[2].to_i*60+arrayHoraInicio[4].to_i
horaFim = arrayHoraFim[0].to_i*3600+arrayHoraFim[2].to_i*60+arrayHoraFim[4].to_i

if horaInicio >= horaFim
    duracaoTotal = (86400-horaInicio+horaFim) + (diaFim-diaInicio-1)*86400
else
    duracaoTotal = horaFim-horaInicio + (diaFim-diaInicio)*86400
end


# calcula e printa a resposta
tabela = [[86400,'dia(s)'],[3600,'hora(s)'],[60,'minuto(s)'],[1,'segundo(s)']]
anterior = 0

tabela.each do |i|
    res = ((duracaoTotal-anterior).floor/i[0].to_f).to_i
    anterior += res*i[0]
    puts "#{res} #{i[1]}"
end
