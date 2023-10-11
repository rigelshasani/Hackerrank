# List Comprehension Alternative Solution
# ---------------------------------------------------------------------------------------------
# list = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if(i+j+k != n)]
#     print(list)
# ---------------------------------------------------------------------------------------------
# two lines..i did it in like 20 in my OC solution.

#-------------------------------
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    list = []
    smallList = []
    for i in range(x+1):                  #repeats twice
        #print(i)                  
        for j in range(y+1):              #repeats twice
            #print(j)
            for k in range(z+1):          #repeats twice  #all repeats 2**3=8 times
                #print(k)
                if(i+j+k != n):
                    smallList.append(i)
                    smallList.append(j)
                    smallList.append(k)
                else:
                    pass
    #print(smallList)
    #print(len(smallList))
    while(len(smallList)> 0):
        group = []
        for i in range(3):
            if smallList:
                group.append(smallList.pop(0))
        list.append(group)
        
    print(list)
#-------------------------------
