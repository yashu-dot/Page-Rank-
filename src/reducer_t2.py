#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys

final_dict = {}

for line in sys.stdin:
    line = line.strip()
    node1, node2 = line.split(",")
    node3 = float(node2)
    if node1 not in final_dict.keys():
        final_dict[node1] = []
        final_dict[node1].append(node3)
    else:
        final_dict[node1].append(node3)


for x, y in sorted(final_dict.items()):
    count = float(0)
    y.sort()
    for i in y:
        count = count+float(i)
    y = 0.15+0.85*(count)
    print("%s,%.5f" % (x, y))
