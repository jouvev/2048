#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from game import *
import tkinter.font as tkFont
from tkinter.messagebox import *
import temps
import gestionFichier
import time
import os

class interface(Tk):#herite de fenetre 
    """interface jeu"""
    def __init__(self,c):
        #initialise la fentre
        Tk.__init__(self)

        self.wm_resizable(width=False,height=False)#on fixe la taille de la fenétre
        self.title("2048")# nom fenetre
        self.iconbitmap(bitmap="@icone2.xbm")#change l'icone de la fenétre
        self.bind("<Key>", self.clavier)
        #definition de la police
        self.font=tkFont.Font(family='Helvetica', size=20, weight='bold')

        self.pauseBool=False

        self.fenetre(c)


    def fenetre(self, c):
        #creation du menu
        self.menuBarre = Menu(self)

        self.menuTaille = Menu(self.menuBarre, tearoff=0)
        self.menuTaille.add_command(label = "4x4", command = lambda : self.changerTaille(4))
        self.menuTaille.add_command(label = "5x5", command = lambda : self.changerTaille(5))
        self.menuTaille.add_command(label = "6x6", command = lambda : self.changerTaille(6))

        self.menuReset = Menu(self.menuBarre, tearoff=0)
        self.menuReset.add_command(label = "BestScore", command = self.resetScore)

        self.menuBarre.add_cascade(label="Taille", menu=self.menuTaille)
        self.menuBarre.add_cascade(label="Reset", menu= self.menuReset)
        
        self.config(menu = self.menuBarre)

        #creation du jeu
        if os.path.exists("parti") and \
           askyesno('récupération',
                    "Voulez-vous récupérer votre partie précédente?") :
            self.recuperationPartie()
        else:
            self.jeu = Jeu(c)

        if os.path.exists("parti"):
            os.remove("parti")

        #creation de la frame qui contiendra le jeu
        self.frameJeu = Frame(self, borderwidth=5,relief=GROOVE)

        #creation de la frame qui contiendra le menu comme les buoutons ou le score
        self.frameMenu = Frame(self, borderwidth=5, relief=GROOVE)

        #declaration d'une liste de frame qui contiendron chaque du jeu 
        self.listFrame = []

        #initialisation des Frames des cases
        for x in range(self.jeu.cote):
            listTempo=[]
            for y in range(self.jeu.cote):
                listTempo.append(Frame(self.frameJeu,width=100,height=100, borderwidth=0.5,relief=SUNKEN))
            self.listFrame.append(listTempo)

        #declaration d'une liste de text qui contient les valeurs de la case
        #et qui permet de les afficher dans les labels
        self.listText = []

        #initialisation des stringvars des labels
        for x in range(self.jeu.cote):
            listTempo=[]
            for y in range(self.jeu.cote):
                listTempo.append(StringVar())
            self.listText.append(listTempo)

        #declaration d'une liste de label qui permetent d'afficher les valeur 
        self.listLabel = []

        #initialisation des labels contenu des les frame des cases
        for x in range(self.jeu.cote):
            listTempo=[]
            for y in range(self.jeu.cote):
                listTempo.append(Label(self.listFrame[x][y],height=10,font=self.font,
                                       textvariable = self.listText[x][y]
                                       ,bg="white",fg="white"))
            self.listLabel.append(listTempo)

        #declaration strigvar qui contiendra le score
        self.bestScore = 0
        self.recuperationScore()
        self.score = StringVar()

        #initialisation de la frame qui contiendra le label qui affichera le score
        self.frameScore = Frame(self.frameMenu, borderwidth=3,relief=GROOVE)

        self.labelScore = Label(self.frameScore,
                                font = self.font , textvariable = self.score,
                                bg="#FFCC33", fg="white")

        #intialisation de la frame pour le timer
        self.debut = time.time()
        self.textTimer = StringVar()
        self.frameTimer = Frame(self.frameMenu, borderwidth=3, relief=GROOVE)
        self.labelTimer = Label(self.frameTimer,
                                font = self.font , textvariable = self.textTimer,
                                bg="#FFCC33", fg="white")

        #affiche les cases avec les coordonées x,y
        for x in range(self.jeu.cote):#a changer pour avec des 2048 speciaux
            for y in range(self.jeu.cote):#a changer pour avec des 2048 speciaux
                self.listFrame[x][y].pack_propagate(0)
                self.listFrame[x][y].grid(row=y,column=x,padx=1,pady=1)
                self.listLabel[x][y].pack(fill=BOTH)

        #affectation des valeur dans les cases
        self.update()

        #affichage du score
        self.frameScore.pack(padx=3,pady=3,fill=BOTH)
        self.labelScore.pack(fill=BOTH)

        #affichage du timer
        self.timer()
        self.frameTimer.pack(padx=4,pady=4,fill=BOTH)
        self.labelTimer.pack(fill=BOTH)
        
        #creation bouton et affichage
        self.boutonRecommencer = Button(self.frameMenu, width=24, height=4,
                                        text="Recommencer", command=self.rejouer,
                                        borderwidth=3, relief=GROOVE)
        self.boutonQuitter = Button(self.frameMenu, width=24, height=4,
                                    text="Quitter", command=self.quitte,
                                    borderwidth=3, relief=GROOVE)
        
        self.boutonQuitter.pack(side=BOTTOM, padx=0, pady=3)
        self.boutonRecommencer.pack(side=BOTTOM, padx=0, pady=3)

        #affichage des principaux frames
        self.frameJeu.pack(side=LEFT,padx=4,pady=4,fill=BOTH)
        self.frameMenu.pack(side=LEFT,padx=4,pady=4,fill=BOTH)

        #test de couleur:
        #v=1
        #for x in range(self.jeu.cote):
        #  for y in range(self.jeu.cote):
        #      v*=2
        #      self.jeu.grille.tableau[x][y]=v
        #self.update()

    def clavier(self, event):
        """on detecte les touches appuyées par l'utilisateur"""
        touche = event.keysym
        
        if touche == "Right" and not(self.pauseBool):
            self.jeu.droite()
            self.update()
            
        elif touche == "Left" and not(self.pauseBool):
            self.jeu.gauche()
            self.update()
            
        elif touche == "Up" and not(self.pauseBool):
            self.jeu.haut()
            self.update()
            
        elif touche == "Down" and not(self.pauseBool):
            self.jeu.bas()
            self.update()

        elif touche == "Escape":
            if self.pauseBool:
                self.play()
            else:
                self.pause()

    def timer(self):
        """update le timer"""
        self.textTimer.set("Time:\n"+temps.temps(self.jeu.timer+(time.time()-self.debut)))
        self.id = self.after(100,self.timer)#on repete l'action toutes les 1000ms
                                
    def update(self):
        """ update l'interface"""
        for x in range(self.jeu.cote):
            for y in range(self.jeu.cote):

                #update la valeur dans le stringvar
                self.listText[x][y].set(self.jeu.grille.voirGraphique(x,y))

                #change la couleur de la case en fonction de sa valeur 
                if self.jeu.grille.tableau[x][y] == None:
                    self.listLabel[x][y].configure(bg="white")
                elif self.jeu.grille.tableau[x][y] == 2:
                    self.listLabel[x][y].configure(bg='#30b6c3')
                elif self.jeu.grille.tableau[x][y] == 4:
                    self.listLabel[x][y].configure(bg="#33c8bc")
                elif self.jeu.grille.tableau[x][y] == 8:
                    self.listLabel[x][y].configure(bg="#3dcd96")
                elif self.jeu.grille.tableau[x][y] == 16:
                    self.listLabel[x][y].configure(bg="#37d364")
                elif self.jeu.grille.tableau[x][y] == 32:
                    self.listLabel[x][y].configure(bg="#9fcf1d")
                elif self.jeu.grille.tableau[x][y] == 64:
                    self.listLabel[x][y].configure(bg="#edbf02")                       
                elif self.jeu.grille.tableau[x][y] == 128:
                    self.listLabel[x][y].configure(bg="#ffa600")
                elif self.jeu.grille.tableau[x][y] == 256:
                    self.listLabel[x][y].configure(bg="#ff7400")
                elif self.jeu.grille.tableau[x][y] == 512:
                    self.listLabel[x][y].configure(bg="#e75406")
                elif self.jeu.grille.tableau[x][y] == 1024:
                    self.listLabel[x][y].configure(bg="#e31515")
                elif self.jeu.grille.tableau[x][y] == 2048:
                    self.listLabel[x][y].configure(bg="#c20000")
                else:
                    self.listLabel[x][y].configure(bg="#640000")

        #chaque fin d'update verifie si le joueur a perdu ou gagner 
        if self.jeu.perdu():#and self.jeu.gagner():
            self.fin()

        #update le score
        if self.jeu.score > self.bestScore:
            self.bestScore = self.jeu.score
            self.sauvegardeScore()
            
        self.score.set("Best Score:\n"+str(self.bestScore)+"\nScore :\n"+str(self.jeu.score))
            
    def fin(self):
        """ affiche une fenetre d'alerte gagner ou perdu
        avec un bouton recommencer"""

        #msg=""
        #titre=""

        #if self.jeu.gagner():
        #    titre="Gagné"
        #    msg="Bravo, vous avez gagné!! Voulez-vous recommencer?"
        #else:
        titre="Perdu"
        msg=":/ vous avez perdu !! Voulez-vous recommencer ?"

        if askyesno(titre,msg):
            self.rejouer()
        else:
            self.quit()
            
    def rejouer(self):
        """ recommence une nouvelle partie"""
        self.jeu.clear()#reset le jeu 
        self.debut = time.time()#reset le timer
        self.play()#enleve la pause
        self.update()#update la fenetre

    def pause(self):
        """bloque les movements et le timer"""
        self.after_cancel(self.id)
        self.pauseBool=True
        self.jeu.timer += time.time() - self.debut 
        for x in range(self.jeu.cote):
            for y in range(self.jeu.cote):
                self.listLabel[x][y].configure(bg="#A4A4A4")

        self.textPause = Label(self.frameJeu,text="Pause",
                               bg="#A4A4A4",font=tkFont.Font(size=50),
                               fg="white")
        self.textPause.grid(row=0,rowspan=self.jeu.cote,column=0,columnspan=self.jeu.cote)

    def play(self):
        """interrompt la pause"""
        self.debut = time.time()
        self.timer()
        self.pauseBool=False
        self.update()
        self.textPause.destroy()

    def quitte(self):
        """ demande si sauvegarde puis quitte"""
        if askyesno('sauvegarde','Voulez-vous sauvergarder votre partie ?'):
            self.sauvegardePartie()
        self.quit()

    def sauvegardeScore(self):
        """ sauvergarde le best score """
        gestionFichier.sauvegarde("bestscore",self.bestScore)

    def recuperationScore(self):
        """ on recupere le best score"""
        self.bestScore = gestionFichier.recuperation("bestscore")

    def resetScore(self):
        """reste le score à 0"""
        gestionFichier.sauvegarde("bestscore",0)
        self.bestScore = 0
        self.update()

    def sauvegardePartie(self):
        """sauvegarde la partie"""
        self.jeu.timer += time.time() - self.debut
        gestionFichier.sauvegarde("parti",self.jeu)

    def recuperationPartie(self):
        """recup la partie sauvergarder"""
        self.jeu = gestionFichier.recuperation("parti")

    def resetFenetre(self):
        """detruit tous les widgets enfants de la fenetre"""
        for w in self.winfo_children():
            w.destroy()

    def changerTaille(self,taille):
        """change la taille du 2048"""
        self.resetFenetre()
        self.fenetre(taille)
        
if __name__=="__main__":

    interface=interface(4) 
    interface.mainloop()
    interface.destroy()
