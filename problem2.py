"""
-------------------------------------------------------------------------------
Name:   problem2.py
Purpose:  Given 3 inputted sidelengths, determines if the sidelengths form a triangle
 
Author: Ge.G
 
Created:  23/02/2021
------------------------------------------------------------------------------
"""
print("*****Welcome to the Triangle Checker*****")

# gets sidelength info
sideOne = float(input("Enter the length of the first side: "))
sideTwo =  float(input("Enter the length of the second side: "))
sideThree = float(input("Enter the length of the third side: "))

# determine and output if the sidelengths form  a triangle
if sideOne + sideTwo > sideThree and sideOne + sideThree > sideTwo and sideTwo + sideThree > sideOne:
  print(f"\nThe figure with sidelengths {sideOne}, {sideTwo} and {sideThree} is a triangle")
else:
  print(f"\nThe figure with sidelengths {sideOne}, {sideTwo} and {sideThree} is not a triangle")
