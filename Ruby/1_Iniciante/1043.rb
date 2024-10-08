nums = gets.split().map(&:to_f)
num1 = nums[0]
num2 = nums[1]
num3 = nums[2]

nums = nums.sort.reverse
newNum1 = nums[0]
newNum2 = nums[1]
newNum3 = nums[2]

if (newNum2+newNum3) > newNum1
    puts "Perimetro = %.1f" % (num1+num2+num3)
else
    puts "Area = %.1f" % ((num1+num2)*num3/2.0)
end
