from readSudoku import *

data = import_file()
print_table(data)
for i in range(0, 9):
    for j in range(0, 9):
        print(str(i)+"+"+str(j),end=" => ")
        print(check_table(data,i,i))