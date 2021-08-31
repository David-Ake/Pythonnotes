# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 10:50:36 2021

@author: 0656646
"""

school = "Coral Gables Sernior High"
#print out 10 letter
print(school[9])

"""

Print out from the tenth letter
to the end  of the string 

"""

print(school[9:])

#Print out the second to fifth letter
print(school[1:4])

#In reverse?
print(school[::-1])
#The length of the string?
L = len(school)
print("Size of string is ", L)

#Print every other letter
print(school[0:L-1:2])

print("Where is the first space in the String?")
print(school.index(" "))
print("Where is the second space in String?")
print(school.index(" ", 6))
print(school[:5])
print(school[6:12])

month = input("Birth month: ")
day = input("Birth day")
year = input("Birth year")
n = input("Your first and last name: ")

space = n.index(" ")
initials = n[0] + n[space + 1]
print("Your Gables password is: ")
print(month + day + year + initials)