#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def pickingNumbers(a):
    a.sort()

    max_subarr_size = -1
    current_subarr_size = 1
    stand = a[0]
    for e in a[1:]:
        if e - stand <= 1:
            current_subarr_size += 1
        else:
            max_subarr_size = max(max_subarr_size, current_subarr_size)
            current_subarr_size = 1
            stand = e

    return max(max_subarr_size, current_subarr_size)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
