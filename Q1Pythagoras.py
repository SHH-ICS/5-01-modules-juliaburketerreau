# Create a program that will accept the two legs of a right-angle triangle, a and b, and display the length of the hypotenuse, c. 
# Remember to use prompts for the input and labels for the output. Use the formula a2 + b2 = c2 to calculate your answer.
import math
redo = True
while (redo):
  a = input( "Put in sidelength 1: " )
  b = input( "Put in sidelength 2: " )
  try:
    a = float(a)
    b = float(b)
    if a >= 1 and b >= 1:
        redo = False   
    else:
      a <= 0 and b <= 0
      print("Try again! Both inputs must be a positive number.")
      redo = True    
  except: 
    print("Try again! Both inputs must be a positive number.")
    redo = True
hyp = a **2 + b**2
hyp = math.sqrt(hyp)
hyp = round(hyp, 2)
print("The hypotenuse is", hyp)