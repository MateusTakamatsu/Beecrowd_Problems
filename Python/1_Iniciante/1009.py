name = input()
salary = float(input())
sells = float(input())

finalMoney = salary + ((15*sells)/100)

print(f'TOTAL = R$ {finalMoney:.2f}')
