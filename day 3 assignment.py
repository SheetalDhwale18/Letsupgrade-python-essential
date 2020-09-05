day 3 assignment 
------------------------------------------------------------------
que no . 1 solution:


a=int(input("please enter the altitude in feets:"))
if  a<=1000:
    print("safe to land")
elif (a>1000 and a<5000):
    print("come down to 1ooo ft")
else:
    print("go around and try later")



"""output:

please enter the altitude in feets:5500
go around and try later

please enter the altitude in feets:4600
come down to 1ooo ft 


please enter the altitude in feets:1000
safe to land


 """
--------------------------------------------------------------------

# Python program to display all the prime numbers within range

lower = 1
upper = 200

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
           
           
           
           
           
  """  output:       Prime numbers between 1 and 200 are:
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
101
103
107
109
113
127
131
137
139
149
151
157
163
167
173
179
181
191
193
197
199

"""