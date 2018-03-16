#made by Percevase

#!/usr/bin/env python
#-*- coding: utf-8 -*-

#import des fonctions sleep et fonction absolue
from time import sleep
from math import fabs

#fonction pour faire la presentation du systeme de l'algo
def presentation ():
	print ("voici le lovo9000 !")
	#sleep (2)
	print ("pour savoir a quel point vous etes lie a une personne entrer votre prenom et le sien !")
	print ("la machine calculera automatiquement le pourcentage de compatibilite que vous avez avec cette personne !")
	#sleep (2)
	return

#algorithme de calcule du pourcentage de compatibilite
def calcLove (lover1, lover2):
	
	lovoScore = 0
	KMaxLovoScore = len (lover1) + len (lover2)
	
	#application de coefficients pour booster un peu les pourcentages
	if len (lover1) == len (lover2):
		lovoScore = 0.75 * (len (lover1) + len (lover2))
	elif len (lover1) > len (lover2):
		lovoScore = 0.75 * len (lover1)
	else :
		lovoScore = 0.75 * len (lover2)
	
	for letterInTheFirstName in lover1:
		for letterInTheSecondName in lover2:
			if letterInTheSecondName == letterInTheFirstName:
				if lover2.index (letterInTheSecondName) == lover1.index (letterInTheFirstName):
					lovoScore += 1
				else :
					lovoScore = lovoScore + (1/fabs (lover2.index (letterInTheSecondName) - lover1.index (letterInTheFirstName)))
	
	#teste qui evite que le score depasse les 100%
	if lovoScore > KMaxLovoScore:
		lovoScore = lovoScore - 0.25 * (len (lover1) + len (lover2))
		
	return lovoScore*100/KMaxLovoScore
	
#fonction qui sert a faire tourner l'algorithme
def main ():
	presentation ()
	name1 = input ("entrer votre prenom: ")
	name1 = name1.lower ()
	name2 = input ("entrer le prenom de votre amour: ")
	name2 = name2.lower ()
	print ("votre compatibilite avec " + name2 + " est: " + str (int (calcLove (name1, name2))) + "% !")
	return 
	
main ()

#made by Percevase
