# ==================a==========================/n
a = float(input("Enter a= "))
b = float(input("Enter b= "))
if a >= b:
     print("max is {}".format(a))
else:
     print("max is {}".format(b))
# =====================b========================/n
num = float(input("Enter num= "))
if (num % 2) == 0:
    print("Number {} is even number".format(num))
else:
     print("Number {} is odd number".format(num))
# ==================c============================/n
user = float(input("Enter num= "))
result = 1
a = 1
while a <= user:
    result *= a
    a += 1
print("Factorial num {} is {}".format(user, result))

