from random import *

def random_letter(rep) :
	"""
	Set a string of characters and add a letter in uppercase or lowercase of the ASCII table
	"""
	if randint(1,2) == 1 :
		rep = rep+chr(randint(97, 122))
	else :
		rep = rep+chr(randint(65, 90))
	return rep

def random_sign(rep):
	"""
	Set a string of characters and add a special character to it at random from the ASCII table
	"""
	random = randint(1, 3)
	if random == 1 :
		rep = rep+chr(randint(33, 47))
	elif random == 2 :
		rep = rep+chr(randint(91, 95))
	else :
		rep = rep+chr(randint(123, 126))
	return rep

#Verifies user input
type_mdp = ""
while type_mdp != "1" and type_mdp != "2" and type_mdp != "3" :
	#Retrieves the password settings
	type_mdp = input("Quelle type de mdp souhaitez vous ?\n   1 : Seulement des lettres\n   2 : Lettres et chiffres\n   3 : Lettre, chiffre et caractère spéciaux ?\n")

nb = int(input("Vous voulez un mdp de combien de caractère ? "))
rep = ""

if type_mdp == "1" :
	#If the user wants letters, the random_letter function is invoked
	while len(rep)<nb :
		rep = random_letter(rep)
elif type_mdp == "2" :
	#If the user wants letters and numbers, either randomly call the random_letter 
	#function or randomly pick a number
	while len(rep)<nb :
		if randint(1,2) == 1 :
			rep += str(randint(0, 9))
		else :
			rep = random_letter(rep)
else :
	#If the user wants letters, numbers and special characters, either random_letter is called, 
	#or a random number is called, or random_sign is called
	while len(rep)<nb :
		random = randint(1,3)
		if random == 1 :
			rep += str(randint(0, 9))
		elif random == 2 :
			rep = random_letter(rep)
		else :
			rep = random_sign(rep)

print("Votre mot de passe est : "+rep)