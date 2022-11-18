import random
from art import logo


############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

###############################################################

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
current_score = 0
dealer_score = 0
player_cards = []
dealer_cards = []


def deal_card():
    return cards[random.randint(0, 12)]


def print_scores(player_cards, current_score, dealer_cards, dealer_score):
    print(
        f"  Your final hand: {player_cards}, current score: {current_score}")
    print(
        f"    Computer's final hand: {dealer_cards}, final score: {dealer_score}")


playing = True

print(logo)


def black_jack():

    for i in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())

    wantHit = True
    dealer_deal = True
    while wantHit:
        current_score = sum(player_cards)
        dealer_score = sum(dealer_cards)
        if current_score > 21 and 11 in player_cards:
            ace_index = player_cards.index(11)
            player_cards[ace_index] = 1
            current_score = sum(player_cards)
        elif current_score > 21:
            print_scores(player_cards, current_score,
                         dealer_cards, dealer_score)
            print("You went over. You lose")
            wantHit = False
            dealer_deal = False
            continue
        elif current_score == 21 and len(player_cards) == 2:
            if dealer_score == 21 and len(dealer_cards) == 2:
                print_scores(player_cards, current_score,
                             dealer_cards, dealer_score)
                print("You both had blackjack it's a draw.")

            else:
                print_scores(player_cards, current_score,
                             dealer_cards, dealer_score)
                print("BLACK JACK! YOU WIN!!")
            wantHit = False
            dealer_deal = False
            continue

        print(
            f"    Your cards: {player_cards}, current score: {current_score}")
        print(f"    Computer's first card: {dealer_cards[0]}")
        hit = input(
            "Type 'y' to get another card, type 'n' to pass: ").lower()
        if hit == "n":
            wantHit = False
            continue
        player_cards.append(deal_card())

    while dealer_deal:
        dealer_score = sum(dealer_cards)
        if dealer_score > 21 and 11 in dealer_cards:
            ace_index = dealer_cards.index(11)
            dealer_cards[ace_index] = 1
            dealer_score = sum(dealer_cards)
        elif dealer_score == 21 and len(dealer_cards) == 2:
            print_scores(player_cards, current_score,
                         dealer_cards, dealer_score)
            print("Dealer had blackjack. You lose")
            break
        elif dealer_score > 21:
            print_scores(player_cards, current_score,
                         dealer_cards, dealer_score)
            print("Dealer busts. You Win!")
            break
        elif dealer_score >= 17:
            if current_score > dealer_score:
                print_scores(player_cards, current_score,
                             dealer_cards, dealer_score)
                print("You Win!")
                break
            elif current_score == dealer_score:
                print_scores(player_cards, current_score,
                             dealer_cards, dealer_score)
                print("Draw!")
                break
            else:
                print_scores(player_cards, current_score,
                             dealer_cards, dealer_score)
                print("You lose")
                break

        dealer_cards.append(deal_card())
        dealer_score = sum(dealer_cards)


while playing:
    black_jack()
    play_again = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play_again == "n":
        playing = False
        continue
    player_cards = []
    dealer_cards = []
    current_score = 0
    dealer_score = 0
