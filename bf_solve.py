from sudoku import *
from copy import copy, deepcopy
tried = 0

def counted(f):
    def wrapped(*args, **kwargs):
        wrapped.calls += 1
        return f(*args, **kwargs)
    wrapped.calls = 0
    return wrapped



def find_next(position_x, position_y, table):
    if not valid_position(position_x, position_y):
        return
    while 1:
        # print(str(position_x) + str(position_y)) #finding void path
        if position_x == 0 and position_y == 9:
            return False
        elif table[position_y][position_x] != "0":
            if position_x == 8:
                position_y += 1
                position_x = 0
            else:
                position_x += 1
        else:
            return [position_x, position_y]


@counted
def solving(position_x, position_y, table):
    global tried
    for i in range(1, 10): # tried number 1 to 9
        tried += 1
        clone_table = deepcopy(table)
        clone_table[position_y][position_x] = str(i)
        print("edit position(" + str(position_x) + "," + str(position_y) + ") with value" + str(i))
        # log_table(clone_table,False)
        if check_table(clone_table, position_x, position_y):
            temp_position = find_next(position_x, position_y, clone_table)
            if not temp_position: #pass by ref
                table = clone_table
                return 1
            print(temp_position)
            if solving(temp_position[0], temp_position[1], clone_table):
                table = clone_table
                return 1
            print("back to ",end="")
            print(temp_position)
    return 0


