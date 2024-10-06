time = gets.to_i
hours = (time/3600.0).to_i
mins = ((time-3600*hours)/60.0).to_i
secs = time - 3600*hours - 60*mins
puts "#{hours}:#{mins}:#{secs}"
