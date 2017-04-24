from bf_solve import *
from sa_solve import *
import time


data = import_file()
print("start")
print_table(data)
print()
# log_table(data,True)
start_time = time.time()
print(create_nonfix_list(data))
print("_"*20)
print(remain_num_row(data, 3))
# emp_list = create_nonfix_list(data)
# table = fill_rand_table(data,emp_list)
done_table = sa_solve(data)
print("done result\n\n")
print_table(done_table)
for i in range(0,9):
    for j in range(0,9):
        if check_table(done_table,i,j):
            print("ok")
        else:
            print('fail')
# print("called function solving "+str(solving.calls)+" time")
# print("try  "+str(tried)+" time")
print("using --- %s seconds ---" % (time.time() - start_time))
