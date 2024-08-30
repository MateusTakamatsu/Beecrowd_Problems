n = int(input())
valIn = 0
valOut = 0

for i in range (n):
    a = int(input())
    if(a>=10 and a<=20):
        valIn+=1
    else:
        valOut+=1

print(f'{valIn} in')
print(f'{valOut} out')
