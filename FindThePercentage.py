#https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    try:
        for _ in range(n):
            name, *line = input().split()        
            scores = list(map(float, line))
            student_marks[name] = scores
    except ValueError:
        print(-1)
    query_name = input()
#Prints all the students grades together. Now we just need to add them up.
#print(student_marks[query_name])

sum=0
marksOfStudent = student_marks[query_name]

for i in range (0,3):
    sum += marksOfStudent[i]

average = sum / 3

print(format(average, ".2f"))
