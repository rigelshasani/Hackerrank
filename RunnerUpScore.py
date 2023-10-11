if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

#to run it on my vscode i had to change lines 2 & 3 to the following:
    #n = 5
    #arr = [2,3,6,6,5]
    
    def second(arr):
        #Initialize empty array
        array = []
        #for each member of the argument arr
        for i in arr:
            #append each element to the array
            array.append(i)
            
        #sort it in ascending order
        newArray = sorted(array)
        #print(newArray)
        #print(len(newArray))
        for i in range(len(newArray)-1, -1, -1):
            if(newArray[i] == newArray[i-1]):
                pass
            else:
                print(newArray[i-1])
                return
        
    second(arr)

# Unfinished
# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
    
#     def second(arr):
#         array = []
#         for i in arr:
#             array.append(i)
#         newArray = sorted(array)
#         print(newArray)
#         for i in range(len(newArray)-1, 0, -1):
#             #print(newArray[i])
#             if(newArray[i] == newArray[i-1]):
#                 print("Equal: " + str(i))
#             else:
#                 print(i)
        
#     second(arr)
