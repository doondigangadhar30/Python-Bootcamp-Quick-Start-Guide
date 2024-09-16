from art import logo
print(logo)

def highest_bid():
    h = (max(clients,key=clients.get))
    print(f"dear {h} is the Auction winner, and their biding price is ${clients[h]}.")
def project():
    a=input("Enter your name: ")
    b=int(input("Enter your bid: $"))
    clients[a]=b
    c=input("is there any others y or n: ").lower()
    if c=='n':
        highest_bid()
    else:
        print("\n"*45)
        project()
clients={}
project()
