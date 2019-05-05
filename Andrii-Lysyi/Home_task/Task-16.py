# ==================1.1==========================/n
for i in range(0,100,2):
    print(i)
# ==================1.2==========================/n
i=0
while i<100:
  print(i)
  i+=2
# ==================2.1==========================/n
for i in range(100):
  if i%2==0:
    continue
  print(i)
# ==================2.2==========================/n
for i in range(100):
  if i%2!=0:
    print(i)
# ==================3==========================/n
list_number=[1,1,2,3,5,8,13,21,34,55,89,134]
for i in list_number:
  if i%2==1:
    print("There are odd number in the list")
    break
else:
  print("There are no odd number in the list")
# ==================4==========================/n
list=list(range(13))
for i in range(len(list)):
  list[i]=float(list[i])
print(list)
# ==================5==========================/n
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
# ==================6==========================/n
list=["q","w","e","r"]
for i in list:
  print(i)
# ==================7==========================/n
list=["q","w","e","r"]
for i in list:
  print(i, end="#")
