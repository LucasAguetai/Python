from pytube import YouTube

#I get the link from the video

url = input("Quel est le lien de la vidéo ? : ")
yt = YouTube(url)
validation = "nothing"

#I request verification that it is the right video 

while validation != "" :
	print("Est-ce bien cette vidéo :", yt.title, "(y or n)")
	validation = input()
	if validation == "y" or validation == "Y" :
		#I get the best quality possible
		yt = yt.streams.get_highest_resolution()
		#I download
		yt.download()
		print("Le téléchargement est terminé ! Bon visionnage :D")
		validation = ""
	else :
		print("Recommençons")
		url = input("Quel est le lien de la vidéo ? : ")
		yt = YouTube(url)