# Create a program that will accept the two legs of a right-angle triangle, a and b, and display the length of the hypotenuse, c. 
# Remember to use prompts for the input and labels for the output. Use the formula a2 + b2 = c2 to calculate your answer.
redo = True
while (redo):
  a = float(input( "Put in sidelength 1 " ))
  b = float(input( "Put in sidelength 2 " ))
  if a != float and b != float:
    print("Put in a number or a decimal")
  else:
    redo = False
hyp = a **2 + b**2
print(hyp)