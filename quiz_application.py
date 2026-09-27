questions = {
    "Capital of India?": "Delhi",
    "2 + 2 = ?": "4",
    "Python is a language?": "Yes"
}

score = 0

for question, answer in questions.items():
    user = input(question + " ")
    if user.lower() == answer.lower():
        score += 1

print("Final Score:", score)
