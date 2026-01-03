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

"""name ="Paul" #Strings are immutable

last_letters = name[1:]
#print ('S' + last_letters)
print (name.upper()) #makes all upper case
name.lower() #makes all lower case
name.split() #separates by white space
name.split('a')#separates at every 'a'"""

#.function() method
# string here {} then also {}.format('something1', 'something2')

"""print('this is a string {}'.format('INSERTED'))

print('The {} {} {}'.format('fox', 'brown', 'Quick')) #The fox brown Quick
print('The {2} {1} {0}'.format('fox', 'brown', 'Quick'))#The Quick brown fox
print('The {0} {0} {0}'.format('fox', 'brown', 'Quick'))#The fox fox fox

print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))#The quick brown fox"""

#float formatting follows "{value:width.precision f}"
"""result = 100/777

print('the result was {r}'.format(r = result))#the result was 0.1287001287001287
print('the result was {r:1.3}'.format(r = result))#the result was 0.129
print('the result was {r:10.3}'.format(r = result))#the result was      0.129"""

#format string literals
"""name = 'Paul'
age = 47
print('Hello, my name is {}'.format(name))#Hello, my name is Paul
print(f'Hello, my name is {name}')#Hello, my name is Paul
print(f'{name} is {age} years old')#Hello, my name is Paul"""








