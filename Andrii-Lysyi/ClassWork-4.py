print("==========1==========")
num=[13,3,19,88] 
def avrg(*ark):
    return(sum(*ark)/len(*ark))
print("avrd num:", avrg(num))
print("==========2==========")
num=int(input("Enter num:"))
def absv(nn):
    if nn<0:
        return nn*-1
    else:
        return nn
print("absv num:", absv(num))
print("==========3==========")
num1=input("Enter num1:")
num2=input("Enter num2:")
def maxn(a,b):
    """Returns the larger number"""
    if a>b:
        return a
    else:
        return b
print("Max num: ", maxn(num1,num2))
print("==========4==========")
import math
types=int(input("Choose your option:\n 1 block\n 2 triangle\n 3 circle\n"))
def block(a, b):
    return(a*b)
def triangle(a, b, c):
    d=a+b+c
    return((d*(d-a)*(d-b)*(d-c))**0.5)
def circle(a):
    return(math.pi*(a**2))
if types==1:
    sidea=float(input("Enter dimention a:"))
    sideb=float(input("Enter dimention b:"))
    print("Block area is "+str(round(block(sidea,sideb),2)))
elif types==2:
    sidea=float(input("Enter dimention a:"))
    sideb=float(input("Enter dimention b:"))
    sidec=float(input("Enter dimention c:"))
    print("Triangle area is "+str(round(triangle(sidea,sideb,sidec),2)))
elif types==3:
    sidea=float(input("Enter radius:"))
    print("Circle area is "+str(round(circle(sidea),2)))
print("==========5==========")
num=input("Enter num:")
def sumn (a):
    x=0
    for num in a:
        x += int(num)
    return x
print("Sum of num: "+str(sumn(num)))
print("==========6==========")
def start(a):
    while True:
        try:
            num1=float(input("Enter num1:"))
            num2=float(input("Enter num2:"))
        except:
            print("Enter value")
        else:
            break
    if a==1:
        print("Add result is " + str(num1+num2))
    if a==2:
        print("Substract result is " + str(num1-num2))
    if a==3:
        print("Multiply result is " + str(num1*num2))
    if a==4:
        if num2 !=0:
          print("Divide result is " + str(num1/num2))
        else:
          print("Divide to 0 !")
while True:
    try:
        fun=int(input("What do you want to do?\n\
        1) add\n\
        2) substract\n\
        3) multiply\n\
        4) divide\n\
        0) quit program\n"))
    except:
        print("Enter value")
        continue
    if fun>0 and fun<=4: 
        start(fun)
    elif fun==0:
        print("Thank you for choosing our software")
        quit()
    else:
        print("Choose correct option")
