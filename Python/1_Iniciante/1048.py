sal = float(input())

tabelaReajuste = [[(0<=sal<=400),15],[(400<sal<=800),12],[(800<sal<=1200),10],[(1200<sal<=2000),7],[(sal>2000),4]]

for i in range (len(tabelaReajuste)):
    if(tabelaReajuste[i][0]):
        newSal = round(sal*(1+(tabelaReajuste[i][1]/100)),2)
        break

print(f'Novo salario: {newSal:.2f}')
print(f'Reajuste ganho: {(newSal-sal):.2f}')
print(f'Em percentual: {tabelaReajuste[i][1]} %')
