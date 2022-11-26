#Write your code below this line 👇
def prime_checker(number):
  
  count = 3
  if number == 1:
    print("It's a prime number.")
  elif number == 2:
    print("It's a prime number.")
  elif number == 3:
    print("It's a prime number.")
  elif number % 2 == 0:
    print("It's not a prime number. because is divisible by 2")
  else:
    while True:
      count += 2
      if count == number:
        print(f"It's a prime number.")
        break
      elif number % count == 0:
        print(f"it's not a prime number.because is divisible by {count}")
        break
      


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



