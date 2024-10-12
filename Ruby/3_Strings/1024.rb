n = gets.to_i
res = ''

n.times do |i|
    text = gets.chomp
    text = text.reverse
    arr = text.bytes
    arr.length().times do |i|
        if !!/[A-Za-z]/.match(arr[i].chr)
            arr[i] = arr[i] + 3
        end
        if i >= (arr.length()/2).truncate
            arr[i] = arr[i] - 1
        end
        res << arr[i].chr
    end
    res << "\n"
end

puts res
