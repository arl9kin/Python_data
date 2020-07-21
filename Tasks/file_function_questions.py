'''
Question 1
Create a function that will calculate the sum of two numbers. Call it sum_two.
'''
# def sum_two(a, b):
#     c = a + b
#     print (c)

# sum_two (3,4)

'''
Question 2
Write a function that performs multiplication of two arguments. By default the
function should multiply the first argument by 2. Call it multiply.
'''

# def multiply (a,b=2):
#     c = a * b
#     print (c)
    
# multiply (2)
# multiply (2,3)


'''
Question 3
Write a function to calculate a to the power of b. If b is not given
its default value should be 2. Call it power.
'''

# def power (a, b=2):
#     c = a**b
#     print (c)
    
# power(2)
# power(2,3)


'''
Question 4
Create a new file called capitals.txt , store the names of five capital cities
in the file on the same line.
'''
# file = open('capitals.txt', 'w')
# file.write('London, Moscow, Berlin, Rome, Tokyo')
# file.close()

# file = open('capitals.txt', 'r')
# print(file.readlines())
# file.close()

'''
Question 5
Write some code that requests the user to input another capital city.
Add that city to the list of cities in capitals. Then print the file to
the screen.
'''
# with open ('capitals.txt','r') as f:
#     for i in f.readlines():
#         print (i ,end = ' ')

# user = str.lower (input ('Do you want to add new capital (y/n): \n\t>>'))

# while user == "yes" or user == "y":
#     user = str.lower (input ('enter new capital: \n\t>>'))
#     with open ("capitals.txt", 'a') as f:
#         f.write(f', {user.title()}')
#     with open ('capitals.txt','r') as f:
#         for i in f.readlines():
#             print (i ,end = ' ')   
#     user = str.lower (input ('Do you want to add new capital (y/n): \n\t>>'))
    
# if user == 'n' or user == "no":
#     print ("thanks for using my programm")
# else:
#     print ("please use only y/n")


'''
Question 6
Write a function that will copy the contents of one file to a new file.
'''

# def clone (a='capitals.txt', b='capitals_copy.txt'):
#     """Creates copy of original file (a)"""    

#     copy = []

#     with open (a, 'r') as origin:
#         for i in origin.readlines():
#             copy.append(i)
            
#     with open (b, 'w') as cop:
#         for i in copy:
#             cop.write (i)
            
# clone()