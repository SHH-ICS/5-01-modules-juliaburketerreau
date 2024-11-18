# Create a program that will ask the user an addition question. 
# The program will generate two random numbers between 1 and 100, and display them as an addition question with appropriate prompts.
import random
a = random.randint(1,100)
b = random.randint(1,100)
print("What is the answer to", a , "+" , b)
ans = input()
if ans == a + b:
    print("That is correct!")
else:
    print("Try again...")