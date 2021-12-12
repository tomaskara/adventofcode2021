import numpy as np

with open('input.txt') as f:
    data = f.read().splitlines()

numbers = [int(num) for num in data[0].split(",")]
boards = []

for line in range(2, len(data), 6):
    current_board = np.empty((0, 5), int)
    for row in data[line:line+5]:
        row = [int(_) for _ in row.split()]
        current_board = np.append(current_board, np.array([row]), axis=0)
    boards.append(current_board)

marked_boards = np.copy(boards)

for num in numbers:
    for index_of_board, board in enumerate(boards):
        for index_of_item, item in np.ndenumerate(board):
            if item == num:
                r, c = index_of_item
                marked_boards[index_of_board][r, c] += 100
                if np.all(marked_boards[index_of_board] >= 100, axis=1)[r] or np.all(marked_boards[index_of_board] >= 100, axis=0)[c]:
                    sum_ummarked = 0
                    for _,element in np.ndenumerate(marked_boards[index_of_board]):
                        if element < 100:
                            sum_ummarked += element
                    print(sum_ummarked*num)
                    quit()

