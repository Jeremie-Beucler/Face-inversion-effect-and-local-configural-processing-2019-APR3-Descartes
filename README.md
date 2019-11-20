# Memoire-APR3

##Mise au point de l'expérience

###Elaboration des stimuli

Les paires de visages sont tirées de la *Chicago Face Database*, dont les conditions d'exposition sont standardisées, et ont été détourées et mises en noir et blanc grâce au logiciel *Gimp*. Le floutage et l'orientation ont ensuite été ajoutés grâce à Powerpoint.

###Codage de l'expérience

Il s'agit d'une expérience de discrimination de visages réalisée sur *Python 3* à l'aide du module *Expyriment*. 

Il y a deux facteurs à deux modalités: Orientation (endroit/envers) et Floutage de la zone des yeux (partiel/total), soit 4 conditions. 

Une croix de fixation précède chaque présentation durant 1500ms, et est suivie de la présentation aléatoire de deux photos appartenant à l'une des quatre conditions.

![](P2MDEK.jpg)

*Exemple: photo de deux visages à l'envers dont l'intérieur des yeux est flouté.* 

A chaque fois, le participant doit indiquer si les photos de la paire présentée sont pareils ou différents. Il y a 10 paires d'entraînement, suivies de 64 paires présentées dans un ordre aléatoire.

```
"""Expérience de discrimination de visages à 4 conditions à l'aide d'Expyriment dont les résultats par sujet sont enregistrés dans un dossier 'data'"""

# -*- coding: utf-8 -*-
import random
import expyriment

counter = 0
while counter < 1:
    nb = int(input("Entrez un nombre entre 1 et 2:"))
    if nb == 1:
        letter_key_same = 'L'
        letter_key_diff = 'S'
        nb_key_same = 108
        counter += 1
    elif nb == 2:
        letter_key_same = 'S'
        letter_key_diff = 'L'
        nb_key_same = 115
        counter +=1
    else:
        counter = counter
#permet de changer une fois sur deux la touche 'pareil' et la touche 'différent' pour contrebalancer les effets de latéralité

exp = expyriment.design.Experiment(name="Perception des visages")
expyriment.control.initialize(exp)


text_1 = expyriment.stimuli.TextLine(text="Expérience APR3 - Tâche de discrimination", text_size=43, text_bold=True)
text_2 = expyriment.stimuli.TextScreen(heading="Instructions", text="\n\n\n\n\n\n\n\n\nVous allez voir des paires de visage. Appuyez sur la touche '" + letter_key_same + "' si les deux visages sont pareils et sur la touche '" + letter_key_diff + "' si les deux visages sont différents, le plus rapidement et le plus précisément possible. \n\n(Appuyez sur une touche pour continuer)", heading_size=30, heading_underline=True)
text_3 = expyriment.stimuli.TextScreen(heading="Entraînement", text="\n\n\n\nVous avez droit à 10 essais d'entraînement.\n\n Appuyez sur une touche pour continuer.")
text_4 = expyriment.stimuli.TextLine(text="Préparez-vous en mettant vos doigts sur les touches. L'expérience commence dans 5 secondes:")

list_rebours = []
compte_a_reb_1 = expyriment.stimuli.TextLine(text="5", text_size=45)
list_rebours.append(compte_a_reb_1)
compte_a_reb_2 = expyriment.stimuli.TextLine(text="4", text_size=45)
list_rebours.append(compte_a_reb_2)
compte_a_reb_3 = expyriment.stimuli.TextLine(text="3", text_size=45)
list_rebours.append(compte_a_reb_3)
compte_a_reb_4 = expyriment.stimuli.TextLine(text="2", text_size=45)
list_rebours.append(compte_a_reb_4)
compte_a_reb_5 = expyriment.stimuli.TextLine(text="1", text_size=45)
list_rebours.append(compte_a_reb_5)
#création des textes (consignes, etc.) précédant l'expérience

upr_tot = []
upd_tot = []
upr_part = []
upd_part = []
same = []
diff = []
l_glob = []
list_stim = []
#création de 4 listes pour les 4 conditions + 2 selon pareil/différent + 2 pour la présentation de tous les stimuli

for i in range(1, 5):
	l_glob.append('P' + str(i) + 'FDAT' + '.jpg')
	l_glob.append('P' + str(i) + 'FDAK' + '.jpg')
	l_glob.append('P' + str(i) + 'MDAT' + '.jpg')
	l_glob.append('P' + str(i) + 'MDAK' + '.jpg')
	l_glob.append('P' + str(i) + 'FDET' + '.jpg')
	l_glob.append('P' + str(i) + 'FDEK' + '.jpg')
	l_glob.append('P' + str(i) + 'MDET' + '.jpg')
	l_glob.append('P' + str(i) + 'MDEK' + '.jpg')
	l_glob.append('P' + str(i) + 'FSAT' + '.jpg')
	l_glob.append('P' + str(i) + 'FSAK' + '.jpg')
	l_glob.append('P' + str(i) + 'MSAT' + '.jpg')
	l_glob.append('P' + str(i) + 'MSAK' + '.jpg')
	l_glob.append('P' + str(i) + 'FSET' + '.jpg')
	l_glob.append('P' + str(i) + 'FSEK' + '.jpg')
	l_glob.append('P' + str(i) + 'MSET' + '.jpg')
	l_glob.append('P' + str(i) + 'MSEK' + '.jpg')
#créé les noms des fichiers par rapport au facteur sexe (M/F), pareil/différent (S/D), endroit/envers (A/E), et floutage des yeux partiel/total(K/T)
#donc nécessite que les photos aient des noms précis pour fonctionner

upr_l = []
upd_l = []
part_l = []
tot_l = []
#création de 4 sous-listes pour distribuer dans les 4 listes des 4 conditions (voir block ci-dessous)

y = 0
while y < len(l_glob):
	list_stim.append(expyriment.stimuli.Picture(filename=l_glob[y]))
	list_stim[y].preload()
	
	for letter in l_glob[y]:
		if letter == 'D':
			diff.append(list_stim[y])
		elif letter == 'S':
			same.append(list_stim[y])
	#code for same or diff (for futur responses)	
		elif letter == 'A':
			upr_l.append(list_stim[y])
		elif letter == 'E':
			upd_l.append(list_stim[y])
		elif letter == 'T':
			tot_l.append(list_stim[y])
		elif letter == 'K':
			part_l.append(list_stim[y])
	if list_stim[y] in upr_l and list_stim[y] in tot_l:
		upr_tot.append(list_stim[y])
	elif list_stim[y] in upd_l and list_stim[y] in tot_l:
		upd_tot.append(list_stim[y])
	elif list_stim[y] in upr_l and list_stim[y] in part_l:
		upr_part.append(list_stim[y])
	elif list_stim[y] in upd_l and list_stim[y] in part_l:
		upd_part.append(list_stim[y])
	y +=1
	#distribue le stim dans les 4 listes selon les différents facteurs (4 conditions: upr_tot, etc.)

random.shuffle(list_stim)
list_train = list_stim[0: 10]
#créé une liste d'entraînement de 10 stim au hasard parmi les stimuli
random.shuffle(list_stim)


cross = expyriment.stimuli.FixCross(colour=(255, 255, 255))
cross.preload()
#importe la croix de fixation

exp.data_variable_names = ["Condition", "Correct", "RT"]
#créé les différentes colonnes du fichier 'data'

expyriment.control.start()

text_1.present()
exp.keyboard.wait()
text_2.present()
exp.keyboard.wait()
text_3.present()
exp.keyboard.wait()
#donne les consignes au sujet

for elt in list_train:
	cross.present()
	exp.clock.wait(1500)
	elt.present()
	exp.keyboard.wait([expyriment.misc.constants.K_l,
								expyriment.misc.constants.K_s])
#liste d'entraînement de 10 stimuli dont les données ne sont pas prises en compte dans les résultats

text_4.present()
exp.clock.wait(3500)
for elt in list_rebours:
	elt.present()
	exp.clock.wait(1000)
	
for elt in list_stim:
		cross.present()
		exp.clock.wait(1500)
		elt.present()
		key, rt = exp.keyboard.wait([expyriment.misc.constants.K_l,
									expyriment.misc.constants.K_s])
		
		if elt in upr_tot:
			if elt in same:
				if key == nb_key_same:
					exp.data.add(["upr_tot", "correct", rt])

				else:
					exp.data.add(["upr_tot", "false", rt])
					
			if elt in diff:
				if key == nb_key_same:
					exp.data.add(["upr_tot", "false", rt])
					
				else:
					exp.data.add(["upr_tot", "correct", rt])
					
		
		if elt in upr_part:
			if elt in same:
				if key == nb_key_same:
					exp.data.add(["upr_part", "correct", rt])
					
				else:
					exp.data.add(["upr_part", "false", rt])
					
			if elt in diff:
				if key == nb_key_same:
					exp.data.add(["upr_part", "false", rt])
					
				else:
					exp.data.add(["upr_part", "correct", rt])
					
					
		if elt in upd_tot:
			if elt in same:
				if key == nb_key_same:
					exp.data.add(["upd_tot", "correct", rt])
					
				else:
					exp.data.add(["upd_tot", "false", rt])
					
			if elt in diff:
				if key == nb_key_same:
					exp.data.add(["upd_tot", "false", rt])
					
				else:
					exp.data.add(["upd_tot", "correct", rt])
					
		
		if elt in upd_part:
			if elt in same:
				if key == nb_key_same:
					exp.data.add(["upd_part", "correct", rt])
					
				else:
					exp.data.add(["upd_part", "false", rt])

			if elt in diff:
				if key == nb_key_same:
					exp.data.add(["upd_part", "false", rt])
					
				else:
					exp.data.add(["upd_part", "correct", rt])
#selon la condition dans laquelle se trouve le stimulus, enregistre si sa réponse est correcte ainsi que son temps de réaction dans un fichier xpd dans le dossier 'data'
			
expyriment.control.end(goodbye_text="Merci pour votre participation!")
```
##Analyse des données

###Conversion en fichiers *.csv* et suppression des premières lignes

Il m'a ensuite fallu convertir les fichiers *.xpd* en fichiers *.csv* et supprimer les premières lignes des fichiers qui contenaient des informations inutiles.

Sur internet, j'ai trouvé cette petite manip' pour changer rapidement l'extension de plusieurs fichiers.

```
@echo off
ren *.xpd *.csv
```
Il ne me restait plus qu'à supprimer les premières lignes de mes fichiers *.csv*.

```
import csv
import os

for csvFilename in os.listdir('.'):
	if not csvFilename.endswith('.csv'):
		continue
#si le fichier n'est pas en .csv, le programme ne le prend pas en compte
	elif 'new' in csvFilename:
		continue
	csvRows = []
	csvFileObj = open(csvFilename)
	readerObj = csv.reader(csvFileObj)
	for row in readerObj:
		if readerObj.line_num in range(1, 11):
			continue
#saute les 11 premières lignes (celles que l'on souhaite supprimer ici)			

		csvRows.append(row)
	csvFileObj.close()
	csvFileObj = open('new' + csvFilename, 'w', newline='')
	csvWriter = csv.writer(csvFileObj)
	for row in csvRows:
		csvWriter.writerow(row)
	csvFileObj.close()
#créé un nouveau fichier csv que l'on va utiliser pour la suite	

		csvRows.append(row)
	csvFileObj.close()
	csvFileObj = open('new' + csvFilename, 'w', newline='')
	csvWriter = csv.writer(csvFileObj)
	for row in csvRows:
		csvWriter.writerow(row)
	csvFileObj.close()
```

###Traitement des données

Une fois cela effectué, l'on dispose donc de fichiers *.csv* utilisables directement.

####Suppression des "outliers"

Il restait à supprimer les données aberrantes, celles pour lesquelles le sujet avait répondu en moins de 300ms ou celles dont le score Z était supérieur à trois (les réponses beaucoup trop rapides, ou beaucoup trop lentes par rapport aux autres réponses du sujet. Cela a été effectué grâce au module *Pandas*.

```
import os
import pandas as pd

for csvFilename in os.listdir('.'):
	if not csvFilename.endswith('.csv'):
		continue
#ne prend en compte que les fichiers .csv
	data_frame = pd.read_csv(csvFilename)
#créé un 'data frame' avec pandas à partir du fichier csv
	mean_rt = data_frame.RT.mean()
	standard_dev_rt = data_frame.RT.std()
	i = 0
	elt_to_del = []
	for elt in data_frame.RT:
		if elt < 300:
			elt_to_del.append(i)
		elif abs(((elt - mean_rt) / standard_dev_rt)) > 3:
			elt_to_del.append(i)
		else: 
			i += 1
	counter = 0
#supprime les données aberrates par rapport aux rt
	if len(elt_to_del) != 0:
		for elt in elt_to_del:
			print("Supression de la ligne excel (", csvFilename, "): ", elt + counter + 2)
			print(data_frame.iloc[int(elt)])
#m'informe des données qui ont été supprimées pour que je puisse vérifier leur nombre, etc.
			print('')
			data_frame = data_frame.drop(data_frame.index[elt])
			counter += 1
			data_frame = data_frame.reset_index(drop=True)
		data_frame.to_csv('corrected' + csvFilename)
#si des données aberrantes ont été supprimées, enregistre le résultat sans écraser le premier fichier
	else:
		data_frame.to_csv(csvFilename)
```

####Statistiques descriptives

Toujours grâce au module *Pandas* ainsi qu'au module *Statistics*, il ne restait plus qu'à lire les fichiers *.csv* de chaque sujet et à sommer les résultats de tous les sujets en fonction des différentes conditions pour obtenir les temps de réaction en ms et les performances en %.

```
import os
import pandas as pd
import statistics as stat

mean_rt_upr_tot = 0
mean_rt_upr_part = 0
mean_rt_upd_tot = 0
mean_rt_upd_part = 0

sd_rt_upr_tot = 0
sd_rt_upr_part = 0
sd_rt_upd_tot = 0
sd_rt_upd_part = 0

mean_prf_upr_tot = []
mean_prf_upr_part = []
mean_prf_upd_tot = []
mean_prf_upd_part = []

sd_prf_upr_tot = []
sd_prf_upr_part = []
sd_prf_upd_tot = []
sd_prf_upd_part = []



for csvFilename in os.listdir('.'):
#boucle sur chaque fichier .csv, i.e. sur chaque sujet
	if not csvFilename.endswith('.csv'):
		continue
#ne prend en compte que les fichiers csv

	df = pd.read_csv(csvFilename)
	df_upr_tot = df[df.Condition == 'upr_tot']
	df_upr_tot_corr = df_upr_tot[df_upr_tot.Correct == 'correct']
	mean_rt_upr_tot += df_upr_tot_corr.RT.mean()
	sd_rt_upr_tot += df_upr_tot_corr.RT.std(ddof=0)
	nb_corr_upr_tot = df_upr_tot_corr.RT.count()
	nb_upr_tot = df_upr_tot.RT.count()
	mean_prf_upr_tot.append((nb_corr_upr_tot / nb_upr_tot) * 100)
#somme les données pour chaque condition (ici: upr_tot)
	
	df_upr_part = df[df.Condition == 'upr_part']
	df_upr_part_corr = df_upr_part[df_upr_part.Correct == 'correct']
	mean_rt_upr_part += df_upr_part_corr.RT.mean()
	sd_rt_upr_part += df_upr_part_corr.RT.std(ddof=0)
	nb_corr_upr_part = df_upr_part_corr.RT.count()
	nb_upr_part = df_upr_part.RT.count()
	mean_prf_upr_part.append((nb_corr_upr_part / nb_upr_part) * 100)
	
	df_upd_tot = df[df.Condition == 'upd_tot']
	df_upd_tot_corr = df_upd_tot[df_upd_tot.Correct == 'correct']
	mean_rt_upd_tot += df_upd_tot_corr.RT.mean()
	sd_rt_upd_tot += df_upd_tot_corr.RT.std(ddof=0)
	nb_corr_upd_tot = df_upd_tot_corr.RT.count()
	nb_upd_tot = df_upd_tot.RT.count()
	mean_prf_upd_tot.append((nb_corr_upd_tot / nb_upd_tot) * 100)
	
	df_upd_part = df[df.Condition == 'upd_part']
	df_upd_part_corr = df_upd_part[df_upd_part.Correct == 'correct']
	mean_rt_upd_part += df_upd_part_corr.RT.mean()
	sd_rt_upd_part += df_upd_part_corr.RT.std(ddof=0)
	nb_corr_upd_part = df_upd_part_corr.RT.count()
	nb_upd_part = df_upd_part.RT.count()
	mean_prf_upd_part.append((nb_corr_upd_part / nb_upd_part) * 100)

print('\nupr_tot\n')
print('rt')
print(round(mean_rt_upr_tot / 20))
print(round(sd_rt_upr_tot / 20))
print('prf')
print(round(stat.mean(mean_prf_upr_tot), 2))
print(round(stat.pstdev(mean_prf_upr_tot), 2))
print('upr_part\n')
print('rt')
print(round(mean_rt_upr_part / 20))
print(round(sd_rt_upr_part / 20))
print('prf')
print(round(stat.mean(mean_prf_upr_part), 2))
print(round(stat.pstdev(mean_prf_upr_part), 2))
print('upd_tot\n')
print('rt')
print(round(mean_rt_upd_tot / 20))
print(round(sd_rt_upd_tot / 20))
print('prf')
print(round(stat.mean(mean_prf_upd_tot), 2))
print(round(stat.pstdev(mean_prf_upd_tot), 2))
print('upd_part\n')
print('rt')
print(round(mean_rt_upd_part / 20))
print(round(sd_rt_upd_part / 20))
print('prf')
print(round(stat.mean(mean_prf_upd_part), 2))
print(round(stat.pstdev(mean_prf_upd_part), 2))
#sort les résultats pour tous les sujets
```
