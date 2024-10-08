ipt = gets.split().map(&:to_f)
ipt = ipt.sort.reverse
a = ipt[0]
b = ipt[1]
c = ipt[2]

tabelaCondicaoOutput = [
    [(a>=(b+c)),'NAO FORMA TRIANGULO'],
    [(a**2==(b**2+c**2)),'TRIANGULO RETANGULO'],
    [(a**2>(b**2+c**2)),'TRIANGULO OBTUSANGULO'],
    [(a**2<(b**2+c**2)),'TRIANGULO ACUTANGULO'],
    [(a==b and b==c),'TRIANGULO EQUILATERO'],
    [((a==b and b!=c) or (a!=b and b==c) or (a==c and c!=b)),'TRIANGULO ISOSCELES']
]

loop do
    tabelaCondicaoOutput.length().times do |i|
        if tabelaCondicaoOutput[i][0]
            puts tabelaCondicaoOutput[i][1]
            if i==0
                break
            end
        end
    end
    break
end
