day 5 assignment 

question no. 1:solution


test_list = [1,5,6,4,1,2,3,5] 
sub_list = [1,1,5] 

 
print ("Original list : " + str(test_list)) 
print ("Original sub list : " + str(sub_list)) 


flag = 0
if(set(sub_list).issubset(set(test_list))): 
	flag = 1

if (flag) : 
	print ("it's a match.") 
else : 
	print ("it's gone.") 
----------------------------------------------------------
#question 2: solution

def isPrime(x):
    for n in range(2,x):
        if x%n==0:
            return False
        else:
            return True

fltrObj=filter(isPrime, range(2500))
print ('Prime numbers between 1-2500:', list(fltrObj))

------------------------------------------------------------

