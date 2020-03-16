### IMPORT STATEMENTS AND VARIABLE DECLARATIONS: ###

import random
import os
import time

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

### CLASS DEFINTIONS: ###

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return (f"{self.rank:>5} of {self.suit:^}")


class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank)) # uses Card class to create all 52 cards in a deck
    
    def __str__(self):
        full_deck = ""
        count = 0
        for card in self.deck:
            count +=1
            full_deck += f"\n{count}. " + card.__str__()
        return "In the deck: " + full_deck

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        deal_card = self.deck.pop()
        return deal_card


class Hand:

    def __init__(self):
        self.hand = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.hand.append(card)
        self.value += values[card.rank]
        
        # check if ace is added
        if card.rank == "Ace":
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    
    def __init__(self, total=100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet



### FUNCTION DEFINITIONS: ####

def take_bet(chips):
    os.system("clear")
    print("Current chips: ", chips.total)
    while True:

        try:          
            chips.bet = int(input("\nWhat would you like to bet?\n[10,20,50,100] "))
            if chips.bet not in [10,20,50,100]:
                print("Invalid bet")
                continue
        except ValueError:
            os.system("clear")
            print("Please input an integer... ")
        else:
            if chips.bet > chips.total:
                print("Uh-oh!\nNot enough chips. You have ", chips.total)
            else:
                break

def hit(deck,hand):
    print("\nDealing...")
    time.sleep(2)
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        player_move = input("What would you like to do, Hit or Stand?...\nEnter 'h' or 's': ")
        
        if player_move[0].lower() == "h":
            hit(deck,hand)
            break
            
        elif player_move[0].lower() == "s":
            playing = False
            break
            
        else:
            print("\nPlease enter 'h' or 's'... ")
            continue

def show_some(player,dealer):
    os.system("clear")
    print("\nDealer's hand:\n\n",dealer.hand[0],"\n <card face down>")
    print("\n","="*15)
    print("\nYour hand:\n", *player.hand, sep="\n ")
    print("\nYour current score = ", player.value, "\n\n")
    
def show_all(player,dealer):
    os.system("clear")
    print("\nDealer's hand:\n", *dealer.hand, sep="\n")
    print("\nDealer's score = ", dealer.value)
    print("="*15)
    print("\nYour hand:\n", *player.hand, sep="\n")
    print("\nYour score = ", player.value, "\n\n")

def player_busts(player, dealer, chips):
    print("Unlucky! You bust :(")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("Congradualtions!! You win! :D")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("Congradualtions! The dealer busted! You win! :D")
    chips.win_bet()
    
def dealer_wins(player, dealer, chips):
    print("Unlucky! Dealer wins :(")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")



### THE GAME ###
def main():
    global playing
    # playing = True

    # Print an opening statement
    os.system("clear")
    print("--Welcome to BlackJack--")

    # Set up the Player's chips
    player_chips = Chips()
    print(f"\nYou have {player_chips.total} starting chips")

    while True:
        
        # Create & shuffle the deck
        print("Shuffling deck...")
        time.sleep(3)
        deck = Deck()
        deck.shuffle()

        # Prompt the Player for their bet
        take_bet(player_chips)

        os.system("clear")
        print("Dealing cards...")
        time.sleep(2)

        # Create player and dealer
        player_hand = Hand()
        dealer_hand = Hand()
        # Like standard poker, player gets card, then dealer
        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())
            
        # Show cards (but keep one dealer card hidden)

        show_some(player_hand, dealer_hand)
        
        while playing:
            
            # Prompt for Player to Hit or Stand
            hit_or_stand(deck, player_hand)
            
            # Show cards (but keep one dealer card hidden)
            show_some(player_hand, dealer_hand)
            
            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand, player_chips)
                break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player_hand.value <= 21:
            show_all(player_hand, dealer_hand)
            time.sleep(1)
            
            while dealer_hand.value < 17 and dealer_hand.value < player_hand.value:
                hit(deck, dealer_hand)
                # Shows all cards everytime the dealer draws a new card
                show_all(player_hand, dealer_hand)
                time.sleep(1)
                if dealer_hand.value > 17 and dealer_hand.value < 21:
                    print("Dealer is thinking...")
                    time.sleep(3)
        
            # Show all cards
            show_all(player_hand, dealer_hand)
            
            # Run different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)
                
            elif player_hand.value < dealer_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
                
            elif player_hand.value > dealer_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)
                
            else:
                push(player_hand,dealer_hand) 
        
        # Inform Player of their chips total
        print(f"\nYou have {player_chips.total} chips left")
        
        # Ask to play again
        new_game = input("\nWould you like to play another hand? Enter 'y' or 'n' ")
        
        if new_game[0].lower()=='y':
            playing=True
            continue
        else:
            print("\n\nThanks for playing!")
            break



if __name__ == '__main__':
    main()