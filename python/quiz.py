def welcome():
    print("Welcome to the Python Quiz Game!")
    name = input("Enter your name: ")
    print(f"Good luck, {name}!\n")

def ask_question(question, options, answer):
    print(question)
    for key, value in options.items():
        print(f"{key}: {value}")
    choice = input("Your answer: ").strip().upper()
    return choice == answer

def main():
    score = 0
    questions = [
        {
            "q": "What is the output of 2**3?",
            "options": {"A": "6", "B": "8", "C": "9", "D": "10"},
            "ans": "B"
        },
        {
            "q": "Which keyword is used to define a function in Python?",
            "options": {"A": "def", "B": "function", "C": "fun", "D": "define"},
            "ans": "A"
        },
        {
            "q": "What data type is the result of: 3 / 2?",
            "options": {"A": "int", "B": "float", "C": "str", "D": "bool"},
            "ans": "B"
        },
        {
            "q": "Which of these is a list in Python?",
            "options": {"A": "(1, 2)", "B": "{1:2}", "C": "[1, 2]", "D": "1, 2"},
            "ans": "C"
        }
    ]

    for q in questions:
        if ask_question(q["q"], q["options"], q["ans"]):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['ans']}\n")

    print(f"You got {score} out of {len(questions)} questions right!")

if __name__ == "__main__":
    welcome()
    main()
