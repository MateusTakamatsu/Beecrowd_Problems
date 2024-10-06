ipt = gets.split()
a = ipt[0].to_i
b = ipt[1].to_i
c = ipt[2].to_i

def maior(x,y)
    return (x+y+(x-y).abs)/2
end

maior1 = maior(a,b)
maiorFinal = maior(maior1,c).to_i
puts "#{maiorFinal} eh o maior"
