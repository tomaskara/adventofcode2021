import numpy as np

with open('input.txt') as f:
    data = f.read().splitlines()

dots = data[:data.index("")]
folds = data[data.index("")+1:]

for indx,fold in enumerate(folds):
    folds[indx] = fold.split(" ")[2].split("=")

for axis,num in folds:
    if axis == 'x':
        for indx,dot in enumerate(dots):
            if int(dot.split(",")[0]) < int(num):
                pass
            else:
                new_x = int(num)+ (int(num) - int(dot.split(",")[0]))
                dots[indx] = str(str(new_x)+","+dot.split(",")[1])
    if axis == 'y':
        for indx,dot in enumerate(dots):
            if int(dot.split(",")[1]) < int(num):
                pass
            else:
                new_y = int(num)+ (int(num) - int(dot.split(",")[1]))
                dots[indx] = str(dot.split(",")[0]+","+str(new_y))

dots = set(dots)

array = np.zeros((6, 40),dtype=int)
for indices in dots:
    array[int(indices.split(",")[1])][int(indices.split(",")[0])] = "1"

for line in array:
    line = list(line)
    for index, item in enumerate(line):
        if item == 1:
            line[index] = str("⬛")
        else:
            line[index] = str("⬜")
    print(*line)
