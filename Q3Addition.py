# Create a program that will ask the user an addition question. 
# The program will generate two random numbers between 1 and 100, and display them as an addition question with appropriate prompts.
import random
a = int(random.randint(1,100))
b = int(random.randint(1,100))
print("What is the answer to", a , "+" , b)
redo = True
while redo:
    num = int(a + b)
    ans = int(input( " What is your answer? " ))
    if ans == num:
          print("That's right!")
          redo = False
    else:
            print("Try again!")
    
