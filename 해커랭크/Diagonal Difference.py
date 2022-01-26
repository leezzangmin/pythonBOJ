#!/bin/python3

import math
import os
import random
import re
import sys;input=sys.stdin.readline
#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    left=0
    right=-1
    left_ans=0
    right_ans=0
    for i in arr:
        left_ans+=i[left]
        right_ans+=i[right]
        left+=1;right-=1
    
    return abs(left_ans-right_ans)

    # Write your code here

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().rstrip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
 #   fptr.write(str(result) + '\n')

   # fptr.close()
