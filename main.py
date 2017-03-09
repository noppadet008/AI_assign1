from sudoku import *
from copy import copy, deepcopy
import time
start_time = time.time()
tried = 0

def counted(f):
    def wrapped(*args, **kwargs):
        wrapped.calls += 1
        return f(*args, **kwargs)
    wrapped.calls = 0
    return wrapped

@counted
def solving(position_x, position_y, table):
    global tried
    for i in range(1, 10):
        clone_table = deepcopy(table)
        clone_table[position_y][position_x] = str(i)
        print("edit position(" + str(position_x) + "," + str(position_y) + ") with value" + str(i))
        tried += 1
        log_table(clone_table,False)
        if check_table(clone_table, position_x, position_y):
            temp_position = find_next(position_x, position_y, clone_table)
            print(temp_position)
            solving(temp_position[0], temp_position[1], clone_table)
            print("back to ",end="")
            print(temp_position)


def find_next(position_x, position_y, table):
    if not valid_position(position_x, position_y):
        return
    while 1:
        print(str(position_x) + str(position_y)) #finding void path
        if position_x == 0 and position_y == 9:
            print("done result\n\n")
            print_table(table)
            print("called function solving "+str(solving.calls)+" time")
            print("try  "+str(tried)+" time")
            print("using --- %s seconds ---" % (time.time() - start_time))
            quit()
        elif table[position_y][position_x] != "0":
            if position_x == 8:
                position_y += 1
                position_x = 0
            else:
                position_x += 1
        else:
            return [position_x, position_y]


data = import_file()
print("start")
print_table(data)
print()
log_table(data,True)
position = find_next(0, 0, data)
solving(position_x=position[0], position_y=position[1], table=data)

