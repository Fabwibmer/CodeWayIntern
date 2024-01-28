# A list of questions, where each question is a dictionary containing the question text,
# a list of answer choices, and the correct answer.
questions = [
    {
        "text": "What is the capital of France?",
        "choices": ["Paris", "Berlin", "Madrid", "Rome"],
        "answer": "Paris"
    },
    {
        "text": "What is the largest ocean?",
        "choices": ["Atlantic", "Pacific", "Indian", "Southern"],
        "answer": "Pacific"
    },
    # Add more questions here
]

# Shuffle the order of the answer choices for each question.
import random
def quiz():
    for question in questions:
        random.shuffle(question["choices"])

    # Keep track of the user's score.
    score = 0

    # Loop through the questions.
    for question in questions:
        # Display the question and the shuffled answer choices.
        print(question["text"])
        for i, choice in enumerate(question["choices"]):
            print(f"{i + 1}. {choice}")

        # Get the user's answer.
        while True:
            try:
                answer = int(input("Enter your answer (1-" + str(len(question["choices"])) + "): ")) - 1
                break
            except ValueError:
                print("Invalid input. Please enter a number from 1 to " + str(len(question["choices"])) + ".")

        # Compare the user's answer to the correct answer.
        if question["choices"][answer] == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is " + question["answer"])

    # Display the user's final score and a message thanking them for playing.
    print("Your final score is " + str(score) + " out of " + str(len(questions)) + ".")
    print("Thanks for playing!")

    # Ask the user if they want to play again.
    
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        # Reset the score and shuffle the answer choices again.
        score = 0
        quiz()
    elif play_again.lower() == "no":
        print("Okay, see you next time!")
        
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
    
if __name__ == "__main__":
    quiz()