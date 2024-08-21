ipt = input().split()
a = float(ipt[0])
b = float(ipt[1])
c = float(ipt[2])

triangulo = (a*c)/2
circulo = 3.14159*c**2
trapezio = ((a+b)*c)/2
quadrado = b**2
retangulo = a*b

# Seria mais fácil apenas dar 5 prints, mas decidi estudar fazer dessa forma
array = ['triangulo', 'circulo', 'trapezio', 'quadrado', 'retangulo']
for i in range (len(array)):
    forma = array[i]
    print(f'{forma.upper()}: {globals().get(forma):.3f}')
