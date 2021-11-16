month_money = int(input())
year_money = 12*month_money
yisa = float(input())
mangi = int(input())
for i in range(mangi):
    year_money = year_money * (100+yisa) / 100
print(year_money)