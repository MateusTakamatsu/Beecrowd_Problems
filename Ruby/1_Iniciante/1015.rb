p1 = gets.split()
x1 = p1[0].to_f
y1 = p1[1].to_f

p2 = gets.split()
x2 = p2[0].to_f
y2 = p2[1].to_f

distancia = Math.sqrt((x1-x2)**2+(y1-y2)**2)

puts "%.4f" % distancia
