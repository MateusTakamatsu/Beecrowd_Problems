ipt = gets.split()
a = ipt[0].to_i
b = ipt[1].to_i
c = ipt[2].to_i
d = ipt[3].to_i

condicoes = [(b>c),(d>a),((c+d)>(a+b)),(c>0),(d>0),((a%2)==0)]

condicoes.length().times do |i|
    if condicoes[i]
        if i == condicoes.length()-1
            puts "Valores aceitos"
        end
    else
        puts "Valores nao aceitos"
        break
    end
end
