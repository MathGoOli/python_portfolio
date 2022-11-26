from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
stop_program = False
bidprice = {}

while stop_program == False:

  name = input(f"Welcome to blind audiction program!\nplease insert your name: \n")
  bid = float(input(f"please insert your bid: \n"))


  bidprice[bid] = name
  stop_q = ""

  stop_q = input('do you want stop? yes or no ')
  if stop_q == "yes":
    stop_program = True
  clear()

#print(bidprice) #debug tool

winner = max(bidprice)
print(logo)
print(f'{bidprice[winner]} is the winner with a {winner}$ bid')