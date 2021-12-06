with open('input.txt') as f:
    data = f.read().splitlines()


horizontal = 0
depth = 0
for i in data:
    direction, lenght = i.split()
    if direction == "forward":
        horizontal += int(lenght)
    elif direction == "down":
        depth += int(lenght)
    else:
        depth -= int(lenght)

print(horizontal*depth)