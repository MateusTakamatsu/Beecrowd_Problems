name = gets
salary = gets.to_f
sells = gets.to_f

finalMoney = salary + ((15*sells)/100)

puts "TOTAL = R$ %.2f" % finalMoney
