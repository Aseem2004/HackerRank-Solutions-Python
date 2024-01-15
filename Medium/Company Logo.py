#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter
if __name__ == '__main__':
    s = sorted(list(input()))
    for x, y in Counter(s).most_common(3):
        print(x, y)