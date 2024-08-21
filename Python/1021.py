total = float(input())
i = -1
q = 0
notasPossiveis = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
nota = notasPossiveis[i]

# Lógica funcionando, falta apenas ajustar a formatação

while i < len(notasPossiveis)-1:
    q = 0
    i+=1
    nota = notasPossiveis[i]

    while total >= nota:
        total = total - nota
        q+=1
    print(f'{q} nota(s) de R$ {nota},00')
