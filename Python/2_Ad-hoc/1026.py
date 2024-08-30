import sys
for line in sys.stdin:
    x,y = [int(i) for i in line.split()]
    print(x ^ y)
