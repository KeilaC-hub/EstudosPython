import datetime

x = datetime.datetime.now()
print(x)

print(x.year)
print(x.month)
print(x.day)
print(x.strftime("%A")) # dia da semana
print(x.strftime("%B")) # mês do ano

i = 1
while i < 6:
  #print(i)
  if i == 3:
    break
  i += 1

