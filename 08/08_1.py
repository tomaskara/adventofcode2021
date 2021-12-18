with open('input.txt') as f:
    data = f.read().splitlines()

outputs = [x.split('| ')[1] for x in data]

result = 0

for output in outputs:
    good_patterns = 2,3,4,7
    words = output.split(' ')
    for word in words:
        if len(word) in good_patterns:
            result += 1

print(result)