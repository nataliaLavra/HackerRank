#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
   
    reverse = []
    for i in arr:
        reverse.append(arr[n-1])
        n-=1
    print(*reverse)
        
