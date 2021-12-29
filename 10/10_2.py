import re
import statistics

with open('input.txt') as f:
    data = f.read().splitlines()

scores = {')': 1,
          ']': 2,
          '}': 3,
          '>': 4}

pairs = {'(': ')',
         '[': ']',
         '{': '}',
         '<': '>'}

scores_list = []

for line in data:
    while True:
        start = len(line)
        line = re.sub('\(\)|\[]|\{}|<>', '', line)
        if len(line) == start:
            break
    if not re.search(']|}|>|\)|]', line):
        complete_list = []
        for char in line:
            complete_list.append(pairs[char])
        complete_list.reverse()
        score = 0
        for i in complete_list:
            score = score * 5 + scores[i]
        scores_list.append(score)

print(statistics.median(scores_list))
