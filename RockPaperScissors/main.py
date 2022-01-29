from random import *

#I ask the name of the player and the number of games he wants to play
name = input("Quelle est votre nom ?\n")
print("Jouons à un jeu : le pierre feuille ciseaux! Les règles sont très simples, la pierre bat les ciseaux, les ciseaux battent la feuille, et la feuille bat la pierre !")
nb = input("Combien de partie voulez vous faire ?\n")
print("Vous voulez faire "+nb+" partie ? très bien, bonne chance !")

scoreUser = 0
scoreComputer = 0
game = ["pierre", "feuille", "ciseaux"]
nbround = 0
while nbround<int(nb) :
	#I ask what he wants to play
	user = int(input("Que souhaitez vous jouez ?\n   1 : La pierre\n   2 : La feuille\n   3 : Le ciseaux\n"))
	com = randint(1, 3)
	print(name + " : " + game[user-1])
	print("Ordi : " + game[com-1])
	#The result is checked with a calculation
	if user-1 == com or user-1 == com-3 :
		scoreUser += 1
		print("Bravo "+name+", vous avez gagnez !\n"+str(scoreUser)+"-"+str(scoreComputer))
	elif user+1 == com or user+1 == com+3:
		scoreComputer += 1
		print("Dommage, vous avez perdu !\n"+str(scoreUser)+"-"+str(scoreComputer))
	else :
		print("Égalité ! le score reste donc à "+str(scoreUser)+"-"+str(scoreComputer))
	nbround +=1

#I display the result
if scoreUser > scoreComputer :
	print("Bravo " + name + ", vous avez gagnez "+str(scoreUser)+"-"+str(scoreComputer))
elif scoreComputer > scoreUser :
	print("Dommage, vous avez perdu "+str(scoreUser)+"-"+str(scoreComputer))
else :
	print("Joli match ! vous êtes égalité à "+str(scoreUser)+"-"+str(scoreComputer))