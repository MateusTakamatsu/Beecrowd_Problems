ipt = gets.to_i
if ipt%2 != 0
    ipt-=1
end

i = 2
while i <= ipt
    puts "#{i}^2 = #{i**2}"
    i+=2
end
