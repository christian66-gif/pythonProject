### code
from tkinter import * #module pour l'interface graphique
from tkinter import messagebox #module pour gerer la boite "Erreur"
import json #module pour gerer des fichiers avec extention .json (java)

#importer le fichier classe.json
with open('classe.json', 'r') as fichier:
    eleves = json.load(fichier)

#ajouter ou modifier un eleve
def ajouter():
    eleve = champ1.get()
    note = champ2.get()
    appreciation = champ3.get()
    eleves[eleve] = {'note': note, 'appreciation': appreciation}

    #nettoyer le texte affiché (del)
    label4.delete(1.0, END)

    # Afficher la nouvelle liste des élèves (insert, update)
    for eleve in sorted(eleves):
        note = eleves[eleve]['note']
        appreciation = eleves[eleve]['appreciation']
        label4.insert(END, f"{eleve}: note={note}, appreciation={appreciation}\n")
    label4.update()

#supprimer un eleve (del)
def supprimer():
    eleve = champ1.get()
    if eleve in eleves:
        del eleves[eleve]

        # nettoyer le texte affiché (delete)
        label4.delete(1.0, END)

        # Afficher la nouvelle liste des élèves (insert, update)
        for eleve in sorted(eleves):
            note = eleves[eleve]['note']
            appreciation = eleves[eleve]['appreciation']
            label4.insert(END, f"{eleve}: note={note}, appreciation={appreciation}\n")
        label4.update()
    else:
        #message Erreur si l'éleve n'existe pas (messagebox)
        messagebox.showerror("Erreur", f"L'élève {eleve} n'est pas dans cette classe.")

#sauvegarder les données dans un fichier '.json'
def sauver():
    with open('classe.json', 'w+') as fichier:
        json.dump(eleves, fichier)

#creation de la mise en page fenetre, labels, champs, buttons (grid)
fenetre = Tk()
fenetre.title('Bulletin de Classe')
fenetre.iconbitmap('menus/logo3.ico')
fenetre.config(background='white')
fenetre.geometry('600x400')

label = Label(fenetre, text='Classe de Monsieur (Madame) X', width=60, height=2, font=('Balthazar', 15)
                    , bg='white')
label.grid(row=0, columnspan=3)

label1 = Label(fenetre, text="Nom de l'élève", font=('times', 13), bg='white')
label1.grid(row=1, column=0, sticky=W, padx=10)

champ1 = Entry(fenetre, highlightthickness=1, font=('times', 13), width=25)
champ1.grid(row=3, column=0, sticky=W, padx=10)

label2 = Label(fenetre, text='Note', font=('times', 13), bg='white')
label2.grid(row=1, column=1, sticky=W)

champ2 = Entry(fenetre,highlightthickness=2, font=('times', 13), width=5)
champ2.grid(row=3, column=1, sticky=W)

label3 = Label(fenetre, text='Appréciation', font=('times', 13), bg='white')
label3.grid(row=1, column=2, sticky=W, padx=10)

champ3 = Entry(fenetre,highlightthickness=2, font=('times', 13), width=29)
champ3.grid(row=3, column=2, sticky=W, padx=10)

bouton1 = Button(fenetre, text='Ajouter / Modifier', font=('times', 10, ), command=ajouter)
bouton1.grid(row=4, column=0, sticky=W, padx=10, pady=10)

bouton2 = Button(fenetre, text='Supprimer', font=('times', 10), width=15, command=supprimer)
bouton2.grid(row=4, column=2, sticky=E, padx=15, pady=10)

bouton3 = Button(fenetre, text='Sauver', font=('times', 10), width=15, command=sauver)
bouton3.grid(row=6, column=2, sticky=E, padx=15, pady=10)

label4 = Text(fenetre, width=70, height=12, highlightthickness=2, bg='white')
label4.grid(row=5, columnspan=3)

# Afficher la liste des élèves (insert), par ordre alphabétique (sorted), après avoir nettoyer le label.Text() (delete)
label4.delete(1.0, END)
for eleve in sorted(eleves):
    note = eleves[eleve]['note']
    appreciation = eleves[eleve]['appreciation']
    label4.insert(END, f"{eleve}: note={note}, appreciation={appreciation}\n")

#afficher la fenetre (boucle principale)
fenetre.mainloop()