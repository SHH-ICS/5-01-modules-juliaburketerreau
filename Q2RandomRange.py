# Create a program that accepts 2 numbers from the user. 
# Your program will output a random number between the range given by the user.
import random 
redo = True
while redo:
  a = input( " What is your first number? " )
  b = input( "What is your second number? " )
  try:
    a = float(a)
    b = float(b)
    if a == float and b == float:
        redo = False
  except:
    print("Enter a valid number")
    redo = True
print(random.randint(a,b))