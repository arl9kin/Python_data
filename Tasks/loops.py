
'''
Question 1
Ask the user for two numbers between 1 and 100. Then count from the
lower number to the higher number. Print the results to the screen.
'''
a = int (input('enter a number 1: >'))
b = int (input('enter a number 2: >'))
if a > b:
    print (b, a3)
elif a < b:
    print (a, b)
else:
    print ('equal')

'''
Question 2
Ask the user to input a string and then print it out to the screen in
reverse order (use a for loop).
'''
string = str.lower (input ('enter a string: >>> '))

for i in range ((len(string)),0,-1):
    print (string[i-1], end = '')

'''
Question 3
Ask the user for a number between 1 and 12 and then display a times
table for that number.
'''
num = int (input ('enter a number from 1 to 12: >>'))
if num >= 1 and num <= 12:
    for i in range (1,11):
        print (f'{num} x {i} = ', i*num)
else:
    print ('wrong number')


'''
Question 4
Can you amend the solution to question 3 so that it just prints out all
times tables between 1 and 12? (no  need to ask user for input)
'''
for i in range (1,11):
    print ('==================')
    for j in range (1,13):
        print (f'{j} x {i} =', i*j)
        


'''
Question 5
Ask the user to input a sequence of numbers. Then calculate the mean
and print the result
'''
numbers =  (input ('enter a numbers, press n to stop: >'))

num=[]

while numbers !='n':
    if numbers == 'n':
        break
    else:
        num.append (int(numbers))
        numbers =  (input ('continue, press n to stop: >'))

a = sum(num)/len(num)
print (f'{a} is mean of the list')


'''
Question 6
Write code that will calculate 15 factorial. (factorial is product of
positive ints up to a given number. e.g 5 factorial is 5x4x3x2x1)
'''
n = int (input ('enter a necessary factorial: '))
fact = 1

for i in range (1, n+1):
    fact = fact * i
    
print (fact)
      
'''
Question 7
Write code to calculate Fibonacci numbers. Create list containing
first 20 Fibonacci numbers, (Fib  numbers made by sum of preceeding
two. Series starts 0 1 1 2 3 5 8 13 ....)
'''

n = 20

a = 0
b = 1

fib = []

for i in range (n):
    fib.append (a)
    a,b = b, a+b
    
print (fib)
'''
Question 8
The previous question was the first to contain comments. Go back
through the other questions in this file and add comments to the
solutions.
'''

'''
Question 9

     *****
     *
     ****
     *
     *
     *
Can you draw this using python? (comment the solution code)
'''
star = '*'
for row in range (1,7):
    for col in range(1,6):
        if row == 1 and col < 6:
            print (star, end = '')
        elif row == 2 and col == 1:
            print ()
            print (star)
        elif row == 3 and col < 5:
            print (star, end = '')
        elif row == 4 and col == 1:
            print ()
            print (star)
        elif row == 5 and col == 1:
            print (star)
        elif row == 6 and col == 1:
            print (star)

'''
Question 10
Write some code that will determine all odd and even numbers
between 1 and 100. Put the odds in a list named odd and the evens
in a list named even.
'''
even = []
odd = []
for i in range (1,101):
    if i % 2 == 0:
        even.append (i)
    else:
        odd.append (i)
        
print (odd)
print (even)



