#HINT: You can call clear() to clear the output in the console.
from replit import clear
from art import logo

print(logo + "\n" + "Welcome to the secret auction program.")

def find_highest_bid(auction_bids, auction_highest_bidder):
    for index in range(0, len(bids)):
        if auction_bids[index]['potential_buyer_bid'] > auction_highest_bidder['buyer_bid']:
            auction_highest_bidder['buyer_name'] = auction_bids[index]['potential_buyer_name']
            auction_highest_bidder['buyer_bid'] = auction_bids[index]['potential_buyer_bid']
    return auction_highest_bidder

bid_is_on = True
# bids = [{}]
# bids = [{

# }]
bids = []
highest_bidder = {}

while bid_is_on:
    name = input("What is your name?: ")
    # bid = float(input("What is your bid?: £"))
    bid = float(input("What is your bid?: £"))

    bids.append(
        {
            'potential_buyer_name': name, 
            'potential_buyer_bid': bid
        }
    )

    if len(highest_bidder) == 0:
        highest_bidder['buyer_name'] = name
        highest_bidder['buyer_bid'] = bid
    
    more_bids = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if more_bids.lower() == "yes":
        clear()
    elif more_bids.casefold() == "no":
        bid_is_on = False
        winner = find_highest_bid(bids, highest_bidder)
else:
    print(f"The winner is {winner['buyer_name']} with a bid of £{winner['buyer_bid']}")

# consider breaking down larger programs such as this into
# smaller parts in order to tackle each little bit one by one -
# step-by-step using a flowchart
