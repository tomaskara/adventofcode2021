with open('input.txt') as f:
    data = f.read().splitlines()


def oxy(numbers):
    index = 0
    while len(numbers) != 1:
        new_data = numbers.copy()
        zip_list = list(zip(*numbers))
        if max(set(zip_list[index]), key=(zip_list[index].count)) != min(set(zip_list[index]), key=(zip_list[index].count)):
            ox_key = max(set(zip_list[index]), key=(zip_list[index].count))
        else:
            ox_key = "1"

        for i in numbers:
            if i[index] != ox_key:
                new_data.remove(i)
            else:
                pass

        index += 1
        numbers = new_data
    return numbers


def co(numbers):
    index = 0
    while len(numbers) != 1:
        new_data = numbers.copy()
        zip_list = list(zip(*numbers))
        if max(set(zip_list[index]), key=(zip_list[index].count)) != min(set(zip_list[index]),
                                                                         key=(zip_list[index].count)):
            ox_key = min(set(zip_list[index]), key=(zip_list[index].count))
        else:
            ox_key = "0"

        for i in numbers:
            if i[index] != ox_key:
                new_data.remove(i)
            else:
                pass

        index += 1
        numbers = new_data

    return numbers


print(int(oxy(data)[0], 2) * int(co(data)[0], 2))

