pares = 0
impares = 0
positivos = 0
negativos = 0

5.times do |i|
    a = gets.to_f
    if a%2 == 0
        pares+=1
    end
    if a%2 !=0
        impares+=1
    end
    if a > 0
        positivos+=1
    end
    if a < 0
        negativos+=1
    end
end

puts "#{pares} valor(es) par(es)"
puts "#{impares} valor(es) impar(es)"
puts "#{positivos} valor(es) positivo(s)"
puts "#{negativos} valor(es) negativo(s)"
