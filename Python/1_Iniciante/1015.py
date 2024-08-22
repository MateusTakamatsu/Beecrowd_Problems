import math

p1 = input().split()
x1 = float(p1[0])
y1 = float(p1[1])

p2 = input().split()
x2 = float(p2[0])
y2 = float(p2[1])

distancia = math.sqrt((x1-x2)**2+(y1-y2)**2)

print(f'{distancia:.4f}')
