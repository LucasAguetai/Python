from random import *

mode = input("1 : 1 joueur\n2 : 2 jouers\n")

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

plateau = "1|2|3\n- - -\n4|5|6\n- - -\n7|8|9"

x=input("Voulez vous commencez ? (o or n)\n")
if mode == 1 :
	if 