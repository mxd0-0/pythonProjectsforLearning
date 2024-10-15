def grade_checker(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


score = input("Enter the student's score (0-100): ")

if score.isdigit():
    score = int(score)
    if 0 <= score <= 100:
        grade = grade_checker(score)
        print(f"The grade is: {grade}")
    else:
        print("Please enter a valid score between 0 and 100.")
else:
    print("Invalid input. Please enter a numeric value.")
