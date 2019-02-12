#!/bin/python3

# Input Format :
# First line contains T that denotes the number of test cases. This is followed by T lines, each containing an integer, N.
#
# Output :
# The sum of all the multiples of 3 or 5 below N.

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    # calculate num of multiple of 3 till given number n
    numOfThreeMultiple = n//3
    if n%3 == 0:
        numOfThreeMultiple -= 1
        
    # calculate num of multiple of 5 till given number n
    numOfFiveMultiple = n//5
    if n%5 == 0:
        numOfFiveMultiple -= 1
        
    # the required sum is individual sum of all multiple of 3 & 5
    reqSum = 3*numOfThreeMultiple*(numOfThreeMultiple+1)//2
    reqSum += 5*numOfFiveMultiple*(numOfFiveMultiple+1)//2
    
    # some values are repeated i.e., all multiples of 15 i.e., 3*5
    # hence subtract from previous result to get final result
    numOfFifteenMultiple = numOfFiveMultiple // 3
    reqSum -= 15*numOfFifteenMultiple*(numOfFifteenMultiple+1)//2
    
    print (reqSum)
