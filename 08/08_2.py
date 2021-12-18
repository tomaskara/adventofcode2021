with open('input.txt') as f:
    data = f.read().splitlines()

outputs = [x.split(' | ')[1] for x in data]
wires = [x.split(' | ')[0] for x in data]

result = 0

for output, wire in zip(outputs, wires):
    dictionary_of_numbers = {i: [] for i in range(10)}
    words = wire.split(' ')
    # match good_patterns first
    for word in words:
        if len(word) == 3:
            dictionary_of_numbers[7] = [x for x in word]
        elif len(word) == 2:
            dictionary_of_numbers[1] = [x for x in word]
        elif len(word) == 4:
            dictionary_of_numbers[4] = [x for x in word]
        elif len(word) == 7:
            dictionary_of_numbers[8] = [x for x in word]
    # match deductive 9, 6, 0
    for word in words:
        if len(word) == 6:
            if all(characters in word for characters in dictionary_of_numbers[4]):
                dictionary_of_numbers[9] = [x for x in word]
            elif all(characters in word for characters in dictionary_of_numbers[7]):
                dictionary_of_numbers[0] = [x for x in word]
            else:
                dictionary_of_numbers[6] = [x for x in word]

    # finaly match 3, 5 and 2
    for word in words:
        section = [x for x in dictionary_of_numbers[1] if x not in dictionary_of_numbers[6]]
        if len(word) == 5:
            if all(characters in word for characters in dictionary_of_numbers[7]):
                dictionary_of_numbers[3] = [x for x in word]
            elif len(word) == 5 and section[0] not in word:
                dictionary_of_numbers[5] = [x for x in word]
            else:
                dictionary_of_numbers[2] = [x for x in word]

    numbers = output.split(' ')
    digits = ''
    for number in numbers:
        characters = [x for x in number]
        characters.sort()
        for item in dictionary_of_numbers.items():
            y = item[1]
            y.sort()
            if characters == y:
                digits += str(item[0])
    result += int(digits)

print(result)







