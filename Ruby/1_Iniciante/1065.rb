res = 0
5.times do |i|
    a = gets.to_f
    if a%2 == 0
        res+=1
    end
end
puts "#{res} valores pares"
