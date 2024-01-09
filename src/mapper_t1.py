#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys
with sys.stdin as f:
    for x in f.read().splitlines():
        a = x.split()
        if (len(a) == 2):
            print(a[0], a[1], sep=",")
