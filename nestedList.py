if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        
    num1 = float(100)
    num2 = float(100)

    for i in range(len(students)):
        if students[i][1] < num1:
            num2, num1 = num1, students[i][1]
        elif students[i][1] < num2 and students[i][1] != num1:    
            num2 = students[i][1]

    students.sort()

    for st in students:
        if st[1] == num2:
            print(st[0])        

        
