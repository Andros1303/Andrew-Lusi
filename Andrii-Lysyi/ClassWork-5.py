print("==========1==========")
print("Hi, the number from 1 to 100 has been choosen, can you find it ?\n")
import random
riddle = random.randint(1, 101)
while True:
    value = int(input("Enter your num:"))
    if value==riddle:
        print("You Win !! num is "+str(riddle))
        break
    elif value>riddle:
        print("Try a smaller num")
    elif value<riddle:
        print("Try a biger num")
print("==========2==========")
import math
types=int(input("Choose your body:\n 1 block\n 2 triangle\n 3 circle\n"))
def block(a, b):
    return(a*b)
def triangle(a, h):
    return(a*h*0.5)
def circle(a):
    return(math.pi*(a**2))
if types==1:
    sidea=float(input("Enter side a:"))
    sideb=float(input("Enter side b:"))
    print("Block area is "+str(round(block(sidea,sideb),2)))
elif types==2:
    sidea=float(input("Enter side a:"))
    sideh=float(input("Enter side h:"))
    print("Triangle area is "+str(round(triangle(sidea,sideh),2)))
elif types==3:
    sidea=float(input("Enter radius:"))
    print("Circle area is "+str(round(circle(sidea),2)))
print ("==========3==========")
import pyowm
city=input("What city you are interested:\n")
owm = pyowm.OWM('3664c132943f34b470fc246f00a49372')    
observation = owm.weather_at_place(city)
w = observation.get_weather()
temperature=w.get_temperature('celsius')['temp']
print("In " + city + " city" + " is the temperature of the air" + " " + str(temperature) + " for the Celsius")
print("In this city "+ w.get_detailed_status()+", wind speed is "+str(w.get_wind()["speed"])+"m/s, humidity is "+str(w.get_humidity())+"%.")
