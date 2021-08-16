import random
names = ["Harshit", "Shivam", "Mayank", "Aditya", "Sonu"]
student_scores = {student:random.randint(40, 100) for student in names}
print(student_scores)

passed_students = {student:score for (student, score) in student_scores.items() if score > 50}
print(passed_students)