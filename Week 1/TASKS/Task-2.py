c = int(input('How many Student data you want to enter : '))
students=[]
for i in range(c):
    student = {
            'name'  : (input(f'Enter Your Name of Student - {i+1} : ')),
            'age'   : (int(input(f'Enter Your Age of Student - {i+1} : '))),
            'subject': []
          }
    # print('Student details : ',student)
    sub = int(input('Enter Number of Subject : '))
    sum = 0  
    for j in range(sub):
        s = {
                'SubjectName' : (input(f'Enter Name of Subject - {j+1} : ')),
                'SubjectMarks' : (int(input(f'Enter Marks (0-100) of Subject - {j+1} : ')))
            }
        subject = []
        marks = s['SubjectMarks']
        sum =  sum + marks
        name = student['name']
        age = (student['age'])
        subjectName = s['SubjectName']
        subjectMarks = s['SubjectMarks'] 
    print(f'Sum out of {100 * sub} : ',sum)
    def avg():
        avg = sum/sub
        print('Average : ',avg)
    avg()
    grade = sum
    if grade >= 50:
        bool = True
        print(f'{bool} Congratulations, You Have passed the exam')
    else:
        bool = False
        print(f'{bool} Unfortunately, You have failed the exam')
    students.append({
                        'Name' : student['name'],
                        'Age' : student['age'],
                        'Grade' : grade,
                        'Subject Name' : subjectName,
                        'Subject Marks' : subjectMarks
                    })                                                           
for student in students: 
    # for subject in students:
        # print(subject)
    print(student)
