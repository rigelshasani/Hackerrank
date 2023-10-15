#https://www.hackerrank.com/challenges/nested-list/problem

#cat <inputfilename> | <python run command>
#to run challenges with input files

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        #get the students from the input and place them in the lists
        students.append([name, score])
    
    #create empty lists
    names = []
    scores  = []
    #add as appropriate to each
    for i in range(len(students)):
        names.append(students[i][0])
        scores.append(students[i][1])

    #go through the scores list and find out which is second lowest
    
    #sort the scores
    scores.sort()
    #keep looping until you find a number that's different
    second = -1
    for i in range(0, len(scores)):
        if scores[i] == scores[0]:
            pass
        else:
            second = scores[i]
            break
    studentsGpa = []
    for i in range(0, len(students)):
        if students[i][1] == second:
            studentsGpa.append(students[i][0])
    studentsGpa.sort()
    for i in studentsGpa:
        print(i)
            
