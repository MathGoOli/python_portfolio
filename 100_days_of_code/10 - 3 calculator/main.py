


#Add function
def add(n1,n2):
  return n1 + n2
#subtraction
def subtraction(n1,n2):
  return n1 - n2
#multiplication
def multiplication(n1,n2):
  return n1 * n2
#division
def division(n1,n2):
  return n1 / n2
#dictionary without "".example: add, not "add"
operations = {
"+":add,
"-":subtraction,
"*":multiplication,
"/":division,
}

def calculator():

  import art
  print(art.logo)

  num1 = float(input("what's the first number? "))
  stop = False
  while stop != True:
    for sym in operations:
      print(sym)
    operation_symbol = input("pick an operation from the line above:" )
    num2 = float(input("what's the next number? "))
    calculation_function = operations[operation_symbol]
    #print(calculation_function) #debug tool
    answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    #end loop lool

    quest_loop = input(f"do you wish to continue calculatin with: {answer} ? Y or N: ").lower()
  # print(f"quest loop is {quest_loop}") #debug tool
    if quest_loop == "n":
      stop = True
      calculator()
    elif quest_loop == "y":
      num1 = answer
calculator()