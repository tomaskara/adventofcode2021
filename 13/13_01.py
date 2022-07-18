with open('input.txt') as f:
    data = f.read().splitlines()

dots = data[:data.index("")]
folds = data[data.index("")+1:]

for indx,fold in enumerate(folds):
    folds[indx] = fold.split(" ")[2].split("=")

axis,num = folds[0]
if axis == 'x':
    for indx, dot in enumerate(dots):
        if int(dot.split(",")[0]) < int(num):
            pass
        else:
            new_x = int(num) + (int(num) - int(dot.split(",")[0]))
            dots[indx] = str(str(new_x) + "," + dot.split(",")[1])
if axis == 'y':
    pass


print(len(set(dots)))
