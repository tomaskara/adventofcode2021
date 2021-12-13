import numpy as np

with open('input.txt') as f:
    data = f.read().splitlines()

for indx,i in enumerate(data):
  j = i.split(' -> ')
  data[indx] = j


floor = np.zeros((1000,1000), dtype=int)

for vent in data:
  x1, y1 = [int(i) for i in vent[0].split(',')]
  x2, y2 = [int(i) for i in vent[1].split(',')]
  y=[y1,y2]
  y.sort()
  x=[x1,x2]
  x.sort()
  if y1==y2 and x1==x2:
    floor[y1,x1] += 1
  elif y1==y2:
    floor[y1,x[0]:x[1]+1] += 1
  elif x1==x2:
    floor[y[0]:y[1]+1,x1] += 1


print((floor > 1).sum())
