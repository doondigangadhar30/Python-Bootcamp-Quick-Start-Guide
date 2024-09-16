print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
if size=="S":
    v=15
elif size=="M":
    v=20
else:
    v=25
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni == "Y" and size=="S":
    q = 2
elif pepperoni == "Y" and size!="S":
    q = 3
else:
    q = 0
extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese =="Y":
    a = 1
else:
    a = 0
bill=v+q+a
print(f"Your final bill is: ${bill}")
