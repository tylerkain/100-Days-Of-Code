print("Welcome to the Secret Auction:")

bids = {}
bidding = False

while not bidding:
    bid_name = input("input your name: ").lower()
    bid = int(input("Bid amount: "))
    bids[bid_name] = bid

    done = input("are you finished y/n: ")

    if done == 'y':
        bidding = True

print(bids)


def wining_bid(bid):
    winning_bid = 0
    winner = ""
    for bidder in bid:
        bid_amount = bid[bidder]
        if bid_amount > winning_bid:
            winning_bid = bid_amount
            winner = bidder
    print(f"winner is {winner} with {winning_bid}")


wining_bid(bids)
