#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys
import ast

filev = sys.argv[1]
nodes_all = {}

v_file = open(filev, "r")
for line in v_file:
    node, rank = line.split(",")
    nodes_all[node] = float(rank)
v_file.close()


for lines in sys.stdin:
    lines = lines.strip()
    fnode, y = lines.split("\t")
    tlist = ast.literal_eval(y)
    n = len(tlist)
    for i in tlist:
        val = float((1/n)*nodes_all[fnode])
        if str(i) in nodes_all:
            print("%s,%f" % (i, val))
    print(fnode, 0, sep=",")
