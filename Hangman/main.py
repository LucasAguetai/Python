from random import *

food = ["burger", "tomate", "salade", "ognion", "steak", "avocat", "pate", "riz", "poulet", "surimi", "pizza", "frites", "couscous", "flan", "fromage", "fraise", "pomme", "poire", "cerise", "cornichon", "snickers"]
animals = ["cochon", "chat", "chien", "poule", "cheval", "poney", "tortue", "lapin", "hamster", "singe", "serpent", "lion", "zebre", "tigre", "agneau", "vache", "mouton", "crocodile", "giraffe"]
other = ["chaise", "table", "ordinateur", "telephone", "cable", "cousin", "canape", "masque", "pull", "pantalon", "ecran", "bouteille", "bonnet", "lit", "feuille", "lunette", "fenetre", "tramway", "metro", "metre", "bus", "train", "horloge", "ocean", "jeux", "foot", "badminton", "sac", "trousse", "cahier", "ville", "immeuble", "fille", "garcon", "polo", "ampoule", "projecteur", "gravier", "stylo", "micro", "logiciel", "courier", "gras", "poussiere", "main", "ventre", "surligneur", "lettre", "chiffre", "fichier", "dossier"]
tout = ["burger", "tomate", "salade", "ognion", "steak", "avocat", "pate", "riz", "poulet", "surimi", "pizza", "frites", "couscous", "flan", "fromage", "fraise", "pomme", "poire", "cerise", "cornichon", "snickers", "cochon", "chat", "chien", "poule", "cheval", "poney", "tortue", "lapin", "hamster", "singe", "serpent", "lion", "zebre", "tigre", "agneau", "vache", "mouton", "crocodile", "giraffe", "chaise", "table", "ordinateur", "telephone", "cable", "cousin", "canape", "masque", "pull", "pantalon", "ecran", "bouteille", "bonnet", "lit", "feuille", "lunette", "fenetre", "tramway", "metro", "metre", "bus", "train", "horloge", "ocean", "jeux", "foot", "badminton", "sac", "trousse", "cahier", "ville", "immeuble", "fille", "garcon", "polo", "ampoule", "projecteur", "gravier", "stylo", "micro", "logiciel", "courier", "gras", "poussiere", "main", "ventre", "surligneur", "lettre", "chiffre", "fichier", "dossier"]

mode = int(input("Avec quelle type de mots voulez vous jouez ?\n   1 : Nourriture\n   2 : Animaux\n   3 : Autre\n   4 : Tout\n"))

def replace_caracter(word, to_return, letter) :
	'''
	Take as parameter a word, the string to return and a letter, and look at the locations
	of the letter in the word, and puts it in the same place in the string to be returned.
	'''
	i=1
	res = ""
	res += word[0]
	while i<len(word)-1 :
		if letter == word[i] :
			res += letter
		else :
			res += to_return[i]
		i+=1
	res += word[i]
	return res


def game(categorie) :
	'''
	Take as parameter an array of words, and make a hangman: namely one marks the first,
	the last letter and the same letter in the word of a random word in the array, and asks for a letter and checks whether it is in the word or not. 
	'''
	end = "not_end"
	word = choice(categorie)
	number_letter = len(word)
	form = ""
	error = 11

	i=0
	form += word[i]
	while i<number_letter-2:
		form += "_"
		i+=1
	form += word[number_letter-1]
	form = replace_caracter(word, form, form[0])
	form = replace_caracter(word, form, form[number_letter-1])

	#Check if the player has won or lost
	while end != "end" :
		print(form)
		rep = input()
		if rep in word :
			form = replace_caracter(word, form, rep)
		else :
			error -= 1
			print("Loupé ! il te reste " + str(error) + " erreur !")

		if "_" not in form :
			print("Bravo, le mot étais bien "+word)
			end = "end"

		if error == 0 :
			print("Dommage, le mot étais "+word)
			end = "end"
		
#Game mode
if mode == 1 :
	game(food)
elif mode == 2 :
	game(animals)
elif mode == 3 :
	game (other)
else :
	game(tout)