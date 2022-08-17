from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.
print(art.logo)
bids = {}

def new_bid(name_of_bidder, bid_made):
  bids[name] = bid_made

def highest_bidder():
  name = ""
  bid = 0
  for bidders in bids:
    if bids[bidders] > bid:
      bid = bids[bidders]
      name = bidders
  print(f"Highest bidder is {name} with the bid of ${bid}")

running = True
while running == True:
  name = input("What is your name: ")
  bid = int(input(f"How much would you like to bid {name}: "))
  new_bid(name,bid)
  others = input("Anymore bidders? (yes/no): ").lower()
  if others == "no":
    running = False
    highest_bidder()
  else:
    clear()


  
  
  
