sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
# split = sentence.split() # debug tool
# print(split) # debug tool
result = {word: len(word) for word in sentence.split()}


print(result)

