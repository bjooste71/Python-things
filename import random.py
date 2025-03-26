import random

# Define a Card class
class Card:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

    def __lt__(self, other):
        return Card.values.index(self.value) < Card.values.index(other.value)

    def __eq__(self, other):
        return Card.values.index(self.value) == Card.values.index(other.value)


# Define a Deck class
class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in Card.suits for value in Card.values]
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop() if self.cards else None


# Define a Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self):
        return self.hand.pop(0) if self.hand else None

    def add_cards(self, cards):
        self.hand.extend(cards)

    def has_cards(self):
        return len(self.hand) > 0


# Define the Game class
class WarGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.deck = Deck()
        self.deal_cards()

    def deal_cards(self):
        while len(self.deck.cards) > 0:
            self.player1.add_cards([self.deck.draw()])
            self.player2.add_cards([self.deck.draw()])

    def play_round(self):
        if not self.player1.has_cards() or not self.player2.has_cards():
            return

        card1 = self.player1.draw_card()
        card2 = self.player2.draw_card()

        print(f"{self.player1.name} plays: {card1}")
        print(f"{self.player2.name} plays: {card2}")

        if card1 > card2:
            print(f"{self.player1.name} wins the round!")
            self.player1.add_cards([card1, card2])
        elif card1 < card2:
            print(f"{self.player2.name} wins the round!")
            self.player2.add_cards([card1, card2])
        else:
            print("It's a tie! Initiating war...")
            self.initiate_war([card1, card2])

    def initiate_war(self, war_cards):
        if len(self.player1.hand) < 4 or len(self.player2.hand) < 4:
            return

        war_cards.extend([self.player1.draw_card() for _ in range(3)])
        war_cards.extend([self.player2.draw_card() for _ in range(3)])

        self.play_round()

        if self.player1.has_cards() and self.player2.has_cards():
            new_card1 = self.player1.draw_card()
            new_card2 = self.player2.draw_card()

            print(f"{self.player1.name} plays: {new_card1}")
            print(f"{self.player2.name} plays: {new_card2}")

            war_cards.extend([new_card1, new_card2])

            if new_card1 > new_card2:
                print(f"{self.player1.name} wins the war!")
                self.player1.add_cards(war_cards)
            elif new_card1 < new_card2:
                print(f"{self.player2.name} wins the war!")
                self.player2.add_cards(war_cards)
            else:
                self.initiate_war(war_cards)

    def is_game_over(self):
        return not self.player1.has_cards() or not self.player2.has_cards()

    def get_winner(self):
        if len(self.player1.hand) > len(self.player2.hand):
            return self.player1.name
        elif len(self.player1.hand) < len(self.player2.hand):
            return self.player2.name
        else:
            return "It's a tie!"


# Example of running the game
if __name__ == "__main__":
    game = WarGame("Alice", "Bob")

    while not game.is_game_over():
        game.play_round()

    print(f"The winner is: {game.get_winner()}")
