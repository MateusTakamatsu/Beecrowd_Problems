ipt = gets.split()
cod = ipt[0].to_i
quant = ipt[1].to_i

tabela = [4,4.5,5,2,1.5]

puts "Total: R$ %.2f" % (quant*tabela[cod-1])
