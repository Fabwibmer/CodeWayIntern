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
    {
        "text":"What is the largest living structure on Earth?",
        "choices": ["Great Barrier Reef" , "Amazon Rainforest" , "Sahara Desert", "Antarctic Ice Sheet"],
        "answer": "Great Barrier Reef"
    }
    
]

import random
def quiz():
    for question in questions:
        random.shuffle(question["choices"])

    score = 0

    for question in questions:
        print(question["text"])
        for i, choice in enumerate(question["choices"]):
            print(f"{i + 1}. {choice}")

   
        while True:
            try:
                answer = int(input("Enter your answer (1-" + str(len(question["choices"])) + "): ")) - 1
                break
            except ValueError:
                print("Invalid input. Please enter a number from 1 to " + str(len(question["choices"])) + ".")

        if question["choices"][answer] == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is " + question["answer"])

    
    print("Your final score is " + str(score) + " out of " + str(len(questions)) + ".")
    print("Thanks for playing!")

    # Ask the user if they want to play again.
    
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        score = 0
        quiz()
    elif play_again.lower() == "no":
        print("Okay, see you next time!")
        
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
    
if __name__ == "__main__":
    quiz()