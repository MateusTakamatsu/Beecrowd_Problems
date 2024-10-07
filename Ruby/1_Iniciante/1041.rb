ipt = gets.split()
x = ipt[0].to_f
y = ipt[1].to_f

tabelaCondicaoOutput = [[(x==y and y==0),'Origem'],[(y==0 and 0!=x),'Eixo X'],[(x==0 and 0!=y),'Eixo Y'],[(x>0 and 0<y),'Q1'],[(x<0 and 0<y),'Q2'],[(x<0 and 0>y),'Q3'],[(x>0 and 0>y),'Q4']]

loop do
    tabelaCondicaoOutput.length().times() do |i|
        if tabelaCondicaoOutput[i][0]
            puts tabelaCondicaoOutput[i][1]
            break
        end
    end
    break
end
