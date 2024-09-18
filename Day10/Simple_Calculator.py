def calci(x=0,d=0):
    if x == 1:
        a = d
    else:
        a = float(input("Enter a number: "))
    
    c = input("+\n-\n/\n*\nPick an operation: ")
    b = float(input("Next number: "))
    
    if c == '+':
        d = a + b
        print(d)
    elif c == '-':
        d = a - b
        print(d)
    elif c == '/':
        d = a / b
        print(d)
    elif c == '*':
        d = a * b
        print(d)
    else:
        print("Enter a valid operation")
        return
    
    h = input(f"Want to continue with {d} and operators? Type 'y' or 'n': ").lower()
    
    if h == 'n':
        print("Over")
    else:
        calci(1,d)

calci(x=0,d=0)
