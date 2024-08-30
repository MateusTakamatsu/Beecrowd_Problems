ipt = int(input())
if(ipt%2!=0):
    ipt-=1

i = 2
while i <= ipt:
    print(f'{i}^2 = {i**2}')
    i+=2
