print("==========1==========")
num = [13,3,19,88] 
def avrg(*ark):
    return(sum(*ark)/len(*ark))
print("avrd num:", avrg(num))
print("==========2==========")
num = int(input("Enter num:"))
def absv(nn):
    if nn < 0:
        return nn*-1
    else:
        return nn
print("absv num:", absv(num))
print("==========3==========")
num1 = input("Enter num1:")
num2 = input("Enter num2:")
def maxn(a,b):
    """Returns the larger number"""
    if a>b:
        return a
    else:
        return b
print("Max num: ", maxn(num1,num2))
print("==========4==========")
import math
type_s = int(input("Choose your option:\n 1 block\n 2 triangle\n 3 circle\n"))
def block(a, b):
    return(a*b)
def triangle(a, b, c):
    p = a+b+c
    return((p*(p-a)*(p-b)*(p-c))**0.5)
def circle(a):
    return(math.pi*(a**2))
if type_s == 1:
    vala = float(input("Enter dimention a:"))
    valb = float(input("Enter dimention b:"))
    print("Block area is "+str(round(block(vala,valb),2)))
elif type_s == 2:
    vala = float(input("Enter dimention a:"))
    valb = float(input("Enter dimention b:"))
    valc = float(input("Enter dimention c:"))
    print("Triangle area is "+str(round(triangle(vala,valb,valc),2)))
elif type_s == 3:
    vala = float(input("Enter radius:"))
    print("Circle area is "+str(round(circle(vala),2)))
print("==========5==========")
num = input("Enter num:")
def sumn (a):
    x = 0
    for num in a:
        x += int(num)
    return x
print("Sum of numbers: "+str(sumn(num)))
print("==========6==========")
def start(a):
    while True:
        try:
            num1 = float(input("Enter num1:"))
        except:
            print("Enter value")
        else:
            break
    while True:
        try:
            num2 = float(input("Enter num2:"))
        except:
            print("Enter value")
        else:
            break
    if a == 1:
        print("Add result is " + str(num1 + num2))
    if a == 2:
        print("Substract result is " + str(num1 - num2))
    if a == 3:
        print("Multiply result is " + str(num1 * num2))
    if a == 4:
        print("Divide result is " + str(num1 / num2))
while True:
    try:
        var = int(input("What do you want to do?\n\
        1) add\n\
        2) substract\n\
        3) multiply\n\
        4) divide\n\
        5) quit program\n"))
  
    except:
        print("Enter value")
        continue
    if var  > 0 and var <= 4: 
        start(var)
    elif var == 5:
        print("Thank you for choose our software")
        quit()
    else:
        print("Choose correct option")
