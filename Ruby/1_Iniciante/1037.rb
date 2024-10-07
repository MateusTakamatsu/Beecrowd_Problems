num = gets.to_f.round(2)

piso = 100
intervalos = ['Fora de intervalo','Intervalo (75,100]','Intervalo (50,75]','Intervalo (25,50]','Intervalo [0,25]','Fora de intervalo']

intervalos.length().times() do |i|
    if (num > piso) or (piso==0 and 0==num) or (piso==-25 and num<0)
        puts intervalos[i]
        break
    else
        piso = piso - 25
    end
end
