ipt = [float(i) for i in input().split()]
a = ipt[0]
b = ipt[1]
c = ipt[2]

# Seria mais fácil apenas dar 5 prints, mas decidi estudar fazer dessa forma
array = [['TRIANGULO',((a*c)/2)],['CIRCULO',(3.14159*c**2)],['TRAPEZIO',(((a+b)*c)/2)],['QUADRADO',(b**2)],['RETANGULO',(a*b)]]
for i in array:
    print(f'{i[0]}: {i[1]:.3f}')
