#!/bin/python

from __future__ import print_function

import os
import sys


def miniMaxSum(arr):
    lsum = sum(arr)
    a = max(arr)
    b = min(arr)
    return print(lsum-a,lsum-b)
if __name__ == '__main__':
    arr = map(int, input().rstrip().split())
    arr = sorted(arr)
    miniMaxSum(arr)
