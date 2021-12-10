with open('input.txt') as f:
    data = f.read().splitlines()

gamma = ""
epsilon = ""
for i in list(zip(*data)):
  gamma += max(set(i), key = i.count)
  epsilon += min(set(i), key = i.count)

print(int(gamma, 2)*int(epsilon, 2))
