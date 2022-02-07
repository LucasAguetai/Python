from random import *

mode = int(input("1 : 1 joueur\n2 : 2 jouers\n"))
if mode == 2 :
	player1 = input("Quelle est le nom du joueur 1 ? (X) ")
	player2 = input("Quelle est le nom du joueur 2 ? (O) ")
else :
	player1 = input("Quelle est votre nom ? ")
	player2 = "L'ordinateur"

def game(plateau, case, symbole) :
	new_plateau = ""
	i=0
	while i<len(plateau) :
		if plateau[i] == case :
			new_plateau += symbole
		else :
			new_plateau += plateau[i]
		i+=1
	return new_plateau

def win(plateau, case) :
	res = 0
	if not (plateau[0] == case and plateau[2] == case and plateau[4] == case) :
		res += 1
		if not (plateau[0] == case and plateau[12] == case and plateau[24] == case) :
			res += 1
			if not (plateau[0] == case and plateau[14] == case and plateau[28] == case) :
				res += 1
				if not (plateau[4] == case and plateau[12] == case and plateau[24] == case) :
					res += 1
					if not (plateau[4] == case and plateau[16] == case and plateau[28] == case) :
						res += 1
						if not (plateau[24] == case and plateau[26] == case and plateau[28] == case) :
							res += 1
							if not (plateau[2] == case and plateau[14] == case and plateau[26] == case) :
								res += 1
	if res == 7 :
		return False
	else :
		return True

plateau = "1|2|3\n- - -\n4|5|6\n- - -\n7|8|9"
if mode == 1 :
	x=input("Voulez vous commencez ? (o or n)\n")
	if x == "o" or x == "O" :
		player = 1
	else :
		player = 2
else :
	x=input(player1 + ", voulez vous commencez ? (o or n)\n")
	if x == "o" or x == "O" :
		player = 1
	else :
		player = 2

rounds = 0
end = ""
while end != "end" :
	if mode == 1 :
		if player == 1 :
			print("Quelle case voulez-vous jouez ?\n")
			case = input(plateau + "\n")
			plateau = game(plateau, case, "X")
			player = 2
		else :
			ordi = randint(1, 9)
			while str(ordi) not in plateau :
				ordi = randint(1, 9)
			plateau = game(plateau, str(ordi), "O")
			player = 1
		rounds += 1

	elif mode == 2 :
		if player == 1 :
			print(player1 + ", quelle case voulez-vous jouez ?\n")
			case = input(plateau + "\n")
			plateau = game(plateau, case, "X")
			player = 2
		else :
			print(player2 + ", quelle case voulez-vous jouez ?\n")
			case = input(plateau + "\n")
			plateau = game(plateau, case, "O")
			player = 1
		rounds += 1

	if rounds == 9 :
		print(plateau + "\nÉgalité !")
		end = "end"

	if win(plateau, "O") :
		print(plateau)
		print(player2 + " a gagné !")
		end = "end"
	elif win(plateau, "X") :
		print(player1 + " a gagnez !")
		end = "end"