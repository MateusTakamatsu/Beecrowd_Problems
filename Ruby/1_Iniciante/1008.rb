number = gets.to_i
hoursWorked = gets.to_i
moneyPerHour = gets.to_f

salary = hoursWorked * moneyPerHour

puts "NUMBER = #{number}"
puts "SALARY = U$ %.2f" % salary
