ipt = gets.split().map(&:to_f)

media = (2*ipt[0]+3*ipt[1]+4*ipt[2]+ipt[3])/10.0
puts "Media: %.1f" % media

tabela = [[(media.round(1)<5),'reprovado'],[(5<=media.round(1) and media.round(1)<=6.9),'em exame'],[(media.round(1)>=7),'aprovado']]

tabela.length().times do |i|
    if tabela[i][0]
        puts "Aluno #{tabela[i][1]}."
        if i==1
            notaExame = gets.to_f
            puts "Nota do exame: %.1f" % notaExame.round(1)
            mediaFInal = (media+notaExame)/2.0
            if mediaFInal>=5
                puts "Aluno aprovado."
            else
                puts "Aluno reprovado."
            end
            puts "Media final: %.1f" % mediaFInal.round(1)
        end
    end
end
