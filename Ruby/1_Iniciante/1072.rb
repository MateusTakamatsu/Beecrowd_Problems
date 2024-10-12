n = gets.to_i
valIn = 0
valOut = 0

n.times do
    a = gets.to_i
    if a >= 10 and a <= 20
        valIn+=1
    else
        valOut+=1
    end
end

puts "#{valIn} in"
puts "#{valOut} out"
