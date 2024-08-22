ipt = input().split()
nota1 = float(ipt[0])
nota2 = float(ipt[1])
nota3 = float(ipt[2])
nota4 = float(ipt[3])

media = (2*nota1+3*nota2+4*nota3+nota4)/10
print(f'Media: {media:.1f}')

tabela = [[(round(media,1)<5),'reprovado'],[(5<=round(media,1)<=6.9),'em exame'],[(round(media,1)>=7),'aprovado']]

for i in range (len(tabela)):
    if(tabela[i][0]):
        print(f'Aluno {tabela[i][1]}.')
        if(i==1):
            notaExame = float(input())
            print(f'Nota do exame: {round(notaExame,1):.1f}')
            mediaFInal = (media+notaExame)/2
            if(mediaFInal>=5):
                print('Aluno aprovado.')
            else:
                print('Aluno reprovado.')
            print(f'Media final: {round(mediaFInal,1):.1f}')
