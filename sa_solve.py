from sudoku import *
from random import randint,sample,random
import math
from copy import copy, deepcopy
tried = 0


def random_number(list_left):
    index = randint(0, list_left.__len__() - 1)
    return str(list_left.pop(index))


def random_col_pair(col_list):
    index = randint(0,col_list.__len__() - 1)
    index = sample(range(0,col_list.__len__()),2)
    return [col_list[index[0]],col_list[index[1]]]


def remain_num_row(table,row_number):
    remain_num_list = []
    mem_not_use_num = [True]*9
    row_list = table[row_number]
    for i in row_list:
        if i is not '0':
            mem_not_use_num[int(i) - 1] = False
    for i in range(0, 9):
        if mem_not_use_num[i]:
            remain_num_list.append(i+1)
    return remain_num_list


def create_nonfix_list(init_table):
    list = []
    for i in range(0,9):
        temp_list = []
        for j in range(0,9):
            if init_table[i][j] == '0':
                temp_list.append(j)  # append column.
        if temp_list.__len__() is 1:  # fill immediately if remain one void slot.
            num = remain_num_row(init_table, i)
            init_table[i][temp_list[0]] = str(num[0])
            temp_list = []
        list.append(temp_list)
    return list


def fill_rand_table(table, empty_list):
    copied_table = deepcopy(table)
    for row_index in range(0, empty_list.__len__()):
        empty_row_list = empty_list[row_index]
        num_remain = remain_num_row(table,row_index)
        for i in empty_row_list:
            copied_table[row_index][i] = random_number(num_remain)
    return copied_table


def cal_score(table):
    score = 0
    for i in range(0, 9):
        for j in range(0, 9):
            score += 1 if check_block(table, i, j) else 0
            score += 1 if check_col(table, i, j) else 0
    return score


def make_some_change(table, empty_list):
    new_table = deepcopy(table)
    row_index = randint(0, 8)
    while empty_list[row_index].__len__() is 0:
        # print("oop random complete row")
        row_index = randint(0, 8)
    pair_col_index = random_col_pair(empty_list[row_index])  #arr size 2
    # swap
    temp = new_table[row_index][pair_col_index[0]]
    new_table[row_index][pair_col_index[0]] = new_table[row_index][pair_col_index[1]]
    new_table[row_index][pair_col_index[1]] = temp
    return new_table


def sa_solve(table):
    count = 0
    t = 0.5   # temperature
    nonfix_point_map = create_nonfix_list(table)  # false mean not fix.
    print(nonfix_point_map)
    filled_table = fill_rand_table(table,nonfix_point_map)
    print(filled_table)
    best_score = cal_score(filled_table)
    while (t > 0) and (best_score is not 162):
        t = 0.99999 * t
        count += 1
        next_stage = make_some_change(filled_table,nonfix_point_map)
        score = cal_score(next_stage)
        if count % 1000 is 0:
            print("^"*20)
            print("round ",end='')
            print(count)
            print("score is ", end='')
            print(score, end=' ')
            print("best score is ", end='')
            print(best_score)
            print("t ",end='')
            print(t)
        if score > best_score:
            best_score = score
            filled_table = next_stage
        elif random() < math.exp( -1*(float((best_score - score)/t))):
            best_score = score
            filled_table = next_stage
        if count % 20000 == 0:
            print("*************reset************")
            t = 0.5
            filled_table = fill_rand_table(table, nonfix_point_map)
            best_score = 0
    print("done at round",end="")
    print(count)
    return filled_table




