#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n,m=map(int,input().split())
    arr=[]
    for i in range(n):
        arr.append(list(map(int,input().rstrip().split())))
    k=int(input())
    [print(*i) for i in sorted(arr,key=lambda attribute:attribute[k])]
