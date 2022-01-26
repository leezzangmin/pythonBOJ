# https://inpa.tistory.com/348 // 키 바인딩

#!/bin/python3

# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    ans=""
    if s[-2:] == "AM":
        if int(s[0:2])>=12:
            ans+='00'+s[2:8]
        else:               # 여기 빼먹어서 한번 틀림
            ans+=s[0:8]
            
    else: # "PM"
        if int(s[0:2])==12:
            ans+=s[0:8]
        else:
            ans+=str(int(s[0:2])+12)+s[2:8]


    return ans


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    print(result)
   # fptr.write(result + '\n')

    #fptr.close()
