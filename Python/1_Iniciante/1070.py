ipt = int(input())

if(ipt%2==0):
    starting = ipt+1
else:
    starting = ipt

for i in range (6):
    print(starting)
    starting += 2
