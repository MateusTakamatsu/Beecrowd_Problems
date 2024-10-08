nums = gets.split().map(&:to_i)
num1 = nums[0]
num2 = nums[1]
num3 = nums[2]

nums = nums.sort

opt = nums
opt.append('')
opt.append(num1)
opt.append(num2)
opt.append(num3)

opt.length().times do |i|
    puts opt[i]
end
