ipt1 = int(input())
ipt2 = int(input())

if(ipt1>ipt2):
    ceil = ipt1
    floor = ipt2
else:
    ceil = ipt2
    floor = ipt1

if(ceil%2==0):
    ceil-=1
else:
    ceil-=2

if(floor%2==0):
    floor+=1
else:
    floor+=2

i = floor
soma = 0
while i <= ceil:
    soma+=i
    i+=2

print(soma)
