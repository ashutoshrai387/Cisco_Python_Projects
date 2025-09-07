# Student Grades and Courses

# 1. nested dictionary containing student details
students = {
    "Ashutosh": {
        "Math": 10,
        "Science": 10
    },
    "Aryan": {
        "Math": 7,
        "Science": 6
    },
    "Aakash": {
        "Math": 8,
        "Science": 9
    }
}


# 2. print the students dictionary
print(students)

# 3. Iterate through the students dictionary and print each student's name and their average grade across all courses
for k,v in students.items():
    avg = sum(v.values())/len(v)
    print(k," : ",avg)

# 4. Add a new course and grade for one of the existing students.
students["Ashutosh"]["English"] = 9
print(students)