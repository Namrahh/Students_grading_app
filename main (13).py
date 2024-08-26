# Class Grading

# Get the exam score from the user
score = int(input("What is your exam score? (out of 100): "))

# Determine the grade based on the score
if score < 0 or score > 100:
    print("Invalid score. Please enter a score between 0 and 100.")
else:
    if score >= 90:
        grade = 'A'
        feedback = "Excellent! You've earned an A."
    elif score >= 80:
        grade = 'B'
        feedback = "Well done! You've earned a B."
    elif score >= 70:
        grade = 'C'
        feedback = "Good job! You've earned a C."
    elif score >= 60:
        grade = 'D'
        feedback = "You've earned a D. Keep pushing!"
    else:
        grade = 'F'
        feedback = "Unfortunately, you've earned an F. Don't lose heart, try again."

    # Print the grade and feedback
    print(f"Your grade is {grade}. {feedback}")