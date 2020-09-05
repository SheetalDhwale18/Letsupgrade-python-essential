
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