import random

class Deck:
	ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
	suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
	values = [1,2,3,4,5,6,7,8,9,10,10,10,10]
	deck = []

	def __init__(self):
		deck_key = 1
		values_index = 0
		for rank in self.ranks:
			for suit in self.suits:
				card_name = rank + " of " + suit
				self.deck.append([card_name,self.values[values_index]])
				deck_key += 1
			values_index += 1
		random.shuffle(self.deck)
	
	def deal(self):
		card = self.deck.pop(0)
		random.shuffle(self.deck)
		return card

	def make_play(self):
		return self.deal()

	def printCards(self, cards):
		statement = "Your cards are the"
		for card in cards:
			statement += " " + card + "," 
		return statement


start = input("Welcome! Type \"Start\" to start! : ")
game = Deck()
player_cards = []
player_value = 0
dealer_cards = []
dealer_value = 0

if(start == "Start"):
	for i in range(2):
		dealer_card = game.deal()
		dealer_cards.append(dealer_card[0])
		dealer_value += dealer_card[1]

		player_card = game.deal()
		player_cards.append(player_card[0])
		player_value += player_card[1]

	print(game.printCards(player_cards))
	print(player_value)

	action = input("Would you like to Hit (H) or Stand (S)? : ")
	if(action == "H"):
		card = game.make_play()
		player_cards.append(card[0])
		player_value += card[1]
		
	print(player_cards)
	print(player_value)


