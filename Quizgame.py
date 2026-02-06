score = 0

print("Welcome to the Simple Quiz Game!")
print("--------------------------------")

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["A. Python", "B. Java", "C. HTML", "D. C++"],
        "answer": "C"
    },
    {
        "question": "Who developed Python?",
        "options": ["A. Dennis Ritchie", "B. James Gosling", "C. Guido van Rossum", "D. Bjarne Stroustrup"],
        "answer": "C"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. /* */"],
        "answer": "C"
    },
    {   "question": "which keyword is used to take input from user in python?",
         "options": ["A. Input", "B. let", "C. cin>>", "D. printf"],
         "answer": "A"

    }
]

for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong! Correct answer is", q["answer"])

print("\n--------------------------------")
print("Quiz Completed!")
print("Your Score:", score, "/", len(questions))
print("--------------------------------")
