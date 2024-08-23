nums = [int(i) for i in input().split()]
num1 = nums[0]
num2 = nums[1]
num3 = nums[2]

nums.sort()

opt = nums
opt.append('')
opt.append(num1)
opt.append(num2)
opt.append(num3)

for i in range (len(opt)):
    print(opt[i])
