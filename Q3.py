# Program for entering student details and calculating total, average, and grade

name = input("Enter student name: ")

score1 = int(input("Subject 1 marks = "))
if score1 < 0 or score1 > 100:
    print("Error: Invalid entry")
    exit()

score2 = int(input("Subject 2 marks = "))
if score2 < 0 or score2 > 100:
    print("Error: Invalid entry")
    exit()

score3 = int(input("Subject 3 marks = "))
if score3 < 0 or score3 > 100:
    print("Error: Invalid entry")
    exit()

total_score = score1 + score2 + score3
average_score = total_score / 3

print("\nStudent Name:", name)
print("Total Marks =", total_score)
print("Average Marks =", average_score)

if average_score >= 90:
    print("Grade A awarded")
elif average_score >= 80:
    print("Grade B awarded")
elif average_score >= 70:
    print("Grade C awarded")
elif average_score >= 60:
    print("Grade D awarded")
elif average_score >= 50:
    print("Grade E awarded")
else:
    print("Grade F awarded")
