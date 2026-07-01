student_results = [
    {
        "name": "Miftahul Islam",
        "gpa": 5
    },
    {
        "name": "Ashraful Islam",
        "gpa": 4.8
    },
    {
        "name": "Jamilur Rahman",
        "gpa": 4.25
    },
    {
        "name": "Masud Rana",
        "gpa": 3.9
    },
    {
        "name": "Jalal Uddin",
        "gpa": 5
    },
    {
        "name": "Anik Ahmed",
        "gpa": 4.75
    },
    {
        "name": "Karim Sheikh",
        "gpa": 3.5
    },
    {
        "name": "Rahim Sheikh",
        "gpa": 4.95
    },
    {
        "name": "Sabbir Rahman",
        "gpa": 4.0
    },
    {
        "name": "Karim Sheikh",
        "gpa": 3.5
    },
    {
        "name": "Rahim Sheikh",
        "gpa": 4.95
    },
    {
        "name": "Sabbir Rahman",
        "gpa": 4.0
    },
    {
        "name": "Karim Sheikh",
        "gpa": 3.5
    },
    {
        "name": "Rahim Sheikh",
        "gpa": 4.95
    },
    {
        "name": "Sabbir Rahman",
        "gpa": 4.0
    },
    {
        "name": "Karim Sheikh",
        "gpa": 3.5
    },
    {
        "name": "Rahim Sheikh",
        "gpa": 4.95
    },
    {
        "name": "Sabbir Rahman",
        "gpa": 4.0
    }
]

def filter_gpa_5(student_result):
    return student_result["gpa"] >= 4

gpa_5_students = list(filter(filter_gpa_5, student_results))

for student in gpa_5_students:
    print(f"{student["name"]}")