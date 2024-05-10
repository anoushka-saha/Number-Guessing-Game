#Anoushka Saha
#Number Guessing Game
#May 10th, 2024
#Day 12 Final Project

#Import random module
import random

#Generate a random number
answer = random.randint(1,100)

#Testing line
print("The answer is " + str(answer))

#Intro statements
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")

#Ask user what difficulty level they want. 10 guesses for easy, 5 guesses for hard.
level = input("Pick a level. Type \'easy\' or \'hard\': ")

if level == "easy":
    guesses = 10
    user_guesses = 10
elif level == "hard":
    guesses = 5
    user_guesses = 5

#For loop to limit number of times user can guess
i = 0
while i <= guesses:
    print("You have " + str(user_guesses) + " guesses remaining to guess the number.")
    #Ask for user's guess
    user_guess = int(input("Make a guess: "))
    if user_guess != answer:
        i = i + 1
        user_guesses = user_guesses - 1
        if user_guesses == 0:
            print("You're out of guesses. Game over.")
            break
        elif user_guess < answer:
            print("Too low. Guess again")
        elif user_guess > answer:
            print("Too high. Guess again")
    else:
        print("Correct answer!")
        break


