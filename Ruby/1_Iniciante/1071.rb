ipt1 = gets.to_i
ipt2 = gets.to_i

if ipt1 > ipt2
    ceil = ipt1
    floor = ipt2
else
    ceil = ipt2
    floor = ipt1
end

if ceil%2 == 0
    ceil-=1
else
    ceil-=2
end

if floor%2 ==0
    floor+=1
else
    floor+=2
end

i = floor
soma = 0
while i <= ceil
    soma+=i
    i+=2
end

puts soma
