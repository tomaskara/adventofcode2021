with open('input.txt') as f:
    data = f.read().splitlines()


horizontal = 0
depth = 0
aim = 0
for i in data:
    direction,lenght = i.split()
    if direction == "forward":
        horizontal += int(lenght)
        depth = depth + (aim*int(lenght))
    elif direction == "down":
        aim += int(lenght)
    else:
        aim -= int(lenght)

print(horizontal*depth)


