life = gets.to_i
years = (life/365.0).to_i
months = ((life-365*years)/30.0).to_i
days = life - 365*years - 30*months
puts "#{years} ano(s)"
puts "#{months} mes(es)"
puts "#{days} dia(s)"
