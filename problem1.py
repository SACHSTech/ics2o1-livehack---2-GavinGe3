
"""
-------------------------------------------------------------------------------
Name:   problem1.py
Purpose:  Given an input of the number of antennas and eyes, determines the alien lifeform
 
Author: Ge.G
 
Created:  23/02/2021
------------------------------------------------------------------------------
"""
print("***Welcome to the alien life form detector***")

# get eye and antenna info
antennas = int(input("How many antennas does the lifeform have?: "))
eyes = int(input("How many eyes does the lifeform have?: "))

# determines and outputs the alien species
if antennas <= 6 and eyes >= 2:
  print("\nLife form detected: MaxMartian")
if antennas >= 3 and eyes <= 4:
  print("\nLife form detected: AudreyMartian")
if antennas <= 2 and eyes <= 3:
  print("\nLife form detected: BrooklynMartian")
if antennas == 0 and eyes == 2:
  print("\nLife form detected: MattDamonMartian")
if antennas > 6 and eyes > 4:
  print("\nNo life form detected")









