life = int(input())
years = int(life/365)
months = int((life-365*years)/30)
days = life - 365*years - 30*months
print(f'{years} ano(s)')
print(f'{months} mes(es)')
print(f'{days} dia(s)')
