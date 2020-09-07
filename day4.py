#python day 4 assignment 

#que 1:solution

lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))  
for num in range(lower,upper + 1):  
   sum = 0  
   temp = num  
   while temp > lower+1:  
       digit = temp % 10  
       sum += digit ** 3  
       temp //= 10  
       if num == sum:  
          print("the first armstrong no is:")  
          print(num)
          
          
          
 """output:     
Enter lower range: 200

Enter upper range: 500
the first armstrong no is:	
216
"""