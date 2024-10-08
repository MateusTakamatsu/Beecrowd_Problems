ipt = gets.split().map(&:to_i)
ipt.append(ipt[0])

ipt.length().times do |i|
    div = ipt[i].to_f/ipt[(i+1)]
    if (div - div.round()) == 0
        puts "Sao Multiplos"
        break
    elsif i == 1
        puts "Nao sao Multiplos"
        break
    end
end
