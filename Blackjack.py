class Deck:
	ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
	suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
	values = [1,2,3,4,5,6,7,8,9,10,10,10,10]
	deck = {}

	def __init__(self):
		deck_key = 1
		values_index = 0
		for rank in self.ranks:
			for suit in self.suits:
				card_name = rank + " of " + suit
				# self.deck.append([card_name,self.values[values_index]])
				self.deck[deck_key] = [card_name, self.values[values_index]]
				deck_key += 1

			values_index += 1

		print(self.deck)

Deck()