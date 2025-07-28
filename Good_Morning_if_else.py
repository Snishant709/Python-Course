'''
The strftime() Method
The datetime object has a method for formatting date objects into readable strings.
The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:
'''
import time
timestamp = (int(time.strftime('%H')))
print(timestamp)
if timestamp <12 and timestamp >5:
    print("Good Morning")
elif timestamp<18 and timestamp >12:
    print("Good Afternoon")
elif timestamp>18 and timestamp <22: 
    print("Good Evening")
else :
    print("Good Night")

# https://docs.python.org/3/library/time.html#time.strftime


t=int(input("Enter time "))
if t < 12 and t >5:
    print("Good Morning")
elif t >12 and t<18:
    print("Good Afternoon")
elif t >18 and t<22:
    print("Good Evening")
else:
    print("Good Night")