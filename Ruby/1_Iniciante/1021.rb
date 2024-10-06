total = gets.to_f
notasPossiveis = [100, 50, 20, 10, 5, 2]
moedasPossiveis = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

def quantosDaUnidade(tipo,unidadesPossiveis,total)
    i = -1
    puts "#{tipo.upcase}S:"
    while i < unidadesPossiveis.length-1 # Faz o loop para cada unidade
        q = 0
        i+=1
        unidade = unidadesPossiveis[i]
        while total.round(2) >= unidade # Faz o loop para cada q em uma unidade
            total = total - unidade
            q+=1
        end
        puts "#{q} #{tipo}(s) de R$ %.2f" % unidade
    end
    return(total)
end

quantosDaUnidade('moeda',moedasPossiveis,quantosDaUnidade('nota',notasPossiveis,total))
