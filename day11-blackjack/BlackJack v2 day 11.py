import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
computer_cards = []


def deal_card():
    return random.choice(cards)


for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


def user_sum():
    return sum(user_cards)


def computer_sum():
    return sum(computer_cards)


def checking():
    if user_sum() > 21 and 11 in user_cards:
        user_cards.remove(11)
        user_cards.append(1)
    if computer_sum() > 21 and 11 in computer_cards:
        computer_cards.remove(11)
        computer_cards.append(1)
    while computer_sum() < 17:
        computer_cards.append(deal_card())


def win_or_lose():
    if user_sum() > 21:
        print("You lose")
    elif computer_sum() == user_sum():
        print("DRAW")
    elif user_sum() == 21:
        print("You won")
    elif computer_sum() == 21:
        print("You lose")
    elif computer_sum() > 21 and user_sum() < 21:
        print("You won")
    elif user_sum() > computer_sum():
        print("You win")
    else:
        print("You lose")


def basic():
    print("Your cards:", user_cards, "current score:", user_sum())
    print("Computer first card:", computer_cards[0])


def final_check():
    print("Your cards:", user_cards, "current score:", user_sum())
    checking()
    print("Computer final cards:", computer_cards, "Computer sum:", computer_sum())
    win_or_lose()


while True:
    basic()
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if another_card == "y":
        user_cards.append(deal_card())
        if user_sum() > 21:
            final_check()
            break
    elif another_card == "n":
        checking()
        final_check()
        break
