import random
g=int(input("What do you choose? \nType 0 for rock,Type 1 for paper,Type 2 for scissors: "))
rd=random.randint(0,2)
rock= '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
'''
paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''
scissor = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
lit = [rock,paper,scissor]
if g==0:
    print(lit[g])
    if rd==0:
        print("computer choose")
        print(lit[rd])
        print("its a tie")
    elif rd==1:
        print("computer choose")
        print(lit[rd])
        print("You loose")
    else:
        print("computer choose")
        print(lit[rd])
        print("You won")
elif g==1:
    print(lit[g])
    if rd==0:
        print("computer choose")
        print(lit[rd])
        print("You won")
    elif rd==1:
        print("computer choose")
        print(lit[rd])
        print("its a tie")
    else:
        print("computer choose")
        print(lit[rd])
        print("You loose")
elif g==2:
    print(lit[g])
    if rd==0:
        print("computer choose")
        print(lit[rd])
        print("You loose")
    elif rd==1:
        print("computer choose")
        print(lit[rd])
        print("You won")
    else:
        print("computer choose")
        print(lit[rd])
        print("its a tie")
else:
    print("Please enter valid number i.e. 0, 1, 2 only.")
