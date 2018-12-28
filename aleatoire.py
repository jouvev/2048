#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import math

def aleatoire(n):
    """ int-> int
    n > 0
    retourne un nombre aléatoire entre 0 et n-1 """
    return math.floor(random.random()*n)

def aleatoireProba(proba):
    """ number->int
    number est compris entre 0 et 1 exclu
    renvoie soit 1 avec une probabilite de 1-proba
    soit 2 avec une probabilite de proba"""
    #nbAleatoire:int
    nb=math.floor(random.random()*100)
    if nb < proba*100:
        return 2
    else:
        return 1

def frequence(proba,n):
    """test la frequence de 2 avec une probabilité de proba sur n lancé"""
    #cpt:int
    cpt=0
    for k in range(n):
        if 2 == aleatoireProba(proba):
            cpt+=1
    return cpt/n
