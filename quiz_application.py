questions = [
    ("What is the capital of India?", "Delhi"),
    ("Which language is used for AI and Data Science?", "Python"),
    ("How many continents are there?", "7"),
    ("What is 5 * 6?", "30"),
    ("What is the largest planet in our Solar System?", "Jupiter")
]

score = 0

print("===== QUIZ GAME =====")

for question, correct_answer in questions:
    user_answer = input(question + " ")

    if user_answer.strip().lower() == correct_answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong! Correct answer is:", correct_answer)

    print()

print("===== QUIZ COMPLETED =====")
print("Your Score:", score, "/", len(questions))

percentage = (score / len(questions)) * 100
print("Percentage:", percentage, "%")

if percentage >= 80:
    print("Grade: A")
elif percentage >= 60:
    print("Grade: B")
elif percentage >= 40:
    print("Grade: C")
else:
    print("Grade: Fail")

input("\nPress Enter to exit...")
