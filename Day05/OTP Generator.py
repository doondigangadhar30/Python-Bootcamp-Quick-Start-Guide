import random
print("Your OTP is:",end=" ")
num=[0,1,2,3,4,5,6,7,8,9]
for i in range(6):
    print(random.choice(num),end="")
