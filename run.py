# loading necessary functions
def check_win(cell):
    win_loc = [[0, 1, 2], [0, 3, 6], [0, 4, 8], [1, 4, 7], [2, 4, 6], [2, 5, 8], [3, 4, 5], [6, 7, 8]]
    win_count = []
    for z in win_loc:
        x_tmp = []
        for y in [0, 1, 2]:
            loc = z[y]
            x_tmp.append(cell[loc])
        win_count.append(x_tmp)

    X_count = [x.count('X') for x in win_count].count(3)
    O_count = [x.count('O') for x in win_count].count(3)
    Blk_count = cell.count(" ")

    if abs(X_count - O_count) > 0:
        if X_count > O_count:
            return 1  # X wins
        elif X_count < O_count:
            return 2  # O wins
    elif X_count == O_count == 1:
        return 0  # impossible
    elif X_count == O_count == 0:
        if abs(cell.count('X') - cell.count('O')) > 1:
            return 0  # impossible
        elif (cell.count('X') - cell.count('O')) <= 1 and Blk_count != 0:
            return 4  # Game not finished
        elif (cell.count('X') - cell.count('O')) <= 1 and Blk_count == 0:
            return 3  # Draw


def display_grid(cell):
    print("---------")
    for i in range(0, len(cell), 3):
        print('| ' + ' '.join(cell[i:i + 3]) + ' |')
    print("---------")

# 1. Prints an empty grid at the beginning of the game.
cells = list("         ")
display_grid(cells)

# 2. Creates a game loop where the program asks the user to enter the cell coordinates,
# analyzes the move for correctness and shows a grid with the changes if everything is okay.
coord_list = (
    (1, 1), (1, 2), (1, 3),
    (2, 1), (2, 2), (2, 3),
    (3, 1), (3, 2), (3, 3)
    )

count = 1
while True:
    coord = input("Enter the coordinates: ")
    not_nums = [c for c in coord.split() if c.isalpha()]
    if len(not_nums) > 0:
        print('You should enter numbers!')
    else:
        nums = tuple([int(x) for x in coord.split(' ')])
        if ((nums[0] > 3 or nums[1] > 3) or (nums[0] < 1 or nums[1] < 1)) and len(nums) == 2:
            print('Coordinates should be from 1 to 3!')
        else:
            if cells[coord_list.index(nums)] == ' ':
                if count % 2 == 1:
                    cells[coord_list.index(nums)] = 'X'
                else:
                    cells[coord_list.index(nums)] = 'O'
                display_grid(cell=cells)
                status = check_win(cell=cells)
                if status == 4:
                    count += 1
                    continue
                elif status == 1:
                    print("X wins")
                    break
                elif status == 2:
                    print("O wins")
                    break
                elif status == 3:
                    print("Draw")
                    break
                elif status == 0:
                    print("Impossible")
            else:
                print('This cell is occupied! Choose another one!')


