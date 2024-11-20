# Create a program that accepts 2 numbers from the user. 
# Your program will output a random number between the range given by the user.
import random 
redo = True
while redo:
  a = input( " What is your first number? " )
  b = input( "What is your second number? " )
  try:
    a = int(a)
    b = int(b)
    redo = False
  except:
    print("Please enter a valid number")
    redo = True
if a > b: 
  print(random.randint(a,b)) 
else:
  print(random.randint(b,a))
