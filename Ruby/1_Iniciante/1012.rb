ipt = gets.split()
a = ipt[0].to_f
b = ipt[1].to_f
c = ipt[2].to_f

# Seria mais fácil apenas dar 5 prints, mas decidi estudar fazer dessa forma
array = [['TRIANGULO',((a*c)/2.0)],['CIRCULO',(3.14159*c**2)],['TRAPEZIO',(((a+b)*c)/2.0)],['QUADRADO',(b**2)],['RETANGULO',(a*b)]]
for i in array
    puts "#{i[0]}: %.3f" % i[1]
end
