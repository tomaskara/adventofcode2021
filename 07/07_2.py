import statistics

with open('input.txt') as f:
    data = f.read().split(',')

data_int = [int(x) for x in data]

position = round(statistics.mean(data_int))
fuel_ver1 = 0
fuel_ver2 = 0
fuel_ver3 = 0
for i in data_int:
    fuel_ver1 += sum(x for x in range(abs(i - position+1)+1))
    fuel_ver2 += sum(x for x in range(abs(i - position)+1))
    fuel_ver3 += sum(x for x in range(abs(i - position-1)+1))

print(min(fuel_ver1,fuel_ver2,fuel_ver3))