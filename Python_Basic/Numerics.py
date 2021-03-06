## Numbers - Integers, floats, math, type casting, user input
# Documentation on integers and floats can be found below:
# https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

# To check the type of an object, use the type function, example below
num_1 = 10
print(type(num_1)) # This should return class 'int'

# Standard math operations can be performed using +, -, *, /
print(4+4) # output 8
print(10-5) # output 5
print(10*2) # output 20
print(10/2) # output 5.0

# Division will give you a float (decimal value number) by default
# To perform floor division, or remove the decimal you can use //
print(10//3) # output 3

# You can use the mod operator % to find the remainder
print(10%3) # output 1
print(10%2) # output 0

# To take a number to the power of another number, you can use
# the ** operator
print(5**2) # output 25 (this is 5 squared)
print(5**3) # output 125 (this is 5 cubed)

# You can import the math module and use functions provided by it
import math
print(math.pow(10,5)) # output 100000.0, this is 10 to the power 5

# Similarly you can import the random module and generate random
# integers using the randint function
import random
print(random.randint(0,1000))   # output random integer between 0
                                # and 1000

# You can use other functions on numbers as well
num_2 = -10
print(abs(num_2))   # abs or absolute value function will remove
                    # the negative sign from the number, output 10

# To convert the string "10" to the int 10, you can cast it to an int
my_string = "10"
my_num = int(my_string) # this will convert "10" to int 10
print(type(my_num)) # output will be class 'int'

# Similarly you can convert an int to a string, 10 to "10"
# by casting it to a string
my_new_string = str(my_num) # this will convert 10 to "10"
print(type(my_new_string)) # output will be class 'str'

# The multiplication program presented in the video is below
# using input from the user using the input function
print("Welcome to the multiplication program")
print("-"*30)
num_1 = int(input("Enter a number to multiply-> "))
num_2 = int(input("Enter a second number to multiply-> "))
result = num_1 * num_2
print(result)

# Question 1: What is the remainder when you divide 2510876961 by 7?
# Don't forget to print your result to the screen!
num_1 = 2510876961
num_2 = 7
## Fill in your code below, 1 line ##
print(num_1 % num_2)
## End question 1

# Question 2: Python will place a higher order of importance to
# operations specified within parenthesis. If you are given the 3
# numbers below and asked to add the first two numbers first, then
# divide by the third one, uncomment the line below that provides
# the right result
num_1 = 15
num_2 = 25
num_3 = 100
## Uncomment the correct line below based on the question above
# print(num_1 + num_2 / num_3)
# print(num_1 / num_2 + num_3)
# print(num_1 + (num_2 / num_3))
print((num_1 + num_2) / num_3)
## End question 2

# Question 3: Import the randint function from the random module
# so it can be used by it's name, randint, instead of referring
# to the random module first
## Write your code below, 1 line ##
from random import randint
my_num = randint(5,100) 
## End question 3

