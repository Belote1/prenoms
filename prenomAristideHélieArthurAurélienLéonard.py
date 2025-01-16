# Créé par Ariside, Arthur, Leonard, Helie et Aurélien en 2nde7 en Python 3.7

import os
os.chdir("C:/Users/helieweinberg/Downloads/SNT")
print(os.getcwd())
#Ouverture du fichier et traitement
fichier = open("prenoms.csv", "r")
names = fichier.read()
list_names = names.split("\n")

#Input
research = str(input("Un prenom stp"))

#Init de variables qui nous servent après
people = 0
founded = False
departements = []

for i in range(len(list_names)): #Loop qui traite chaque ligne une par une

    line = list.names[i].split(";") #Chaque ligne devient une liste

    if line[1] == research: #si c'est bien le prénom qu'on recherche...
        founded = True #on dit l'avoir trouver pour après arrêter le programme plus tôt et aller plus vite (optionnel)
        people = people + int(line[4])
        departements.append(line[3]) #liste de départements qu'on utilisera + tard

    else:
        if founded:
            break #on arrête la boucle plus tôt pour économiser du temps

#2nde init pour les départements
departementsUtilises = []
biggestDepartement = 0
nbrBiggestDepartement = 0


for i in range(len(departements)): #pour voir le meilleur département

    if departementsUtilises.count(departements[i]) == 0: #on passe que si on n'a jamais traité le département
        departementsUtilises.append(departements[i]) #on l'ajoute pour ne plus le refaire
        if nbrBiggestDepartement < departements.count(departements[i]): #on voit si il y a + de personnes dans ce département que dans le + gros actuel
            nbrBiggestDepartement = departements.count(departements[i]) #on remplace les valeurs
            biggestDepartement = departements[i]

print("Il y a", people, "personnes qui sont nées avec le prénom", research, "depuis 1900. De plus, ils sont nés majoritairement dans le", biggestDepartement, "ème département de la France avec", nbrBiggestDepartement, "personne(s) ! ")









