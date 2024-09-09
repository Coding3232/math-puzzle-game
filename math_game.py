import random
import time

def generate_question():
    """Generates a random math question and returns the question as a string and the answer."""
    operators = ['+', '-', '*']
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(operators)
    
    question = f"{num1} {operator} {num2}"
    answer = eval(question)  # Calculate the correct answer
    return question, answer

def play_game():
    """Main function to play the math puzzle game."""
    print("Welcome to the Math Puzzle Game!")
    time.sleep(1)
    
    score = 0
    total_questions = 10
    time_limit = 10  # seconds
    
    for i in range(total_questions):
        question, correct_answer = generate_question()
        print(f"Question {i+1}: What is {question}?")
        
        start_time = time.time()
        
        try:
            user_answer = int(input(f"You have {time_limit} seconds. Your answer: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        elapsed_time = time.time() - start_time
        
        if elapsed_time > time_limit:
            print("Time's up!")
        elif user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {correct_answer}.")
        
        time.sleep(1)
    
    print(f"Game Over! Your final score is: {score}/{total_questions}")
    
    new_game = input("Do you want to play again? (yes/no): ").lower()
    if new_game == 'yes':
        play_game()
    else:
        print("Thanks for playing!")

# Run the game
if __name__ == "__main__":
    play_game()
