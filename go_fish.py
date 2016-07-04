import random

deck = ['ace', 'ace', 'ace', 'ace', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4', '5', '5', '5', '5', '6', '6', '6', '6', '7', '7', '7', '7', '8', '8', '8', '8', '9', '9', '9', '9', '10', '10', '10', '10', 'jack', 'jack', 'jack', 'jack', 'queen', 'queen', 'queen', 'queen', 'king', 'king', 'king', 'king']
my_hand = []
opponent_hand = []
exit = False

def draw(cards, owner):
	if len(deck) >= cards:
		for i in range(0, cards):
			drawn_card = deck.pop((int)(random.random() * len(deck)))
			owner.append(drawn_card)
			if owner == my_hand:
				print "You drew a %r." % drawn_card
			else:
				print "Your opponent drew a card."
	else:
		print "No more cards in the deck."
		if not my_hand and not opponent_hand:
			exit = True
	print "Your hand:", my_hand

	
		
def start_game():
	draw(7, my_hand)
	draw(7, opponent_hand)
	my_score = 0
	opponent_score = 0
	exit = False
	while(not exit):
		while(not exit):
			l = 0
			n = len(opponent_hand) - 1
			m = len(my_hand) - 1
			while(l < m):      #checks hand for duplicates
				while(l < m):
					if my_hand[l] == my_hand[m]:
						print "You have a pair of %rs." % my_hand[m]
						my_hand.pop(m)
						my_hand.pop(l)
						my_score += 1
						m = len(my_hand) - 1
						print my_hand
					m -= 1
				m = len(my_hand) - 1
				l += 1
			l = 0
			while(l < n):	#checks opponent's hand for duplicates
				while(l < n):
					if opponent_hand[l] == opponent_hand[n]:
						print "Your opponent has a pair of %rs." % opponent_hand[n]
						opponent_hand.pop(n)
						opponent_hand.pop(l)
						opponent_score += 1
						n = len(opponent_hand) - 1
					n -= 1
				n = len(opponent_hand) - 1
				l += 1
			
			if not my_hand:
				draw(1, my_hand)
				draw(1, my_hand)
				
			if not opponent_hand:
				draw(1, opponent_hand)
				draw(1, opponent_hand)
			
			print "Choose a card from your hand to ask the opponent or 'exit' to exit."
			while True:
				t = raw_input()
				if t.lower() in my_hand: break
				if t.lower() == "exit": 
					exit = True
					print "You will now exit the game."
					break
				print "Sorry, you didn't choose a card from your hand."
				
			if exit == True: break
			if t.lower() in opponent_hand:
				print "Your opponent gives you a %r." % t.lower()
				opponent_hand.remove(t.lower())
				my_hand.append(t.lower())
			else:
				print "Go fish!"
				draw(1, my_hand)
			
			if exit == True: break
			
			y = (int)(random.random()*len(opponent_hand))
			print "Your opponent asks for a", opponent_hand[y],"."
			if opponent_hand[y] in my_hand:
				my_hand.remove(opponent_hand[y])
				opponent_hand.append(opponent_hand[y])
				
	print "Your score:", my_score
	print "Your opponent's score:", opponent_score
	if my_score > opponent_score:
		print "Congratulations! You won!"
	
	elif opponent_score > my_score:
		print "You suck! Your opponent won!"
	
	elif opponent_score == my_score:
		print "You tied! Bummer!"
			
			

start_game()

