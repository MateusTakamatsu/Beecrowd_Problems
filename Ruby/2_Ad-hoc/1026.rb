ARGF.each_line do |line|
    x,y = line.split()
    puts (x.to_i^y.to_i)
end
