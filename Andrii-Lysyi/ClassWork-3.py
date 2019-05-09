print("==========1==========")
list=input("Enter list:\n")
listn = list.split(",")
print("Max="+str(max(listn))+", min="+str(min(listn)))
print("==========2==========")
base = range(11)
even = [x for x in base if x%2==0]
oddmul3 = [x for x in base if x%3==0]
other = [x for x in base if x%2!=0 and x%3!=0]
print(even)
print(oddmul3)
print(other)
print("==========3==========")
inputn = int(input("Enter an integer value > 0:\n"))
if inputn < 0:
    print("Enter a valid number next time")
elif inputn == 0:
    print("Factorial is 1")
else:
    fact = [x for x in range(0,inputn+2)]
    i = 0
    factorial = [1]
    while i < inputn:
        factorial.append(factorial[i]*fact[i+1])
        i += 1
    print("Factorial is "+str(max(factorial))) 
print("==========4==========")
while True:
    login = input("Please enter your login:\n")
    if login == "First":
        print("Greetings "+login)
        break
    else:
        print("Enter a valid login")
print("==========5==========")
while 2 > 1:
    if int(input("Please enter your number:\n"))>0:
        pass
    else:
        break
print("==========6==========")
num = int(input("Please enter quantity of numbers:\n"))
i =0
while i < num:
    i+=1
    if int(input("Please enter your number:\n"))>0:
        pass
    else:
        break
print("==========7==========")
list = range(10, 31)
listn = []
for x in list:
    listn.append(x)
for x in listn:
    if x%2 != 0:
        print(str(x)+" is a prime number")
    elif x%8 == 0:
        print(str(x)+" equals "+str(2)+" * "+str(2)+" * "+str(2)+" * "+str(x//8))
    elif x%4 == 0:
        print(str(x)+" equals "+str(2)+" * "+str(2)+" * "+str(x//4))
    else:
        print(str(x)+" equals "+str(2)+" * "+str(x//2))
print("==========8==========")
sentence = "Beautiful is batter than ugly"
words = sentence.split(" ")
length = []
for word in words:
    length.append(len(word))
myset = dict(zip(length, words))
wordssorted = []
for srt in sorted(myset):
    wordssorted.append(myset[srt])
print(" ".join(wordssorted))







