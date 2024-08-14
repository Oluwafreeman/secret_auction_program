from art import logo

def compare(auction):
    highest_bid = 0
    for bidder in auction:
        if auction[bidder] > highest_bid:
            highest_bid = auction[bidder]
            winner = bidder
    print(f"The winner is {winner}, with a bid of {highest_bid}")

print(logo)
bids = {}

bidding_finished = False
while not bidding_finished:
    name = input("What's your name?: ")
    bid = int(input("What's your bid: $"))

    bids[name] = bid
    answer = input("Is there any other bidders around?\n").lower()
    if answer == "no":
        bidding_finished = True
compare(bids)

