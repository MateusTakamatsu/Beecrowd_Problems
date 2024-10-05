peca1 = gets.split()
num1 = peca1[1].to_i
valor1 = peca1[2].to_f

peca2 = gets.split()
num2 = peca2[1].to_i
valor2 = peca2[2].to_f

preco = (num1*valor1) + (num2*valor2)

puts "VALOR A PAGAR: R$ %.2f" % preco
