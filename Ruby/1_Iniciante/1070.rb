ipt = gets.to_i

if ipt%2 == 0
    starting = ipt+1
else
    starting = ipt
end

6.times do
    puts starting
    starting += 2
end
