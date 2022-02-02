from random import *

mode = int(input("1 : 1 joueur\n2 : 2 jouers\n"))

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
	if not (plateau[1] == "case" and plateau[3] == "case" and plateau[5] == "case") :
		res += 1
		if not (plateau[1] == "case" and plateau[13] == "case" and plateau[25] == "case") :
			res += 1
			if not (plateau[1] == "case" and plateau[15] == "case" and plateau[29] == "case") :
				res += 1
				if not (plateau[5] == "case" and plateau[13] == "case" and plateau[25] == "case") :
					res += 1
					if not (plateau[5] == "case" and plateau[17] == "case" and plateau[29] == "case") :
						res += 1
						if not (plateau[25] == "case" and plateau[27] == "case" and plateau[29] == "case") :
							res += 1
	if res == 6 :
		return False
	else :
		return True

plateau = "1|2|3\n- - -\n4|5|6\n- - -\n7|8|9"

x=input("Voulez vous commencez ? (o or n)\n")
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

		if rounds == 9 :
			print(plateau + "\nÉgalité !")
			end = "end"

		if win(plateau, "O") :
			print("L'ordinateur a gagné !")
			end = "end"
		elif win(plateau, "X") :
			print("Vous avez gagnez !")
			end = "end"