import random

print("Welcome to the game!")
secret_number = random.randint(1, 10)
attempts = 3
while attempts > 0:
    print(f"Attempts: {attempts}")
    ## Переменные:

    user_number = int(input("Enter the number: "))

    if secret_number > user_number:
        print("The secret number is bigger!")
        attempts = attempts - 1
    if secret_number < user_number:
        print("The secret number is less!")
        attempts = attempts - 1
    if secret_number == user_number:
        print("Your number is right...")
        break
if attempts == 0:
    print("Your are lose, right number is: " + str(secret_number))

