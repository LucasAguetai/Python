from pytube import YouTube

url = input("Quel est le lien de la vidéo ? : ")
yt = YouTube(url)

print("Est-ce bien cette vidéo :", yt.title, "(y or n)")
validation = input()
if validation == "y" or validation == "Y" :
	yt = yt.streams.get_highest_resolution()
	yt.download()