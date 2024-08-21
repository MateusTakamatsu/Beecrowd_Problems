total = float(input())
notasPossiveis = [100, 50, 20, 10, 5, 2]
moedasPossiveis = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

def quantosDaUnidade(tipo,unidadesPossiveis,total):
    i = -1
    print(f'{tipo.upper()}S:')
    while i < len(unidadesPossiveis)-1: # Faz o loop para cada unidade
        q = 0
        i+=1
        unidade = unidadesPossiveis[i]
        while round(total,2) >= unidade: # Faz o loop para cada q em uma unidade
            total = total - unidade
            q+=1
        print(f'{q} {tipo}(s) de R$ {unidade:.2f}')
    return(total)

quantosDaUnidade('moeda',moedasPossiveis,quantosDaUnidade('nota',notasPossiveis,total))
