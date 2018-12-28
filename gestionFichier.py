#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle

def sauvegarde(nom,contenu):
    """ sauvegarde le contenu dans un fichier appellé nom""" 
    with open(nom,"wb") as fichier:
            monPickler = pickle.Pickler(fichier)
            monPickler.dump(contenu)
            
def recuperation(nom):
        """retourne le contenu du fichier nom"""
        with open(nom, "rb") as fichier:
            monDepickler = pickle.Unpickler(fichier)
            contenu = monDepickler.load()

        return contenu
