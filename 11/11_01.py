import numpy as np

with open('input.txt') as f:
    data = f.read().splitlines()
arr = np.array(list(map(int, str(data[0]))))
for line in data[1:]:
    line = list(map(int, str(line)))
    arr = np.vstack([arr,line])

count = 0

for i in range(100):
    arr = arr + 1
    if 10 in arr:
        indices = list(zip(*np.where(arr >= 10)))
        for x,y in indices:
            if (x + 1) <= 9:
                arr[x + 1, y] += 1
                if (y+1) <= 9:
                    arr[x + 1, y + 1] += 1
                if (y-1) >= 0:
                    arr[x + 1, y - 1] += 1

            if (x-1) >= 0:
                arr[x - 1, y] += 1
                if (y-1) >= 0:
                    arr[x - 1, y - 1] += 1
                if (y+1) <= 9:
                    arr[x - 1, y + 1] += 1

            if (y +1) <= 9:
                arr[x, y + 1] += 1

            if (y - 1) >= 0:
                arr[x, y - 1] += 1

            for octopus in list(zip(*np.where(arr >= 10))):
                if octopus not in indices:
                    indices.append(octopus)

    count += np.count_nonzero(arr >= 10)
    arr = np.where(arr < 10, arr, 0)

print(count)
