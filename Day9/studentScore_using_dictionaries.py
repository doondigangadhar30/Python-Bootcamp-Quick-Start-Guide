student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
 
student_grades = {}

for key in student_scores:
 
    score = student_scores[key]
 
    if score >= 91:
        student_grades[key] = 'Outstanding'
    elif score >= 81:
        student_grades[key] = 'Exceeds Expectations'
    elif score >= 71:
        student_grades[key] = 'Acceptable'
    else:
        student_grades[key] = 'Fail'