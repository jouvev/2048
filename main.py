#!/usr/bin/env python
# -*- coding: utf-8 -*-

from game import *

jeu=Jeu(4)

while not(jeu.perdu()) and not(jeu.gagner()):
    jeu.affichage()
    action=input("scrore : {}\nz,q,s,d ? ".format(jeu.score))
    if action == "z":
        if not(jeu.possibleHaut()):
            print("imposible!")
        jeu.haut()
    elif action == "q":
        if not(jeu.possibleGauche()):
            print("imposible!")
        jeu.gauche()
    elif action == "s":
        
        if not(jeu.possibleBas()):
            print("imposible!")
        jeu.bas()
    else:
        if not(jeu.possibleDroite()):
            print("imposible!")
        jeu.droite()

jeu.affichage()

if jeu.gagner():
    print("Vous avez gagné !!!")
else:
    print("Vous avez perdu !!!")

