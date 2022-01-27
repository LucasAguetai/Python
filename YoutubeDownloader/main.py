from pytube import YouTube

#I get the link from the video

url = input("Quel est le lien de la vidéo ? : ")
yt = YouTube(url)

#I request verification that it is the right video 

print("Est-ce bien cette vidéo :", yt.title, "(y or n)")
validation = input()
if validation == "y" or validation == "Y" :
	#I get the best quality possible
	yt = yt.streams.get_highest_resolution()
	#I download
	yt.download()