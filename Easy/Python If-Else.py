#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if n%2!=0:
    print("Weird")
else:
    if (n==2 or n==4):
        print("Not Weird")   
    elif (n>=6 and n<=20):
        print("Weird") 
    elif(n>20 and n<=100):
        print("Not Weird")    
