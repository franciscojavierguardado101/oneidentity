# valid operators
OPERATORS = {'+', '-', '*', '/'}
stack = []
# keep track of operation
OPERATION = ''
# take input for a fraction
expression = input("Enter a fraction: ")
expression = expression.split(' ')

# function to solve mixed number
def solved_mixed_number(num):
    if '_' not in num:
        return num
    # a_b/c
    a = num.split('_')[0]
    b = (num.split('_')[1]).split('/')[0]
    c = (num.split('_')[1]).split('/')[1]
    a = int(a)
    b = int(b)
    c = int(c)

    result = str((a*c)+b) + '/' + str(c)
    return result

# function to reduce fraction
from math import gcd
def reduceFraction(x,y):
    d = gcd(x,y)
    x = x//d
    y = y//d
    return x,y

# function to convert fraction to mixed number
def convert_to_mixed_number(num):
    if '/' in num:
        a = num.split('/')[0]
        b = num.split('/')[1]
        a = int(a)
        b = int(b)
        if a//b == 0:
            return num
        a,b = reduceFraction(a,b)        
        result = str(a//b) + '_' + str(a-(a//b * b)) + '/' + str(b)
    else:
        result = num
    return result

def fraction_multiplication(num1,num2):
    num1 = solved_mixed_number(num1)
    num2 = solved_mixed_number(num2)

    result = str(int(num1.split('/')[0]) * int(num2.split('/')[0])) + '/' + str(int(num1.split('/')[1]) * int(num2.split('/')[1]))
    result = convert_to_mixed_number(result)
    return result

def fraction_division(num1,num2):
    num1 = solved_mixed_number(num1)
    num2 = solved_mixed_number(num2)

    result = str(int(num1.split('/')[0]) * int(num2.split('/')[1])) + '/' + str(int(num1.split('/')[1]) * int(num2.split('/')[0]))
    result = convert_to_mixed_number(result)
    return result

def fraction_addition(num1,num2):
    num1 = solved_mixed_number(num1)
    num2 = solved_mixed_number(num2)
    # add two fractions
    if int(num1.split('/')[1]) != int(num2.split('/')[1]):
        result = str(int(num1.split('/')[0]) * int(num2.split('/')[1]) + int(num2.split('/')[0]) * int(num1.split('/')[1])) + '/' + str(int(num1.split('/')[1]) * int(num2.split('/')[1]))
    else:
        result = str(int(num1.split('/')[0]) + int(num2.split('/')[0])) + '/' + str(int(num1.split('/')[1]))
    result = convert_to_mixed_number(result)
    return result

def fraction_subtraction(num1,num2):
    num1 = solved_mixed_number(num1)
    num2 = solved_mixed_number(num2)
    # subtract two fractions
    if int(num1.split('/')[1]) != int(num2.split('/')[1]):
        result = str(int(num1.split('/')[0]) * int(num2.split('/')[1]) - int(num2.split('/')[0]) * int(num1.split('/')[1])) + '/' + str(int(num1.split('/')[1]) * int(num2.split('/')[1]))
    else:
        result = str(int(num1.split('/')[0]) - int(num2.split('/')[0])) + '/' + str(int(num1.split('/')[1]))
    result = convert_to_mixed_number(result)
    return result


for i in expression:
    if i not in OPERATORS:
        if OPERATION == '':
            stack.append(i)
        else:
            num1 = stack.pop()
            num2 = i
            if OPERATION == '+':
                result = fraction_addition(num1,num2)
                stack.append(result)
            elif OPERATION == '-':
                result = fraction_subtraction(num1,num2)
                stack.append(result)
            elif OPERATION == '*':
                result = fraction_multiplication(num1, num2)
                stack.append(result)
            elif OPERATION == '/':
                result = fraction_division(num1, num2)
                stack.append(result)
            OPERATION = ''
    else:
        OPERATION = i
    

print(stack.pop())