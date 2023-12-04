
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

class Biere:
    def __init__(self, jour, nom, pays, style, desctription, image_path):
        self.nom = nom
        self.jour = jour
        self.pays = pays
        self.style = style
        self.desctription = desctription
        self.image_path = image_path


biere01 = Biere("Jour01", "To Øl Gose to Hollywood", "Danemark", "Gose", "Une gose rafraîchissante avec une touche d'agrumes.","./images/To_Øl-Gose_to_Hollywood.jpeg")
biere02 = Biere("Jour02", "Omnipollo Bianca Mango Lassi Gose", "Belgique", "Trappiste belge", "Une bière trappiste belge légère et rafraîchissante.","images/Omnipollo_Bianca_Mango_Lassi_Gose.jpeg")
biere03 = Biere("Jour03", "Westmalle Extra", "Suède", "Gose", "Une gose exotique aux saveurs de mangue.","images/Westmalle_Extra.png")
biere04 = Biere("Jour04", "Põhjala Öö", "Estonie", "imperial stout", "Une imperial stout estonienne avec des notes de café et de chocolat.","images/Põhjala_Öö.jpeg")
biere05 = Biere("Jour05", "The Kernel Table Beer", "Royaume-Uni", "Session IPA", "Une session IPA britannique légère et pleine de saveurs houblonnées.","images/The Kernel Table Beer.jpg")
biere06 = Biere("Jour06", "Jolly Pumpkin Bam Bière", "États-Unis", "Pale Ale", "Une bière farmhouse ale américaine avec des notes épicées.","images/Jolly_Pumpkin_Bam_Bière.jpeg")
biere07 = Biere("Jour07", "De Molen Rasputin", "Pays-Bas", "Imperial stout", "Une imperial stout néerlandaise complexe et riche.","images/De_Molen_RasputinDe_Molen_Rasputin.jpg")
biere08 = Biere("Jour08", "Lervig Lucky Jack", "Norvège", "American Pale Ale", "Une American Pale Ale norvégienne avec des notes d'agrumes.","images/Lervig_Lucky_Jack.jpg")
biere09 = Biere("Jour09", "Ayinger Celebrator Doppelbock", "Allemagne", "Doppelbock", "Une doppelbock allemande riche et maltée.","images/Ayinger_Celebrator_Doppelbock.png")
biere10 = Biere("Jour10", "Crooked Stave Sour Rose", "États-Unis", "Sure", "Une bière sure aux fruits rouges, avec une acidité délicate.","images/Crooked_Stave_Sour_Rose.jpg")
biere11 = Biere("Jour11", "St. Feuillien Saison", "Belgique", "Saison belge", "Une saison belge classique avec des arômes épicés et fruités.","images/St-Feuillien-Saison.png")
biere12 = Biere("Jour12", "BrewDog Elvis Juice", "Écosse", "American IPA écossaise", "Une  avec des notes de pamplemousse et de caramel.","images/BrewDog_Elvis_Juice.jpg")
biere13 = Biere("Jour13", "Mahr's Bräu Ungespundet", "Allemagne", "kellerbier allemande", "Une kellerbier allemande non filtrée et douce.","images/Mahr's_Bräu_Ungespundet.png")
biere14 = Biere("Jour14", "Birra Del Borgo Duchessa", "Italie", "Sour", "Une bière sour aux pêches et aux baies.","images/Birra_Del_Borgo_Duchessa.JPG")
biere15 = Biere("Jour15", "Jopen Mooie Nel IPA", "Pays-Bas", "IPA", "Une  néerlandaise aux arômes de fruits tropicaux.","images/Jopen_Mooie_Nel_IPA.jpeg")
biere16 = Biere("Jour16", "Gueuze Tilquin à l'Ancienne", "Belgique", "Gueuze", "Une gueuze belge traditionnelle avec une acidité équilibrée.","images/Gueuze_Tilquin_à_l'Ancienne.jpeg")
biere17 = Biere("Jour17", "Pühaste Must Kuld", "Estonie", "Porter", "Une porter balte riche en saveurs de café et de chocolat.","images/Pühaste_Must_Kuld.jpeg")
biere18 = Biere("Jour18", "Oedipus Thai Thai", "Pays-Bas", "Saison", "Une saison épicée avec des notes de citronnelle et de gingembre.","images/Oedipus_Thai_Thai.jpg")
biere19 = Biere("Jour19", "Pilsner Urquell", "République tchèque", "Pilsner", "La première pilsner au monde, avec une amertume noble.","images/Pilsner_Urquell.jpeg")
biere20 = Biere("Jour20", "Magic Rock High Wire Grapefruit", "Royaume-Uni", "American Pale Ale", "Une American Pale Ale avec une explosion de pamplemousse.","images/Pilsner_Urquell.jpeg")
biere21 = Biere("Jour21", "Brouwerij 't IJ IJwit", "Pays-Bas", "Blanche", "Une bière blanche néerlandaise avec des arômes d'écorce d'orange et de coriandre.","images/Brouwerij_'t_IJ_IJwit.jpg")
biere22 = Biere("Jour22", "Mikkeller Windy Hill", "Danemark", "New England IPA", "Une bière de blé acidulée et houblonnée.","images/Mikkeller_Windy_Hill.jpg")
biere23 = Biere("Jour23", "Brasserie Dupont Saison Dupont", "Belgique", "Saison", "Une  belge classique et rafraîchissante.","images/Brasserie_Dupont_Saison_Dupont.jpeg")
biere24 = Biere("Jour24", "Oskar Blues Dale's Pale Ale", "États-Unis", "Pale Ale", "Une pale ale américaine équilibrée et facile à boire.","images/Oskar_Blues_Dale's_Pale_Ale.jpg")

liste_bieres = [biere01, biere02, biere03, biere04, biere05, biere06, biere07,
biere08, biere09, biere10, biere11, biere12, biere13, biere14, biere15, biere16,
biere17, biere18, biere19, biere20, biere21, biere22, biere23, biere24]

jours_de_lavent = [ "Jour01", "Jour02", "Jour03", "Jour04", 
"Jour05", "Jour06", "Jour07", "Jour08", "Jour09", "Jour10", "Jour11", 
"Jour12", "Jour13", "Jour14", "Jour15", "Jour16", "Jour17", "Jour18", "Jour19", 
"Jour20", "Jour21", "Jour22", "Jour23" , "Jour24"]

#########-------------------------------------------  version 1.0   ----------------------------------------##########
# def obtenir_biere_par_jour():
#     global liste_bieres
    
#     if not liste_bieres:
#         print("Il n'y a plus de bières disponibles.")
#         return None

#     # Utilisez random.choice pour obtenir une bière aléatoire à chaque appel
#     biere_jour = random.choice(liste_bieres)

#     # # Retirez la bière choisie de la liste pour éviter de la répéter
#     liste_bieres.remove(biere_jour)

#     return biere_jour



# for jour in jours_de_lavent:
#     print(f"Avant l'appel pour le {jour}, la taille de la liste des bières est : {len(liste_bieres)}")
#     biere_jour = obtenir_biere_par_jour()
    
#     if biere_jour:
#         print(" ")
#         print(f"Pour le {jour}, la bière est : {biere_jour.nom}")
#         print(f"\tStyle: {biere_jour.pays}")
#         print(f"\tStyle: {biere_jour.style}")
#         print(f"\tDescription: {biere_jour.desctription}")
#         print(" ")
       
#     else:
#         print(" ")
#         print(f"Joyeux Noël!")
#         print(" ")





#########-------------------------------------------  version 2.0   ----------------------------------------##########


# Triez la liste jours_de_lavent
jours_de_lavent.sort()

def obtenir_biere_par_jour():
    global liste_bieres

    if not liste_bieres:
        print("Il n'y a plus de bières disponibles.")
        return None

    # Utilisez random.choice pour obtenir une bière aléatoire à chaque appel
    biere_jour = random.choice(liste_bieres)

    # Retirez la bière choisie de la liste pour éviter de la répéter
    liste_bieres.remove(biere_jour)

    return biere_jour

def afficher_biere_du_jour():
    global jours_de_lavent

    if not jours_de_lavent:
        messagebox.showinfo("Fin du calendrier", "Joyeux Noël!")
        return

    jour = jours_de_lavent.pop(0)
    biere_jour = obtenir_biere_par_jour()

    if biere_jour:
        message = f"Période de l'avent: {jour}\n"
        message += f"Bière: {biere_jour.nom}\n"
        message += f"Pays: {biere_jour.pays}\n"
        message += f"Style: {biere_jour.style}\n"
        message += f"Description: {biere_jour.desctription}"

        messagebox.showinfo("Bière du jour", message)
    else:
        messagebox.showinfo("Fin du calendrier", "Joyeux Noël!")

# Interface graphique
fenetre = tk.Tk()
fenetre.title("Calendrier de l'Avent - Bière")
fenetre.geometry("300x200")

# Bouton pour afficher la bière du jour
bouton_afficher_biere = tk.Button(fenetre, text="Afficher la bière du jour", command=afficher_biere_du_jour)
bouton_afficher_biere.pack()

fenetre.mainloop()





#########-------------------------------------------  version 3.0   ----------------------------------------##########

# def obtenir_biere_par_jour():
#     global liste_bieres

#     if not liste_bieres:
#         print("Il n'y a plus de bières disponibles.")
#         return None

#     biere_jour = random.choice(liste_bieres)
#     liste_bieres.remove(biere_jour)

#     return biere_jour

# def afficher_biere_du_jour():
#     global jours_de_lavent

#     if not jours_de_lavent:
#         messagebox.showinfo("Fin du calendrier", "Joyeux Noël!")
#         return

#     jour = jours_de_lavent.pop(0)
#     biere_jour = obtenir_biere_par_jour()

#     if biere_jour:
#         afficher_fenetre_biere(jour, biere_jour)
#     else:
#         messagebox.showinfo("Fin du calendrier", "Joyeux Noël!")

# def afficher_fenetre_biere(jour, biere):
#     fenetre_biere = tk.Toplevel()
#     fenetre_biere.title(f"Bière du {jour}")

#     image = Image.open(biere.image_path)
#     image = image.resize((200, 200), Image.ANTIALIAS(

#     ))
#     photo = ImageTk.PhotoImage(image)

#     label_image = tk.Label(fenetre_biere, image=photo)
#     label_image.image = photo
#     label_image.pack()

#     message = f"Période de l'avent: {jour}\n"
#     message += f"Bière: {biere.nom}\n"
#     message += f"Pays: {biere.pays}\n"
#     message += f"Style: {biere.style}\n"
#     message += f"Description: {biere.description}"

#     label_message = tk.Label(fenetre_biere, text=message)
#     label_message.pack()

# # Interface graphique principale
# fenetre = tk.Tk()
# fenetre.title("Calendrier de l'Avent - Bière")
# fenetre.geometry("300x200")

# # Bouton pour afficher la bière du jour
# bouton_afficher_biere = tk.Button(fenetre, text="Afficher la bière du jour", command=afficher_biere_du_jour)
# bouton_afficher_biere.pack()

# fenetre.mainloop()