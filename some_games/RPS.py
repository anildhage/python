# Rock paper scissors game
def rps():
	import random

	t = ['rock', 'paper', 'scissors']
	computer = t[random.randint(0,2)]
	player = False

	while player == False:
		player = input("rock, paper, scissors?")
		if player == computer:
			print("Tie!")
		elif player == 'rock':
			if computer == 'paper':
				print("You lose", computer, "covers", player)
			else:
				print("You Win", player, "smashes", computer)
		elif player == 'paper':
			if computer == 'scissors':
				print("You lose", computer, "cuts", player)
			else:
				print("You Win", player, "covers", computer)
		elif player == 'scissors':
			if computer == 'rock':
				print("You lose", computer, "smashes", player)
			else:
				print("You Win", player, "cuts", computer)
		else:
			print("Thats not a valid play, check your spelling!")
		player = False
		computer = t[random.randint(0,2)]

rps()




