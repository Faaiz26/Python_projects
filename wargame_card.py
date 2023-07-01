from random import shuffle

#Two usefull variables for creating cards

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()




"""

my_cards = [(s,r) for s in SUITE for r in RANKS]
my_cards = []

for r in RANKS:
    for s in SUITE:
        my_cards.append((s,r))

print(my_cards)
"""




class Deck:
    """
    THis object will create a deck of cards to initiate player.
    
    """
    def __init__(self) -> None:
        print("Creating New Ordered Deck")
        self.all_cards = [(s,r) for s in SUITE for r in RANKS]
    
    def shuffle(self):
        print("Shuffling DECK")
        shuffle(self.all_cards)

    def split_in_half(self):
        return(self.all_cards[:26],self.all_cards[26:])
    

class Hand:
    def __init__(self,cards):
        self.cards = cards
    def __str__(self):
        return("Contains {} cards").format(len(self.cards)) #number of cards in player hand 
    
    def add(self,added_cards):
        self.cards.extend(added_cards) #adding cards to hand
    
    def remove_cards(self):
        return(self.cards.pop()) #removing cards from hand


class Player:
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_Card = self.hand.remove_cards()
        print("{} has placed: {}".format(self.name,drawn_Card))
        print("\n")
        return(drawn_Card)

    def remove_war_cards(self):
        war_cards = []
        for x in range(3):
            war_cards.append(self.hand.cards.pop())
        return(war_cards)
        
    def still_has_cards(self):
        """
        Return Truer if player has any cards left
        """
        return(len(self.hand.cards) > 0)    # retun (len(self.hand.cards) != 0)
    

print("Welcome to Game")


#create a new deck and split it into half:
d = Deck()
d.shuffle()
half_1 , half_2 = d.split_in_half()

#create two players

computer_player = Player(name = "computer_player",hand = Hand(half_1))

name = input("Please enter your name: ")

user = Player(name,Hand(half_2))


total_rounds = 0
war_counts = 0


while user.still_has_cards() and computer_player.still_has_cards():
    total_rounds += 1
    print("Time for new round")

    print("Current standings")

    print(user.name+" has the counts : "+ str(len(user.hand.cards)))
    print(computer_player + " has the counts : "+ str(len(computer_player.hand.cards)))

    print("play a card")
    print("\n")

    table_cards = []

    c_card = computer_player.play_card()
    p_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:  #checking computer card ranking with player card ranking
        war_counts  += 1

        print('War')

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(computer_player.remove_war_cards())

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            computer_player.hand.add(table_cards)
    
    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            computer_player.hand.add(table_cards)

print("game over, number of rounds :" + str(total_rounds))
print("a war happened " + str(war_counts) + " times")




    