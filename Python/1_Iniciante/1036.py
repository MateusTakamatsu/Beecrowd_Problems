import math
ipt = input().split()
a = float(ipt[0])
b = float(ipt[1])
c = float(ipt[2])
delta = b**2-4*a*c

if (round(delta,5) < 0) or (a == 0):
    print('Impossivel calcular')
else:
    deltaSqrt = math.sqrt(round(delta,5))
    print(f'R1 = {(-b + deltaSqrt)/(2*a):.5f}')
    print(f'R2 = {(-b - deltaSqrt)/(2*a):.5f}')
