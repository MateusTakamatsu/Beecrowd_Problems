sal = gets.to_f

tabelaReajuste = [
    [(0<=sal and sal<=400),15],
    [(400<sal and sal<=800),12],
    [(800<sal and sal<=1200),10],
    [(1200<sal and sal<=2000),7],
    [(sal>2000),4]
]

tabelaReajuste.length().times do |i|
    if tabelaReajuste[i][0]
        $newSal = (sal*(1+(tabelaReajuste[i][1]/100.0))).round(2)
        $percentual = tabelaReajuste[i][1]
        break
    end
end

puts "Novo salario: %.2f" % $newSal
puts "Reajuste ganho: %.2f" % ($newSal-sal)
puts "Em percentual: #{$percentual} %"
