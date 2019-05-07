print("==================1.1==========================")
for i in range(0,100,2):
    print(i)
print("==================1.2==========================")
i=0
while i<100:
  print(i)
  i+=2
print("==================2.1==========================")
for i in range(100):
  if i%2==0:
    continue
  print(i)
print("==================2.2==========================")
for i in range(100):
  if i%2!=0:
    print(i)
print("==================3==========================")
list=[1,1,2,3,5,8,13,21,34,55,89,134]
for i in list:
  if i%2==1:
    print("There are odd number in the list")
    break
else:
  print("There are no odd number in the list")
print("==================4==========================")
numbers_int = [13, 3, 19, 88]
numbers_float = []
for i in numbers_int:
    numbers_float.append(float(i))
print(numbers_float)
print("==================5==========================")
f1=f2=1
n=int(input())
if n<2:
    quit()
    print(f1, end=' ')
print(f2, end=' ')
for i in range(2, n):
    f1, f2=f2, f1+f2
    print(f2, end=' ')
    print()
print("==================6==========================")
list=["q","w","e","r"]
for i in list:
  print(i)
print("==================7==========================")
list=["q","w","e","r"]
for i in list:
  print(i,end="#, ")
