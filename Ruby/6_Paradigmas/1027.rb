n = gets.to_i
arr = []

n.times do |i|
    a,b = gets.split(' ').map(&:to_i)
    
    # Pula os y inválidos
    next if (b != 1 and b != -1)

    # Ordenação do array, se for necessário
    if i == 0
        arr.push([a,b])
        puts "#{[a,b]} inserido  no caso [1] na iteração [#{i}]"
    else # Insere na menor posição possível para x e y
        dotIsInserted = false
        for dot in arr
            if a <= dot[0] and b >= dot[1]
                arr.insert(arr.index(dot),[a,b])
                dotIsInserted = true
                puts "#{[a,b]} inserido  no caso [2] na iteração [#{i}]"
                break
            end
        end
        next if dotIsInserted == true
        arr.push([a,b])
        puts "#{[a,b]} inserido  no caso [3] na iteração [#{i}]"
    end

    arr.each do |i|
        ant = arr[i-1]
        if arr[i]
    end

end
p arr
puts arr.length()
