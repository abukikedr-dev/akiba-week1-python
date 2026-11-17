# Collect information from the user
student_name = input("Enter Student Name: ")
student_id = input("Enter Student ID: ")
department = input("Enter Department: ")
year = int(input("Enter Year: "))
university = input("Enter University: ")
phone_number = input("Enter Phone Number: ")

# Display the Student ID Card
print("\n+--------------------------------+")
print("|       AKIBA STUDENT CARD       |")
print("+--------------------------------+")
print(f"| Name: {student_name} |")
print(f"| ID: {student_id} |")
print(f"| Department: {department} |")
print(f"| Year: {year} |")
print(f"| University: {university} |")
print(f"| Phone: {phone_number} |")
print("+--------------------------------+")