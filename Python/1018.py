total = int(input())
i = -1
q = 0
notasPossiveis = [100, 50, 20, 10, 5, 2, 1]
nota = notasPossiveis[i]

print(total)
while i < 6:
    q = 0
    i+=1
    nota = notasPossiveis[i]

    while total >= nota:
        total = total - nota
        q+=1
    print(f'{q} nota(s) de R$ {nota},00')
