# Name: Naina Dhingra
# Roll no.: 2501840022
# Date: 1 November 2025
# Assignment 2
# Building a Student Marks Analyzer

print("---------------------------\n  Students Marks Analyser\n---------------------------")
students = {}  # Dictionary to store data in form {name: marks}

# Data Entry

def enter_marks():
    n = int(input("\nEnter number of students: "))
    for i in range(n):
        name = input(f"Enter name of student {i+1}: ")
        marks = float(input(f"Enter marks for {name}: "))
        students[name] = marks
    print(f"\nstudents data: {students}")

enter_marks()

# Statistical Analysis

if not students:
    print("No data available!")
else:
    scores = list(students.values())        # Extract marks
    top_score = max(scores)                 # Highest mark
    avg_score = sum(scores) / len(scores)   # Average marks
    pass_count = 0
    for m in scores: 
        if m >= 40:
            pass_count = pass_count + 1     # Pass Count
    
    fail_count = len(scores) - pass_count   # Fail Count

    print("\n--- Statistical Analysis ---")
    print(f"Top Score     : {top_score}")
    print(f"Average Score : {avg_score}")
    print(f"Pass Count    : {pass_count}")
    print(f"Fail Count    : {fail_count}")

# Names of Passed and Failed students

passed_students = []
failed_students = []

for name, marks in students.items():
    if marks >= 40:
        passed_students.append(name)
    else:
        failed_students.append(name)

print("\n--- Pass & Fail Summary ---")
print("Passed Students:", passed_students)
print("Failed Students:", failed_students)

# Printing Grades of each student \t{marks}\t{grade}\t{remark}
print("\nName\t   Makrs\t     Grade \t    Status")
print("-----------------------------------------------------")
# Assigning Grades

for name, marks in students.items():
    if marks >= 90:
        grade = "A"

    elif marks >= 80:
        grade = "B"

    elif marks >= 70:
        grade = "C"

    elif marks >= 60:
        grade = "D"
    
    elif marks < 60:
        grade = "F"
    

    if marks >= 40:
        remark = "Pass"
    else:
        remark = "Fail"
    
    print(f"{name}\t    {marks}\t       {grade}\t       {remark}")


# Sample Run 1

'''
---------------------------
  Students Marks Analyser
---------------------------

Enter number of students: 5
Enter name of student 1: Naina
Enter marks for Naina: 25
Enter name of student 2: Ananya
Enter marks for Ananya: 87
Enter name of student 3: Janvi
Enter marks for Janvi: 46
Enter name of student 4: Ira
Enter marks for Ira: 78
Enter name of student 5: Sakshi
Enter marks for Sakshi: 92

students data: {'Naina': 25.0, 'Ananya': 87.0, 'Janvi': 46.0, 'Ira': 78.0, 'Sakshi': 92.0}

--- Statistical Analysis ---
Top Score     : 92.0
Average Score : 65.6
Pass Count    : 4
Fail Count    : 1

--- Pass & Fail Summary ---
Passed Students: ['Ananya', 'Janvi', 'Ira', 'Sakshi']
Failed Students: ['Naina']

Name       Makrs             Grade          Status
-----------------------------------------------------
Naina       25.0               F               Fail
Ananya      87.0               B               Pass
Janvi       46.0               F               Pass
Ira         78.0               C               Pass
Sakshi      92.0               A               Pass'''

# Sample Run 2

'''
---------------------------
  Students Marks Analyser
---------------------------

Enter number of students: 10
Enter name of student 1: khushi
Enter marks for khushi: 80
Enter name of student 2: neelam
Enter marks for neelam: 72
Enter name of student 3: ridhi
Enter marks for ridhi: 82
Enter name of student 4: jannat
Enter marks for jannat: 43
Enter name of student 5: devika
Enter marks for devika: 32
Enter name of student 6: sidhhi
Enter marks for sidhhi: 86
Enter name of student 7: juhi
Enter marks for juhi: 90
Enter name of student 8: riya
Enter marks for riya: 71
Enter name of student 9: dhruvi
Enter marks for dhruvi: 21
Enter name of student 10: jiya
Enter marks for jiya: 42

students data: {'khushi': 80.0, 'neelam': 72.0, 'ridhi': 82.0, 'jannat': 43.0, 'devika': 32.0, 'sidhhi': 86.0, 'juhi': 90.0, 'riya': 71.0, 'dhruvi': 21.0, 'jiya': 42.0}

--- Statistical Analysis ---
Top Score     : 90.0
Average Score : 61.9
Pass Count    : 8
Fail Count    : 2

--- Pass & Fail Summary ---
Passed Students: ['khushi', 'neelam', 'ridhi', 'jannat', 'sidhhi', 'juhi', 'riya', 'jiya']
Failed Students: ['devika', 'dhruvi']

Name       Makrs             Grade          Status
-----------------------------------------------------
khushi      80.0               B               Pass
neelam      72.0               C               Pass
ridhi       82.0               B               Pass
jannat      43.0               F               Pass
devika      32.0               F               Fail
sidhhi      86.0               B               Pass
juhi        90.0               A               Pass
riya        71.0               C               Pass
dhruvi      21.0               F               Fail
jiya        42.0               F               Pass'''
