ipt = gets.split()
a = ipt[0].to_f
b = ipt[1].to_f
c = ipt[2].to_f
delta = b**2-4*a*c

if delta.round(5) < 0 or a == 0
    puts "Impossivel calcular"
else
    deltaSqrt = Math.sqrt(delta.round(5))
    puts "R1 = %.5f" % ((-b + deltaSqrt)/(2*a))
    puts "R2 = %.5f" % ((-b - deltaSqrt)/(2*a))
end
