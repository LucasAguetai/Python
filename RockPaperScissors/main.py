from random import *

name = input("Quelle est votre nom ?")
print("Jouons à un jeu : Le pierre feuille ciseaux. Les règles sont très simple, la piere bat les ciseaux, les ciseaux bat la feuille, et la feuille bat la pierre !")
nb = input("Combien de partie voulez vous faire ?\n")
print("Vous voulez faire "+nb+" partie ? très bien, bonne chance !")

scoreUser = 0
scoreComputer = 0
game = ["pierre", "feuille", "ciseaux"]
nbround = 0
while nbround<int(nb) :
	user = int(input("Que souhaitez vous jouez ?\n   1 : La pierre\n   2 : La feuille\n   3 : Le ciseaux\n"))
	com = randint(1, 3)
	print(name + " : " + game[user-1])
	print("Ordi :" + game[com-1])
	if user-1 == com :
		scoreUser += 1
		print("Bravo "+name+", vous avez gagnez !\n"+scoreUser+"-"+scoreComputer)
	elif user+1 == com :
		scoreComputer += 1
		print("Dommage, vous avez perdu !\n"+scoreUser+"-"+scoreComputer)