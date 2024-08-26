nums = [float(i) for i in input().split()]
num1 = nums[0]
num2 = nums[1]
num3 = nums[2]

nums.sort(reverse=True)
newNum1 = nums[0]
newNum2 = nums[1]
newNum3 = nums[2]

if((newNum2+newNum3)>newNum1):
    print(f'Perimetro = {num1+num2+num3:.1f}')
else:
    print(f'Area = {(num1+num2)*num3/2:.1f}')
