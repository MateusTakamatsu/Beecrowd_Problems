ipt = gets.split().map(&:to_i)
a = ipt[0]
b = ipt[1]
if a >= b
    puts "O JOGO DUROU #{(24-a+b)} HORA(S)"
else
    puts "O JOGO DUROU #{(b-a)} HORA(S)"
end
