import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
card_values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    def __init__(self,suit,rank):
        
        try:
            self.suit = suit
            self.rank = rank
            self.value = card_values[rank]

        except:
            print('The rank you have entered is not correct')

    def __str__(self):
        return self.rank + ' of ' + self.suit
    

    randomnr = random.randrange(1,52)

    randomnr