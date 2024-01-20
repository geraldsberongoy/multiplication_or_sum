# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

# Given 1:
# number 1 = 20
# number 2 = 30

# Expected output: 
# The result is 600

# Given 2:
# number 1 = 40
# number 2 = 30

# Expected output:
# The result is 70

# pseudocode
# 1. assigning variables for givens
# 2. multiply 2 numbers
# 3. if statement result <= 1000
#      print result
# 4. else statement
#      print add 2 number

# Code

# Given 1:
number_1 = 20
number_2 = 30

product = number_1 * number_2

if product <= 1000:
    print("The result is: ", product)
else:
    sum = number_1 + number_2
    print("The result is: ", sum)

# Given 2:
number_3 = 40
number_4 = 30

product = number_3 * number_4

if product <= 1000:
    print("The result is: ", product)
else:
    sum = number_3 + number_4
    print("The result is: ", sum)