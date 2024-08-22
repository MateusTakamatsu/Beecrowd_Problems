time = int(input())
hours = int(time/3600)
mins = int((time-3600*hours)/60)
secs = time - 3600*hours - 60*mins
print(f'{hours}:{mins}:{secs}')
