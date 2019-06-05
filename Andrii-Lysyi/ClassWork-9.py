print("==========1==========")
names = ['Sam', 'Don', 'Daniel'] 
surnames = map(hash, names)
print(list(surnames))
print("==========2==========")
colorlist = ["red", "green", "black", "red", "brown", "red", "blue", "red", "red", "yellow"]
numred = filter(lambda col: col == "red", colorlist)
print(list(numred))
print("==========3==========")
numlist = ["1", "2", "3", "4", "5", "6", "7"]
listint = [int(num) for num in numlist]
print(listint)
listint2 = list(map(lambda num: int(num), numlist))
print(listint2)
print("==========4==========")
def kilom(mile):
    return mile/1.6
lengthlist = [1.7, 7, 8.5]
listkilom1 = list(map(kilom, lengthlist))
print(listkilom1)
listkilom2 = list(map(lambda length: length/1.6, lengthlist))
print(listkilom2)
print("==========5==========")
from functools import reduce
people = [{'name': 'Sam', 'height': 160}, {'name': 'Alex', 'height': 80}, {'name': 'Jack'}] 
ifheight = list(filter(lambda x: len(x)>1, people))
filtering = list(map(lambda x: x['height'], ifheight))
summ = reduce(lambda x, y: x+y, filtering)
print(summ)
print("==========6==========")
def topping(func):
    def extras():
        print("<\^^^^^^^/>\n tomatos \n --meat-- \n ~salad~") 
        func()
    return extras
@topping
def sandwitch():
    print("<\______/>")
sandwitch()
print("==========7==========")
def rangegen(num1, num2, step=1):
    while num1 < num2:
        yield num1
        num1 += step
print(list(rangegen(2, 15)))