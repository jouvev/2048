#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aleatoire import *
from tableau import *
import random

class Jeu:
    """
    Créer une grille de c*c avec les régles du 2048
    """
    def __init__(self,c):
        """initialise le tableau de c*c vide """
        #tableau: List[List[number]]
        self.cote=c
        self.grille = Tableau(c)
        self.score = 0
        self.timer = 0

        self.ajoutAleatoire()
        self.ajoutAleatoire()

    def ajoutAleatoire(self):
       """ apres chaque action il faut ajouter un nombre"""
       #coordonne:list[int]
       coordonne = random.choice(self.grille.listVide())
       
       self.grille.modifie(coordonne[0],coordonne[1],aleatoireProba(0.1)*2)

#on s'occupe du deplacement à dorite
    def possibleDroite(self):
        """ retourne vrai s'il est possible de faire un deplacement à droite"""
        for x in range(self.grille.cote-1):
            for y in range(self.grille.cote):
                if self.grille.tableau[x][y]!=None and (self.grille.tableau[x+1][y]==None or self.grille.tableau[x][y] == self.grille.tableau[x+1][y]):
                    return True
        return False
                    
    def droite(self):
        """ slide à droite et ajoute un nouveau nombre avec ajoutAleatoire
            d'abord tout mettre le plus à droite possible
            puis faire les couples puis tout mettre à droite"""
        if self.possibleDroite():
            for y in range(self.grille.cote):
                self.deplacementDroite(y)
                self.coupleDroite(y)
                self.deplacementDroite(y)
            self.ajoutAleatoire()
        
    def deplacementDroite(self,y):
        """ déplace tout les éléments de la ligne y à droite"""
        x=self.grille.cote-2
        while x >=0:
            i=1
            if self.grille.tableau[x][y]!=None:
                while x+i<self.grille.cote and self.grille.tableau[x+i][y]==None:
                    i=i+1
                if i!=1:
                    self.grille.modifie(x+i-1,y,self.grille.tableau[x][y])
                    self.grille.modifie(x,y,None)
            x=x-1

    def coupleDroite(self,y):
        """fait les couples sur la ligne y s'il existe"""
        x=self.grille.cote-2
        while x >=0:
            if self.grille.tableau[x][y]!= None and self.grille.tableau[x][y] == self.grille.tableau[x+1][y] :
                self.grille.modifie(x+1,y,2*self.grille.tableau[x][y])
                self.addScore(2*self.grille.tableau[x][y])
                self.grille.modifie(x,y,None)
            x=x-1
            
#on s'occupe du deplacement à gauche
    def possibleGauche(self):
        """ retourne vrai s'il est possible de faire un deplacement à gauche"""
        x=self.grille.cote-1
        while x > 0:
            for y in range(self.grille.cote):
                if self.grille.tableau[x][y]!=None and (self.grille.tableau[x-1][y] == None or self.grille.tableau[x][y] == self.grille.tableau[x-1][y]):
                    return True
            x=x-1
        return False
    
    def gauche(self):
        """ slide à gauche et ajoute un nouveau nombre avec ajoutAleatoire
            d'abord tout mettre le plus à gauche possible
            puis faire les couples puis tout mettre à gauche """
        if self.possibleGauche():
            for y in range(self.grille.cote):
                self.deplacementGauche(y)
                self.coupleGauche(y)
                self.deplacementGauche(y)
            self.ajoutAleatoire()


    def deplacementGauche(self,y):
        """ déplace tout les éléments de la ligne y à droite"""
        x=1
        while x < self.grille.cote:
             i=1
             if self.grille.tableau[x][y]!= None:
                 while x-i>=0 and self.grille.tableau[x-i][y]==None:
                     i=i+1
             if i!=1:
                self.grille.modifie(x-i+1,y,self.grille.tableau[x][y])
                self.grille.modifie(x,y,None)
             x=x+1

    def coupleGauche(self,y):
        """fait les couples sur la ligne y s'il existe"""
        x=1
        while x < self.grille.cote:
            if self.grille.tableau[x][y]!= None and self.grille.tableau[x][y] == self.grille.tableau[x-1][y] :
                self.grille.modifie(x-1,y,2*self.grille.tableau[x][y])
                self.addScore(2*self.grille.tableau[x][y])
                self.grille.modifie(x,y,None)
            x=x+1

# on s'occupe du deplacement en haut
    def possibleHaut(self):
        """ retourne vrai s'il est possible de faire un deplacement en haut"""
        y=self.grille.cote-1
        while y > 0:
            for x in range(self.grille.cote):
                if self.grille.tableau[x][y]!=None and (self.grille.tableau[x][y-1] == None or self.grille.tableau[x][y] == self.grille.tableau[x][y-1]):
                    return True
            y=y-1
        return False
    
    def haut(self):
        """ slide en haut et ajoute un nouveau nombre avec ajoutAleatoire
            d'abord tout mettre le plus haut possible
            puis faire les couples puis tout mettre en haut """
        if self.possibleHaut():
            for x in range(self.grille.cote):
                self.deplacementHaut(x)
                self.coupleHaut(x)
                self.deplacementHaut(x)
            self.ajoutAleatoire()
        
    def deplacementHaut(self,x):
        """ deplace tout les éléments en haut de la colone x """
        y=1
        while y < self.grille.cote:
            i=1
            if self.grille.tableau[x][y] != None:
                while y-i >=0  and self.grille.tableau[x][y-i] == None:
                    i=i+1
            if i!=1:
                self.grille.modifie(x,y-i+1,self.grille.tableau[x][y])
                self.grille.modifie(x,y,None)
            y=y+1

    def coupleHaut(self,x):
        """fait les couples sur la colonne x s'il existe"""
        y=1
        while y < self.grille.cote:
            if self.grille.tableau[x][y]!= None and self.grille.tableau[x][y] == self.grille.tableau[x][y-1] :
                self.grille.modifie(x,y-1,2*self.grille.tableau[x][y])
                self.addScore(2*self.grille.tableau[x][y])
                self.grille.modifie(x,y,None)
            y=y+1
                
# on s'occupe du deplacement en bas
    def possibleBas(self):
        """ retourne vrai s'il est possible de faire un deplacement en bas"""
        for y in range(self.grille.cote-1):
            for x in range(self.grille.cote):
                if self.grille.tableau[x][y]!=None and (self.grille.tableau[x][y+1] == None or self.grille.tableau[x][y] == self.grille.tableau[x][y+1]):
                    return True
        return False
    
    def bas(self):
        """ slide en bas et ajoute un nouveau nombre avec ajoutAleatoire
            d'abord tout mettre le plus bas possible
            puis faire les couples puis tout mettre en bas """
        if self.possibleBas():
            for x in range(self.grille.cote):
                self.deplacementBas(x)
                self.coupleBas(x)
                self.deplacementBas(x)
            self.ajoutAleatoire()
        
    def deplacementBas(self,x):
        """ deplace tout les éléments en haut de la colone x """
        y = self.grille.cote-2
        while y >= 0 :
            i=1
            if self.grille.tableau[x][y] != None:
                while y+i < self.grille.cote  and self.grille.tableau[x][y+i] == None:
                    i=i+1
            if i!=1:
                self.grille.modifie(x,y+i-1,self.grille.tableau[x][y])
                self.grille.modifie(x,y,None)
            y=y-1

    def coupleBas(self,x):
        """fait les couples sur la colonne x s'il existe"""
        y = self.grille.cote-2
        while y >= 0 :
            if self.grille.tableau[x][y]!= None and self.grille.tableau[x][y] == self.grille.tableau[x][y+1] :
                self.grille.modifie(x,y+1,2*self.grille.tableau[x][y])
                self.addScore(2*self.grille.tableau[x][y])
                self.grille.modifie(x,y,None)
            y=y-1
            
#affichage
    def voir(self):#graphique
        return self.grille.tableau

    def affichage(self):#console
        """ affichage de la grille en mode console """
        #final:str
        final=""
        for y in range(self.grille.cote):
            for x in range(self.grille.cote):
                final = final + self.grille.voir(x,y)
                if x != self.grille.cote-1:
                    final = final + " | "
            final = final + "\n"
            if y != self.grille.cote-1:
                nb = (self.grille.cote * 7 )- 2 
                final = final+ "-"*nb + "\n"
        print(final)
            
#on s'arrete aussi si 2048 est atteint
    def gagner(self):
        """ test si 2048 est atteint est donc la partie est gagné"""
        for x in range(self.grille.cote):
            for y in range(self.grille.cote):
                if self.grille.tableau[x][y] == 2048:
                    return True
        return False
    
#on doit tester apres chaque movement si la partie est perdu
    def perdu(self):
        """ test si la partie est terminé"""
        if self.grille.nonVide() == self.grille.cote*self.grille.cote:
            for x in range(self.grille.cote):
                for y in range(self.grille.cote):
                    if x+1<self.grille.cote and self.grille.tableau[x+1][y] == self.grille.tableau[x][y] :
                        return False
                    elif x-1>=0 and self.grille.tableau[x-1][y] == self.grille.tableau[x][y] :
                        return False
                    elif y+1<self.grille.cote and self.grille.tableau[x][y+1] == self.grille.tableau[x][y] :
                        return False
                    elif y-1>=0 and self.grille.tableau[x][y-1] == self.grille.tableau[x][y] :
                        return False
        else:
            return False

        return True

#on gere le score
    def addScore(self,v):
        """ ajoute v au score"""
        self.score += v
    
#une fonction pour recommencer
    def clear(self):
        """ vide le tableau et le réinitialise pour une nouvelle partie"""
        self.grille.clear()
        self.__init__(self.cote)
