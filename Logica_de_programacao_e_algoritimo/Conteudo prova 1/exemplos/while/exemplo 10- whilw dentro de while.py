# -*- coding: UTF-8 -*-

tabuada = 1

while tabuada <= 10:
    n = 0
    print("Tabuada %d " % tabuada)
    while n <= 10:
        print("%d * %d = %d" % (tabuada, n, tabuada * n))
        n = n + 1
    tabuada = tabuada + 1
