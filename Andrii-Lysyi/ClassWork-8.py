print("==========1==========")
while True:
    try:
        num = input("Enter the num:")
        num.isdigit() == True
        print(num+" is even") if int(num)%2 == 0 else print(num+" is odd")
    except ValueError:
        print("Enter the num")
    else:
        break
print("==========2==========")
def agetype(age):
    print(age+" is even") if int(age)%2 == 0 else print(age+" is odd")
class AgeError(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return repr(self.data)
while True:
    try:
        age = input("Enter your age:")
        if age.isdigit() == True:   
            if int(age)<1 or int(age)>120:
                raise AgeError("Enter a corect age:")
            else:
                agetype(age)
        else:
            raise AgeError("Enter a digit")          
    except AgeError as ae:
        print(ae.data)
    else:
        break
print("==========3==========")
num = input("Enter two num seperated by a coma:")
try:
    # vals = num.split(",")
    # num1 = int(vals[0])
    # num2 = int(vals[1])
    # rslt = num1%num2
    num1, num2 = eval(num)
    rslt = int(num1)%int(num2)
except ZeroDivisionError:
    print("Second num is 0, you can't divide by 0")
except ValueError:
    print("Eneter num")
else:
    print(rslt)
finally:
    print("code is corekt")
print("==========4==========")
class WeeksError(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return repr(self.data)
day = ["day", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
while True:
    try:
        userday = input("Enter a num from 1 to 7 to find week day:")
        if userday.isdigit() == True:
            if int(userday)<1 or int(userday)>7:
                raise Error("Enter a num from 1 to 7")
            else:
                print(day[int(userday)])
        else:
            raise Error("Enter a num")
    except Error as we:
        print(we.data)
    else:
        break