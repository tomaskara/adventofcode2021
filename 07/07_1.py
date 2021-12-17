import statistics

with open('input.txt') as f:
    data = f.read().split(',')

data_int = [int(x) for x in data]


fuel = 0
for i in data_int:
    fuel += abs(i - statistics.median(data_int))

print(fuel)
