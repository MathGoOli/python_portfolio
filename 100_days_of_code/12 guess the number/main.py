#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo
is_game_over = False

def difficulty():
  dif = input(f"choose your difficulty: easy or hard:\n ")
  if dif == "easy":
    return 10
  elif dif == "hard":
    return 5
  else:
    difficulty()

def choose_number():
  return int(random.choice(range(1,101)))

def gameplay(difficulty,number):
  number_of_tries = difficulty
  count = 1
  for _ in range(1, number_of_tries + 1):
    num = int(input("Quess a number: "))

    if num > number:
      print("your number is too hight")
    elif num < number:
      print("your number is too low")
    elif num == number:
      print("you win")
      return
    print(f"you have {number_of_tries - _} left")
    count += 1
  print("you loose")
  return

gameplay(difficulty(),choose_number())