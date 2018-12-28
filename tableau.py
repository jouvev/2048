#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Tableau:
	"""
	créer un tableau de longueur par largeur
	"""
	def __init__(self,c):
		"""
		initialise un tableau de c par c vide 
		"""
		#tableau:list[list[alpha]]
		self.tableau =[]
		#listTempo:list[alpha]
		listTempo =[]
		#self.longueur:int
		self.cote = c
		
		for k in range(self.cote):
			listTempo = []
			for i in range(self.cote):
				listTempo.append(None)
			self.tableau.append(listTempo)

	def nonVide(self):
		""" compte le nombre de cases non vide dans le tableau """
		#cpt:int
		cpt=0
		for k in range(len(self.tableau)):
			for i in range(len(self.tableau[k])):
				if self.tableau[k][i] != None:
					cpt+=1
		return cpt

	def modifie(self,x,y,valeur):
		""" donne la valeur valeur à la case du tableau en x,y"""
		self.tableau[x][y]=valeur

	def voir(self,x,y):
		""" retourne la valeur de la case x,y du tableau"""
		if self.tableau[x][y] == None:
			return "    "
		elif self.tableau[x][y] < 10:
			return " "+str(self.tableau[x][y])+"  "
		elif self.tableau[x][y] < 100:
			return " "+str(self.tableau[x][y])+" "
		elif self.tableau[x][y] < 1000:
			return " "+str(self.tableau[x][y])
		else:
			return str(self.tableau[x][y])
	def voirGraphique(self,x,y):
		""" retourne la valeur de la case x,y du tableau
                    pour l'affichage Graphique"""
		if self.tableau[x][y] == None:
			return ""
		else:
			return str(self.tableau[x][y])

	def listVide(self):
		""" renvoie une liste de coordonne de toutes les cases vides"""
		#LFinal:List[List[int]]
		LFinal=[]
		for x in range(self.cote):
			for y in range(self.cote):
				if self.tableau[x][y] == None:
					LFinal.append([x,y])
		return LFinal

	def clear(self):
		""" efface tout le tableau"""
		for x in range(self.cote):
			for y in range(self.cote):
				self.tableau[x][y]= None
			
