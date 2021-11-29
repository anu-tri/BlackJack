import random
import os

class BlackJack():
    def __init__(self):
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

    def deal(self):
        hand = []
        for i in range(2):
            random.shuffle(self.deck)
            card = self.deck.pop()
            if card == 11:card = "J"
            if card == 12:card = "Q"
            if card == 13:card = "K"
            if card == 14:card = "A"
            hand.append(card)
        return hand

    def play_again(self):
        response = input("Do you want to play again? (Y/N) : ").lower()
        if response == "y":
            dealer_hand = []
            player_hand = []
            deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
            self.game()
        else:
            exit()

    def total(self,hand):
        total = 0
        for card in hand:
            if card == "J":
                total += 11
            elif card == "Q":
                total += 12
            elif card == "K":
                total += 13
            elif card == "A":
                if total >= 11: 
                    total+= 1
                else: 
                    total+= 11
            else:
                total += card
        return total

    def hit(self,hand):
        card = self.deck.pop()
        if card == 11:card = "J"
        if card == 12:card = "Q"
        if card == 13:card = "K"
        if card == 14:card = "A"
        hand.append(card)
        return hand

    def clear(self):
        os.system('CLS')

    def show_results(self,dealer_hand, player_hand):
        self.clear()
        print("The dealer has a " + str(dealer_hand) + " for a total of " + str(self.total(dealer_hand)))
        print("You have a " + str(player_hand) + " for a total of " + str(self.total(player_hand)))

    def blackjack(self, dealer_hand, player_hand):
        if self.total(player_hand) == 21:
            self.show_results(dealer_hand, player_hand)
            print("Congratulations! You got a Blackjack!\n")
            self.play_again()
        elif self.total(dealer_hand) == 21:
            self.show_results(dealer_hand, player_hand)		
            print("Sorry, you lose. The dealer got a blackjack.\n")
            self.play_again()


    def score(self,dealer_hand, player_hand):
        if self.total(player_hand) == 21:
            self.show_results(dealer_hand, player_hand)
            print("Congratulations! You got a Blackjack!\n")
        elif self.total(dealer_hand) == 21:
            self.show_results(dealer_hand, player_hand)
            print("Sorry, you lose. The dealer got a blackjack.\n")
        elif self.total(player_hand) > 21:
            self.show_results(dealer_hand, player_hand)
            print("Sorry. You busted. You lose.\n")
        elif self.total(dealer_hand) > 21:
            self.show_results(dealer_hand, player_hand)
            print("Dealer busts. You win!\n")
        elif self.total(player_hand) < self.total(dealer_hand):
            self.show_results(dealer_hand, player_hand)
            print("Sorry. Your score isn't higher than the dealer. You lose.\n") 
        elif self.total(player_hand) > self.total(dealer_hand):
            self.show_results(dealer_hand, player_hand)
            print("Congratulations. Your score is higher than the dealer. You win\n")

    def game(self):
        response = 0
        os.system('CLS')
        print("\nWelcome to BLACKJACK!\n")
        dealer_hand = self.deal()
        player_hand = self.deal()
        while response != "q":
            print("The dealer is showing a " + str(dealer_hand[0]))
            print("You have a " + str(player_hand) + " for a total of " + str(self.total(player_hand)))
            self.blackjack(dealer_hand, player_hand)
            response = input("Do you want to Hit(H), Stand(S), or Quit(Q): ").lower()
            self.clear()
            if response == "h":
                self.hit(player_hand)
                while self.total(dealer_hand) < 17:
                    self.hit(dealer_hand)
                self.score(dealer_hand, player_hand)
                self.play_again()
            elif response == "s":
                while self.total(dealer_hand) < 17:
                    self.hit(dealer_hand)
                self.score(dealer_hand, player_hand)
                self.play_again()
            elif response == "q":
                exit()
            
BlackJack().game()