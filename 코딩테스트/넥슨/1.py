#!/bin/python3




#
# Complete the 'minNum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER samDaily
#  2. INTEGER kellyDaily
#  3. INTEGER difference
#


# 샘이 켈리보다 diffrence만큼 많이 풀었음
# s = 5 k = 


def minNum(samDaily, kellyDaily, difference):
    if samDaily>kellyDaily:
        return -1
    

    sam=difference
    kelly=0

    tol=0
    
    while sam>=kelly:
        print(sam,kelly,'sk')
        if tol>1000000:
            return -1
        sam+=samDaily
        kelly+=kellyDaily
        tol+=1
    return tol

