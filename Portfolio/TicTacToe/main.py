# Tic Tac Toe
import os





grid = [['T','A','B','C'],
        ['1', ' ' , ' ' , ' ' ],
        ['2', ' ' , ' ' , ' ' ],
        ['3', ' ' , ' ' , ' ' ],
]
board_map = {
    "A": '1',
    "B": '2',
    "C": '3'
}
def print_grid(grid=grid):
    for line in grid:
        print(line)
## check if win

def win(grid=grid, player='None'):
    # line
    for line in grid:
        if line[1] == line[2] == line[3] == player:
            return True, line[1]
    # cross
    if grid[1][1] == grid[2][2] == grid[3][3] == player:
        return True, line[1]
    elif grid[-2][-2] == grid[-3][-3] == grid[-4][-4] == player:
        return True, line[1]
    for num in range(4):
        if grid[1][num] == grid[2][num] == grid[3][num] == player:
            return True, line[1]
    return False, None

def grid_writer(move="", board_map=board_map, player='player'):
    if move != "":
       col, row = [_ for _ in move]
       grid[int(row)][int(board_map[col])] = player

def game():
    player = "X"
    while True:
        print_grid()

        move = input(f"insert player {player} movement: ")
        grid_writer(move=move, board_map=board_map, player=player)
        status, line = win(grid=grid, player=player)
        if status:
            print_grid()
            print(f'player: {player} Wins')
            break

        if player == "X":
            player = "0"
        else:
            player = "X"
        os.system('cls')
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game()
