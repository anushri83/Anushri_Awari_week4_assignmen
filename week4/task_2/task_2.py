
# Create a script that processes a CSV file containing student grades and calculates the
# average grade for each student.

import csv  
def average_grades(input_csv):

    try:
        with open(input_csv, 'r') as file:   # open and read from file
            content = csv.reader(file)  
            header = next(content)     #read and skips header(attributes)

            students = []  #list to store name and average of student
            for row in content:
                name = row[0]
                grades = list(map(int, row[1:]))  # Convert grades to integers
                average = sum(grades) / len(grades)
                students.append([name, average])

            print("name : average")
            for n,a in students:
                print(n,":",f"{a:.2f}")     #print name and average 
    
    except FileNotFoundError:      #error
        print(f"{input_csv} not found ")

input=r"C:\Users\admin\Downloads\python\cogitix\week4\task_2\student.csv"   #input file address
average_grades(input)