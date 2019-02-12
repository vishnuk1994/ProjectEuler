#!/bin/python3
import sys

# By considering the terms in the Fibonacci sequence whose values do not exceed N, find the sum of the even-valued terms.

# creating dict to store even fib nums, it helps in reducing time at cost of extra space
# by rough estimate; it is better to use space as for high value of n, it will recalculate the series
mapOfEvenFibNum = {0:0,1:2}


# getting nth even fib num.
# formula used is based on the logic that every third element in fibonacci is even
# refer : https://www.geeksforgeeks.org/nth-even-fibonacci-number/
def getEvenFib(n):
    if n in mapOfEvenFibNum:
        return mapOfEvenFibNum[n]
    
    return ( 4* getEvenFib(n-1) + getEvenFib(n-2) ); 

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    count = 1
    reqSum = 0
    num = getEvenFib(count)
    # getting fib num till we reach n
    # updating dict with values
    while num <= n:
        reqSum += num
        mapOfEvenFibNum[count] = num
        count += 1
        num = getEvenFib(count)
    
    print(reqSum)
