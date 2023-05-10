# code
from tkinter import *           #module pour l'interface graphique
from tkinter import messagebox  #module pour gerer la boite "Erreur"
import json                     #module pour gerer des fichiers avec extention .json (java)
import os                       #module pour gerer les fichiers

eleves = {}                                     #creer un dictionnaire vide

def sauver():                                   #sauver ou creer un nouveau dictionnaire
    with open('classe.json', 'w+') as fichier:
        json.dump(eleves, fichier)

if os.path.exists('classe.json'):               #verifier si le fichier existe
    with open('classe.json', 'r+') as fichier:  #importer le fichier
        if os.path.getsize('classe.json') == 0: #vérifier si le fichier est vide
            eleves = {}                         #creer un dictionnaire vide
        else:
            eleves = json.load(fichier)         #ouvrir le fichier, change la valeur de la variable (eleves)
else:                                           #message pour informer l'utilisateur
    messagebox.showinfo('INFORMATION', "Un nouveau fichier classe.json va être crée dans votre repertoire !")
    sauver()                                    #creer un nouveau dictionnaire

def moy():
    for eleve in eleves.values():               #moyenne des notes
        eleve['note'] = int(eleve['note']) #transforme la valeur de la clé 'note'...[v['note']] ...en entier
    moyenne = round(sum([v['note'] for v in eleves.values()]) / len(eleves)) #moy des valeurs de la clé['note']
    champ4.delete(0, END)
    champ4.insert(0, moyenne)

def afficher():                                 #afficher le dictionnaire élèves,
    global label4, label5, label6
    for label in [label4, label5, label6]:
        label.delete(1.0, END)                  #nettoyer les labels.Text()

    for eleve in sorted(eleves):                #tri alphabetique
        note = eleves[eleve]['note']            #ciblage des variables vers les clés du dictionnaire
        appreciation = eleves[eleve]['appreciation']

        label4.insert(END, f'{eleve} \n')       #insertion des valeurs associées aux clés du dictionnaire
        label5.insert(END, f'{note} \n')        #dans 3 labels differents
        label6.insert(END, f'{appreciation} \n')
    label4, label5, label6.update()

def ajouter():                                  #ajouter ou modifier un eleve
    eleve = champ1.get()
    if champ2.get().isdigit() and 0 <= int(champ2.get()) <= 20: # si un nombre entier de 0 a 20 inclus
        note = champ2.get()                     #affectation des entrées utilisateur aux variables
        appreciation = champ3.get()             #eleve/ note/ appreciation avec la methode champ.get()
        eleves[eleve] = {'note': note, 'appreciation': appreciation}
        afficher()                              #rafraichir et afficher le texte
    else:
        messagebox.showwarning("ATTENTION", f"la note de {eleve} n'est pas une entrée valide !\n" 
                               "entrez un nombre entier de 0 à 20 inclus ")

def supprimer():                                #supprimer un eleve (del)
    eleve = champ1.get()
    if eleve in eleves:
        del eleves[eleve]
        afficher()                              #rafraichir et afficher le texte
    else:
        #message Erreur si l'éleve n'existe pas (messagebox)
        messagebox.showerror("Erreur", f"L'élève {eleve} n'est pas dans cette classe.")


#creation de la mise en page fenetre, frame, labels, champs, buttons (grid)
#couleur = '#DDEAF7' #definir la variable couleur vert #F4F6EB #A8EDDB  bleu #DDEAF7 jaune #E6E8CF
#fond = '#F4F6EB'    #couleur des background

nuancier = {'bleu' : {'couleur' : '#DDEAF7', 'fond' : '#F4F6EB'},
            'vert' : {'couleur' : '#F4F6EB', 'fond' : '#A8EDDB'},
            'jaune' : {'couleur' : '#E6E8CF', 'fond' : '#F4F6EB'}}

couleur = nuancier["vert"]['couleur']
fond = nuancier["vert"]['fond']

#def change_couleur:

fenetre = Tk()
fenetre.iconbitmap('menus/logo3.ico')
fenetre.title('Bulletin de Classe')
fenetre.config(background=couleur)
fenetre.geometry('634x400')

frame = Frame(fenetre, background=couleur)
frame.pack(expand=YES)

label = Label(frame, text='Classe de Monsieur (Madame) X', width=60, height=2, font=('Balthazar', 15)
                    , bg=couleur)
label.grid(row=0, columnspan=3)

label1 = Label(frame, text="Nom de l'élève", font=('times', 13), bg=couleur)
label1.grid(row=1, column=0, sticky=W, padx=10)

champ1 = Entry(frame, highlightthickness=1, font=('times', 13), width=25, background=fond)
champ1.grid(row=3, column=0, sticky=W, padx=10)

label2 = Label(frame, text='Note', font=('times', 13), bg=couleur)
label2.grid(row=1, column=1, sticky=W, padx=15)

champ2 = Entry(frame,highlightthickness=1, font=('times', 13), width=5, background=fond)
champ2.grid(row=3, column=1)

label3 = Label(frame, text='Appréciation', font=('times', 13), bg=couleur)
label3.grid(row=1, column=2, sticky=W, padx=10)

champ3 = Entry(frame,highlightthickness=1, font=('times', 13), width=29, background=fond)
champ3.grid(row=3, column=2, sticky=W, padx=10)

bouton1 = Button(frame, text='Ajouter / Modifier', font=('times', 10, ), command=ajouter)
bouton1.grid(row=4, column=0, sticky=W, padx=10, pady=10)

bouton2 = Button(frame, text='Supprimer', font=('times', 10), width=17, command=supprimer)
bouton2.grid(row=4, column=2, sticky=E, padx=13, pady=10)

bouton3 = Button(frame, text='Sauver', font=('times', 10), width=17, command=sauver)
bouton3.grid(row=6, column=2, sticky=E, padx=11, pady=10)

bouton4 = Button(frame, text='Quitter', font=('times', 10), width=17, command=quit)
bouton4.grid(row=6, column=2, sticky=W, padx=11, pady=10)

bouton5 = Button(frame, text='Moyenne', font=('times', 10), width=15, command=moy)
bouton5.grid(row=4, column=0, sticky=E, padx=12, pady=10)

#bouton6 = Button(frame, text='Couleur', font=('times', 10), width=14, command=change_couleur)
#bouton6.grid(row=6, column=0, sticky=W, padx=11, pady=10)

champ4 = Entry(frame,highlightthickness=1, font=('times', 13), width=5, background=fond)
champ4.grid(row=4, column=1)

label4 = Text(frame, width=28, height=12, highlightthickness=1, bg=fond)
label4.grid(row=5, column=0, sticky=W, padx=10)

label5 = Text(frame, width=6, height=12, highlightthickness=1, bg=fond)
label5.grid(row=5, column=1)

label6 = Text(frame, width=33, height=12, highlightthickness=1, bg=fond)
label6.grid(row=5, column=2, sticky=W, padx=10)

afficher()          #afficher le dictionnaire

fenetre.mainloop()  #afficher la fenetre (boucle principale)
