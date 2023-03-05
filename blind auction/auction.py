import os
import art

print(art.logo)
bid_dictionary = {}

def bidding():
    name = input("What's your name?\n").capitalize()
    bid = int(input("Kaç yatırıyorsun?:\n$"))
    bid_dictionary[name] = bid

bidding_end = False
while not bidding_end:
    bidding()
    answer = input("Başka teklif var mı? Yes or No yazın\n").lower()
    os.system('clear')
    winner = max(bid_dictionary, key=bid_dictionary.get)
    winner_bid = max(bid_dictionary.values())
    if answer == "no":
        bidding_end = True
        print(f"The winner is {winner} with a bid of ${winner_bid}")