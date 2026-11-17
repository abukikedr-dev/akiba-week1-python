student_name = input("Enter student name: ")
python_score = float(input("Enter Python score: "))
english_score = float(input("Enter English score: "))
math_score = float(input("Enter Mathematics score: "))

total_score = python_score + english_score + math_score
average_score = total_score / 3

print("============================================")
print("EXAM RESULT REPORT")
print("-----------------------------------------")
print("Student Name: ", student_name)
print("Python Score: ", python_score)
print("English Score: ", english_score)
print("Mathematics Score: ", math_score)
print("-----------------------------------------")
print("Total Score: ", total_score)
print("Average Score: ", round(average_score, 2))
print("=============================================")