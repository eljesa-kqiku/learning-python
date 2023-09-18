import art
import os

bidders = []


def add_user():
    name = input('What is your name?: ')
    amount = int(input('What is your bid?: '))
    bidders.append({
        "name": name,
        "amount": amount
    })


print(art.logo)
done = False
while not done:
    add_user()
    another_bidder = input('Are there any other bidders? Type "yes" or "no": ')
    os.system('cls' if os.name == 'nt' else 'clear')
    if another_bidder == 'no':
        done = True

max_bidder = bidders[0]
for person in bidders:
    if person["amount"] > max_bidder["amount"]:
        max_bidder = person

print(f"\nThe winner is {max_bidder['name']} with a bid of {max_bidder['amount']}")