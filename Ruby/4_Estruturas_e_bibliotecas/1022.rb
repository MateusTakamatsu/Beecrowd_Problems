n = gets.to_i

n.times do |i|
    ipt = gets.split(' ')
    n1 = ipt[0].to_i
    d1 = ipt[2].to_i
    n2 = ipt[4].to_i
    d2 = ipt[6].to_i
    op = ipt[3]

    dr  = (op != '/') ? d1*d2 : d1*n2
    nr = (op == '*') ? n1*n2 : ((op == '/') ? n1*d2 : (n1*d2).send(op, (n2*d1)))
    puts "#{nr}/#{dr}" << ' = ' << "#{Rational(nr,dr)}"
end
