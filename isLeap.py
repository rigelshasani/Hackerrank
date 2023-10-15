#Link: https://www.hackerrank.com/challenges/write-a-function/problem
#Is a given year a lap year?

def is_leap(year):
    leap = False
     
    if(year % 4 == 0):
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True    
        else:
            leap = True
    return leap

year = int(input())
