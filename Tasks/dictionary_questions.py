
'''
Question 1
Can you remember how to check if a key exists in a dictionary?
Using the capitals dictionary below write some code to ask the user to input
a country, then check to see if that country is in the dictionary and if it is
print the capital. If not tell the user it's not there.
'''
# capitals = {'France':'Paris','Spain':'Madrid','United Kingdom':'London',
#             'India':'New Delhi','United States':'Washington DC','Italy':'Rome',
#             'Denmark':'Copenhagen','Germany':'Berlin','Greece':'Athens',
#             'Bulgaria':'Sofia','Ireland':'Dublin','Mexico':'Mexico City'
#             }

# user = str.capitalize(input ('Enter a country:\n\t >>>'))

# if user.isalpha()  or 'United states' or 'United kingdom':
#     if user in capitals:
#         print (f'{capitals [user]} is the capital of {user}')
#     elif user == "Usa" or user == 'United states':
#         print (f'{capitals ["United States"]} is the capital of {"United States"}')
#     elif user == "Uk" or user == "United kingdom":
#         print (f'{capitals ["United Kingdom"]} is the capital of {"United Kingdom"}')
#     else:
#         print ('No such country')
# else:
#     print ('Please don\'t use numbers or other symbols')


'''
Question 2
Write python code that will create a dictionary containing key, value pairs
that represent the first 12 values of the Fibonacci sequence
i.e {1:0,2:1,3:1,4:2,5:3,6:5,7:8 etc}
'''
# start = 0
# nxt = 1

# fab = {}

# for nums in range (1,13):
#     fab[nums] = start
#     start, nxt = nxt, nxt+start

# print (fab)
    

'''
Question 3
Create a dictionary to represent the open, high, low, close share price data
for 4 imaginary companies. 'Python DS', 'PythonSoft', 'Pythazon' and 'Pybook'
the 4 sets of data are [12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
[98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]
'''
# data1 = {'Python DS': {'open':12.87, 'high':13.23, 'low':11.42, 'close': 13.10},
#         'PythonSoft': {'open':23.54, 'high':25.76, 'low':21.87,'close':22.33},
#         'Pythazon': {'open':98.99, 'high':102.34, 'low':97.21,'close':100.065},
#         'Pybook': {'open':203.63, 'high':207.54, 'low':202.43, 'close':205.24}
#         }

# for k,v in data1.items():
#     print (f"""{k}:\n\t Open price is {v['open']} \n\t High price is {v['high']}
#      Low price is {v['low']} \n\t Close price is {v['close']}""")

# names = ['Python DS', 'PythonSoft', 'Pythazon', 'Pybook']
# status = ['open', 'high', 'low', 'close']
# price = [[12.87, 13.23, 11.42, 13.10],[23.54,25.76,21.87,22.33],
# [98.99,102.34,97.21,100.065],[203.63,207.54,202.43,205.24]]
# data = {}

# for i in range (len(status)):
#     data[names[i]] = dict (zip(status, price[i]))

# for k,v in data.items():
#     print (f"""{k}:\n\t Open price is {v['open']} \n\t High price is {v['high']}
#      Low price is {v['low']} \n\t Close price is {v['close']}""")


''' Question 4
Go to the python module web page and find a module that you like. Play with it,
read the documentation and try to implement it.
'''
# import webbrowser as w
# w.open('https://docs.python.org/3/library/webbrowser.html#module-webbrowser', new=0, autoraise=True)

'''
Question 5
Create a dictoinary containing as keys the letters from A-Z, the values should
be random numbers created from the random module. Can you draw a bar graph of
the results?
'''
# from random import randint as r
# import matplotlib.pyplot as plt
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# dict = {}

# for i in range (len(alpha)):
#     dict [alpha[i]] = r(1,100)


# for k,v in dict.items():
#     print (k, v)


# x,y = zip(*dict.items())

# plt.bar(x,y)
# plt.show()
'''
Question 6
Create a dictionary containing 4 suits of 13 cards
['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
'''
# a = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
# suit = ['spades','diamonds', 'clubs','hearts']
# suits = {}

# for i in range (len(suit)):
#     suits [suit[i]] = a


# for k,v in suits.items():
#     print(k,v, end = " ")
