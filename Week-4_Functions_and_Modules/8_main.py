import os
import csv

file_path = 'student_marks.csv'

if not os.path.exists(file_path):
    print(f"Error: {file_path} does not exist.")
    exit(1)

student_marks = []
student_names = []

with open(file_path, 'r') as data:
    reader = csv.reader(data)
    next(reader)  # Skip the header row
    for row in reader:
        student_names.append(row[0])
        student_marks.append(int(row[1]))
avg_score = sum(student_marks) / len(student_marks)
max_score = max(student_marks)
max_score_index = student_marks.index(max_score)
topper = student_names[max_score_index]

print("Average score:", avg_score)
print("Topper of the class :\n",topper, "with a score of", max_score)