#!/bin/python3
from functools import reduce
import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
        return reduce((lambda x,y: x+y), ar)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
