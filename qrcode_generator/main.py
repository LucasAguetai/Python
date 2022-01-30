import qrcode

sujet = input("Que voulez vous mettre en qrcode ?\n")
img = qrcode.make(sujet)
img.save(sujet+".png")