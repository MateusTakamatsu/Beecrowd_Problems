res = 0
soma = 0
6.times do |i|
    a = gets.to_f
    if a > 0
        res+=1
        soma += a
    end
end
puts "#{res} valores positivos"
puts (soma/res.to_f).round(1)
