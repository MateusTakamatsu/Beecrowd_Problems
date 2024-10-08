ipt = gets.to_f
op = ipt
res = 0

tabela = [[4500,0.28],[3000,0.18],[2000,0.08]]

for i in tabela
    if op>i[0]
        res = res + ((op-i[0])*i[1]).round(2)
        op = i[0]
    end
end

if ipt <= 2000
    puts "Isento"
else
    puts "R$ %.2f" % res
end
