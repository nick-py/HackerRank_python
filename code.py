#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    count_a = count_b = 0
    for i,j in enumerate(a):
        if(j == b[i]):
            pass
        elif (j<b[i]):
            count_b = count_b + 1
        elif (j>b[i]):
            count_a = count_a + 1
    return '{}{}'.format(count_a, count_b)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
