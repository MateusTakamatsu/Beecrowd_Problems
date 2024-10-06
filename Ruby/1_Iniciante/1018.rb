total = gets.to_i
i = -1
notasPossiveis = [100, 50, 20, 10, 5, 2, 1]
nota = notasPossiveis[i]

puts total
while i < 6
    q = 0
    i+=1
    nota = notasPossiveis[i]
    
    while total >= nota
        total = total - nota
        q+=1
    end
    puts "#{q} nota(s) de R$ #{nota},00"
end
