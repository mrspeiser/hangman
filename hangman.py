import os
from sys import platform

def hangman(word):
	if platform == "linux" or platform == "linux2":
	    # linux
	    os.system('clear');
	elif platform == "darwin":
	    # OS X
	    os.system('clear');
	elif platform == "win32":
	    # Windows...
	    os.system('cls');
	    
	wrong = 0
	stages = ["",
				"__________________",
				"|                 ",
				"|        |        ",
				"|        0        ",
				"|       /|\       ",
				"|       / \       ",
				"|                 "
	]
	rletters = list(word)
	board = ["__"] * len(word)
	win = False
	print("Welcome to Hangman!");
	while wrong < len(stages):
		msg = "Guess A Letter: "
		char = input(msg)
		if char in rletters:
			cind = rletters.index(char)
			board[cind] = char
			rletters[cind] = '$'
		else:
			wrong+=1
		print((" ".join(board)))
		e = wrong + 1
		print("\n".join(stages[0:e]))
		if "__" not in board:
			print("you win!")
			print(" ".join(board))
			win = True
			break
	if not win:
		print("\n".join(stages[0: wrong]))
		print("You lose! It was {}".format(word))


word = input('Player 1 enter a word: ')
hangman(word)
