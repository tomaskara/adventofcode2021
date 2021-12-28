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
                low_points.append(item)
            #uprightcorner
            elif n_item == len(line) - 1 and line[n_item - 1] > item and hmap[n_line + 1, n_item] > item:
                low_points.append(item)
        elif n_line == len(hmap)-1 and (n_item == 0 or n_item == len(line) - 1):
            #downleftcorner
            if n_item == 0 and line[n_item+1] > item and hmap[n_line-1, n_item] > item:
                low_points.append(item)
            #downrightcorner
            elif n_item == len(line)-1 and line[n_item - 1] > item and hmap[n_line - 1, n_item] > item:
                low_points.append(item)

        #handleedges
        elif n_item == 0 or n_item == len(line) - 1:
            if n_item == 0 and line[n_item+1] > item and hmap[n_line-1, n_item] > item and hmap[n_line+1, n_item] > item:
                low_points.append(item)
            elif n_item == len(line) - 1 and line[n_item-1] > item and hmap[n_line-1, n_item] > item and hmap[n_line+1, n_item] > item:
                low_points.append(item)
        elif n_line == 0 or n_line == len(hmap) - 1:
            if n_line == 0 and line[n_item-1] > item and line[n_item+1] > item and hmap[n_line+1, n_item] > item:
                low_points.append(item)
            elif n_line == len(hmap) - 1 and line[n_item-1] > item and line[n_item+1] > item and hmap[n_line-1, n_item] > item:
                low_points.append(item)

        else:
            if line[n_item-1] > item and line[n_item+1] > item and hmap[n_line-1, n_item] > item and hmap[n_line+1, n_item] > item:
                low_points.append(item)

print(sum(low_points)+len(low_points))







