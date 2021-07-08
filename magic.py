import random
print("welcome to abra-ka-dabra club")
print("take any number in your from range 1 to 10")
a=[1,2,3,4,5,6,7,8,9,10]
b=random.choice(a)
print("add number",b,"in your original number")
c=random.choice(a)
print("add number",c,"in your original number")
print("subtract the original number from it")
d=random.choice(a)
print("add number",d,"in your remaining number number")
e=random.choice(a)
print("subtract number",e,"from your remaining number")
f=input("lets compare the answer\npress 'y' to compare")
if f=="y":
    print("your answer is",b+c+d-e)

