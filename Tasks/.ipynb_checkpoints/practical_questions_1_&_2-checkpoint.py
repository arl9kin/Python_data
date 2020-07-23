'''
Question 1

Create a class to represent a bank account. It will need to have a balance,
a method of withdrawing money, depositing money and displaying the balance to
the screen. Create an instance of the bank account and check that the methods
work as expected.
'''

# class Bank_account (object):
#     """"""
#     status = 'client'
    
#     def __init__ (self, name, balance = 0.0):
#         self.name = name
#         self.balance = balance
        
#     def show_balance(self):
#         print (f'your balance is {self.balance}') 
        
#     def withdraws_types (self):
#         print ("1. Bank\n2. Bankomate\n3. Electronic ")
    
#     def withdraw (self,summ):
#         if self.balance == 0:
#             print ('You don\'t have enough money on your account')
#             print (f'your balance is {self.balance}')
#         else:
#             if self.balance - summ >= 0:
#                 print ('Here it is your money')
#                 self.balance -= summ
#                 print (f'your balance is {self.balance}')
#             else:
#                   print ('You don\'t have enough money for this transaction')
#                   print (f'your balance is {self.balance}')
    
#     def deposit (self,summ):
#         if summ >0:
#             self.balance += summ
#             print (f'your balance is {self.balance}')
#         else:
#             print ('Your deposit shoud be positive number')
            
#     def balance(self):
#         print (f'your balance is {self.balance}') 
        
# anton = Bank_account('Anton')
# mauka = Bank_account ("Mauka Keka")



'''Question 2
 Create a circle class that will take the value of a radius and
 return the area of the circle
'''
# import math 

# class Circle(object):
#     """class will take the value of a radius and
#  return the area of the circle"""
    
#     status = 'circle'    

#     def __init__ (self, radius):
#         self.radius = radius
        
#     def circle_area (self):
#         area = (self.radius**2) * math.pi
#         return round (area,3)

# my_circ2 = Circle(5.5)
# my_circ2.circle_area()

# my_circ2 = Circle(sd)
