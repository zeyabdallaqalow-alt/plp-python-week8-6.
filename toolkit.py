
import random

# Number Guessing Game
def guessing_game():
    secret_number = random.randint(1, 10)
    print("\nWelcome to the Number Guessing Game!")
    print("Guess a number between 1 and 10.")

    while True:
        guess = int(input("Enter your guess: "))

        if guess == secret_number:
            print(f"Congratulations! You guessed {secret_number} correctly!")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")


# To-Do List
def todo_list():
    tasks = []

    while True:
        print("\n--- To-Do List ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter your task: ")
            tasks.append(task)
            print(f"Task '{task}' added successfully!")

        elif choice == "2":
            if tasks:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")
            else:
                print("Your to-do list is empty.")

        elif choice == "3":
            if tasks:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")
                try:
                    number = int(input("Enter task number to remove: "))
                    if 1 <= number <= len(tasks):
                        removed = tasks.pop(number - 1)
                        print(f"Removed: {removed}")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("There are no tasks to remove.")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please try again.")


# Simple Calculator
def calculator():
    print("\n--- Simple Calculator ---")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("Choose an operation: +, -, *, /")
        operation = input("Enter operation: ")

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("Cannot divide by zero.")
                return
            result = num1 / num2
        else:
            print("Invalid operation.")
            return

        print(f"The answer is: {result}")

    except ValueError:
        print("Please enter valid numbers.")


# Main menu loop
print("Welcome to My Python Toolkit!")

while True:
    print("\nChoose a tool:")
    print("1. Number Guessing Game")
    print("2. To-Do List")
    print("3. Simple Calculator")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        guessing_game()
    elif choice == "2":
        todo_list()
    elif choice == "3":
        calculator()
    elif choice == "4":
        print("Thank you for using My Python Toolkit. Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1, 2, 3 or 4.")
