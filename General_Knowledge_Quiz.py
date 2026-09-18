Questions = [
    {
        "questions" : "Which architectural marvel hides a secret private apartment at its peak?",
        "answer" : "Eiffel Tower"
    },
    {
        "questions" : "Which ancient wonder travels four centimeters every year on a tectonic plate?",
        "answer" : "Giza Pyramids"
    },
    {
        "questions" : "What was the first fruit harvested by gravity's absence and tested in space?",
        "answer" : "Apple"
    },
    {
        "questions" : "Which island nation invites you to dive down to mail a letter?",
        "answer" : "Vanuatu"
    },
    {
        "questions" : "Which bizarre, egg-laying creature evolved to digest its food without a stomach?",
        "answer" : "Platypus"
    },
]

def sanitization(text):
    return text.strip().lower()

def ask_question(question_data, number, total):
    print(f"\nQuestion {number}/{total} : {question_data['questions']}")
    answer = input("Your answer: ")

    user_answer = sanitization(answer)
    correct_answer = sanitization(question_data['answer'])

    if user_answer == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"Incorrect! The correct answer is: {question_data['answer']}")
        return False

def quiz():
    print("General Knowledge Quiz")
    print(f"You will be asked {len(Questions)} questions. Try to answer them correctly!\n")

    score = 0
    total = len(Questions)

    for i, question_data in enumerate(Questions, start=1):
        if ask_question(question_data, i, total):
            score += 1

    display_results(score, total)

def display_results(score, total):
    percentage = (score / total) * 100

    print("Final Score")
    print(f"You scored {score:>2} out of {total} ({percentage:.0f}%)")

    if percentage == 100:
        print("Excellent! You got a perfect score!")
    elif percentage >= 70:
        print("Great job!")
    elif percentage >= 40:
        print("Not bad, but there's room for improvement.")
    else:
        print("Better luck next time! Keep learning and trying!")

if __name__ == "__main__":
    quiz()
    