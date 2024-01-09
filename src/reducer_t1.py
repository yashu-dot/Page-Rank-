#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys
v_f = sys.argv[1]
data_all = {}


def create_data(x, y):
    if x not in data_all.keys():
        data_all[x] = set()
        data_all[x].add(y)
    else:
        data_all[x].add(y)


with sys.stdin as f:
    for line in f:
        line = line.strip()
        a, b = line.split(",")
        create_data(a, b)


def get_y(li):
    li = list(li)
    li.sort()
    B_list = []
    for i in li:
        if i.isnumeric():
            B_list.append(int(i))
        else:
            B_list.append(i)
    return B_list


vf = open(v_f, "w")
for d, e in sorted(data_all.items()):
    print(d, get_y(e), sep="\t")
    vf.write("%s,%d\n" % (d, 1))
vf.close()
