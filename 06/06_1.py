from copy import deepcopy

with open('input.txt') as f:
    data = f.read().split(',')

DAYS = 80

data_int = [int(x) for x in data]


dictionary_of_timers = {i: 0 for i in range(9)}
for fish in data_int:
    dictionary_of_timers[fish] += 1

for day in range(DAYS):
    temp_dict_of_timers = deepcopy(dictionary_of_timers)

    dictionary_of_timers[0] = temp_dict_of_timers[1]
    dictionary_of_timers[1] = temp_dict_of_timers[2]
    dictionary_of_timers[2] = temp_dict_of_timers[3]
    dictionary_of_timers[3] = temp_dict_of_timers[4]
    dictionary_of_timers[4] = temp_dict_of_timers[5]
    dictionary_of_timers[5] = temp_dict_of_timers[6]
    dictionary_of_timers[6] = temp_dict_of_timers[7] + temp_dict_of_timers[0]
    dictionary_of_timers[7] = temp_dict_of_timers[8]
    dictionary_of_timers[8] = temp_dict_of_timers[0]


print(sum(dictionary_of_timers.values()))









