import re

with open('input.txt') as f:
    data = f.read().splitlines()

scores = {')': 3,
          ']': 57,
          '}': 1197,
          '>': 25137}

score = 0

for line in data:
    while True:
        start = len(line)
        line = re.sub('\(\)|\[]|\{}|<>', '', line)
        if len(line) == start:
            break
    if re.search(']|}|>|\)|]', line):
        score += scores[re.search(']|}|>|\)|]', line).group()]

print(score)
