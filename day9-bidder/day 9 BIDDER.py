from replit import clear


def find_highest_bidder(bulding_record):
    highest_bid = 0
    winner = ""
    for bidder in bulding_record:
        bid_amount = bulding_record[bidder]
        if int(bid_amount) > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print("the winner is", winner)


while True:
    y = input("What's your bid?: ")
    x = input("What is your name?: ")
    m = input("Are there any other bidders?: ")
    dic = {}
    dic[x] = y  # dic x ir vienads ar y sanak - marus:125
    if m == "no":
        find_highest_bidder(dic)
        break
    else:
        clear()
