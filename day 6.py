

#question no 1:solution
class Bank_Account: 
    def __init__(self,name): 
        self.balance=0
        self.name=name
        
  
    def deposit(self): 
        amount=float(input("Enter amount to be Deposited: ")) 
        self.balance += amount 
        print("\n Amount Deposited:",amount) 
  
    def withdraw(self): 
        amount = float(input("Enter amount to be Withdrawn: ")) 
        if self.balance>=amount: 
            self.balance-=amount 
            print("\n You Withdrew:", amount) 
        else: 
            print("\n Insufficient balance  ") 
  
    def display(self): 
        print("\n Net Available Balance=",self.balance) 
        print("\n name of the account holder is:=",self.name) 

   

s = Bank_Account("john De'suza") 
   
 
s.deposit() 
s.withdraw() 
print("\n the current account details are:")
s.display()

"""


output
Enter amount to be Deposited: 200

 Amount Deposited: 200.0

Enter amount to be Withdrawn: 600

 Insufficient balance  
the current account details are:

 Net Available Balance= 200.0

 name of the account holder is:= john De'suza
"""

#question 2: Solution

import math
class cone():
    def __init__(self,radius,height):
        self.radius=radius
        self.height=height
    def volume(self):
        return (1.0/3)*math.pi*r*r*h
    def SA(self):
        return math.pi*r*(r+1)
 
r=int(input("Enter radius of cone: "))
h=int(input("enter height of cone:"))
obj=cone(r,h)
print("volume of cone:",obj.volume(),2,)
print("surface area of cone:",obj.SA(),2)


"""output
Enter radius of cone: 14

enter height of cone:15
volume of cone: 3078.7608005179973 2
surface area of cone: 659.7344572538566 2

"""


















