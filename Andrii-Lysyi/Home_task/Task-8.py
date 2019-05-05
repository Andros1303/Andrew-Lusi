#"======================a============================"/n
user = str(input("Enterb num= "))
count = 1
for i in user:
    count *= int(i)
print(count)
#"=========================b=========================="/n
num_reverse = " ".join(user[::-1])
print(num_reverse)
#"==========================c=========================="/n
num_sort = sorted(user)
print(num_sort)
