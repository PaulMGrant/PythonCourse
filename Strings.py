#Author: Paul Grant
#Date: 2025-12-31
#Description: This module contains utility functions for string manipulation.

"""mystring = "Hello, World!"
mystring[0]  # Accessing the first character 'H'
mystring[9]  # Accessing the tenth character 'r'
mystring[-2]  # Accessing the second last character 'l'
mystring[0:6] #Accessing H to ,
mystring[:3] #Accessing H to but not including the second L
mystring[::] #accessing first to last in a step size of 1
mystring[::2] #Accessing first to ast in a step size of 2
mystring[2:7:2]#Accessing l to w in steps of 2
mystring[::-1]#Accessing first to last char and then go through in reverse"""

name ="Paul" #Strings are immutable

last_letters = name[1:]
print ('S' + last_letters)
