import numpy as np

with open('input.txt') as f:
    data = f.read().splitlines()

for index, ln in enumerate(data):
    data[index] = [int(x) for x in ln]


hmap = np.array(data)

low_points = []

for n_line, line in enumerate(hmap):
    for n_item, item in enumerate(line):
        #handlecorners
        if n_line == 0 and (n_item == 0 or n_item == len(line) - 1):
            #upleftcorner
            if n_item == 0 and line[n_item+1] > item and hmap[n_line+1, n_item] > item:
                low_points.append([n_line, n_item])
            #uprightcorner
            elif n_item == len(line) - 1 and line[n_item - 1] > item and hmap[n_line + 1, n_item] > item:
                low_points.append([n_line, n_item])
        elif n_line == len(hmap)-1 and (n_item == 0 or n_item == len(line) - 1):
            #downleftcorner
            if n_item == 0 and line[n_item+1] > item and hmap[n_line-1, n_item] > item:
                low_points.append([n_line, n_item])
            #downrightcorner
            elif n_item == len(line)-1 and line[n_item - 1] > item and hmap[n_line - 1, n_item] > item:
                low_points.append([n_line, n_item])

        #handleedges
        elif n_item == 0 or n_item == len(line) - 1:
            if n_item == 0 and line[n_item+1] > item and hmap[n_line-1, n_item] > item and hmap[n_line+1, n_item] > item:
                low_points.append([n_line, n_item])
            elif n_item == len(line) - 1 and line[n_item-1]>item and hmap[n_line-1,n_item]>item and hmap[n_line+1,n_item] > item:
                low_points.append([n_line, n_item])
        elif n_line == 0 or n_line == len(hmap) - 1:
            if n_line == 0 and line[n_item-1]>item and line[n_item+1] > item and hmap[n_line+1, n_item] > item:
                low_points.append([n_line, n_item])
            elif n_line == len(hmap) - 1 and line[n_item-1]>item and line[n_item+1] > item and hmap[n_line-1 , n_item] > item:
                low_points.append([n_line, n_item])

        else:
            if line[n_item-1]>item and line[n_item+1] > item and hmap[n_line-1,n_item] > item and hmap[n_line+1 , n_item] > item:
                low_points.append([n_line, n_item])

been_there = []


def basin(row,column):
    new_nods = []
    if column + 1 < len(line):
        if hmap[row, column+1] != 9 and [row, column+1] not in been_there:
            been_there.append([row, column+1])
            new_nods.append([row, column+1])
    if column - 1 >= 0:
        if hmap[row, column-1] != 9 and [row, column-1] not in been_there:
            been_there.append([row, column - 1])
            new_nods.append([row, column-1])
    if row + 1 < len(hmap):
        if hmap[row+1, column] != 9 and [row+1, column] not in been_there:
            been_there.append([row+1, column])
            new_nods.append([row+1, column])
    if row - 1 >= 0:
        if hmap[row-1, column] != 9 and [row - 1, column] not in been_there:
            been_there.append([row - 1, column])
            new_nods.append([row-1, column])

    while new_nods:
        for i in new_nods:
            basin(i[0], i[1])
            new_nods.remove(i)

    return been_there


basins = []

for point in low_points:
    been_there = [point]
    basins.append(len(basin(point[0], point[1])))

basins.sort(reverse=True)

print(basins[0]*basins[1]*basins[2])








