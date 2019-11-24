# Code du projet APR3

## Mise au point de l'expérience grâce au module [Expyriment](https://www.expyriment.org/)

### Contrebalancement de la latéralité

Pour éliminer les effets de la latéralité (e.g. les sujets droitiers appuieront systématiquement plus vite à droite qu'à gauche), j'ai fait en sorte que l'expérimentateur doive rentrer, au début du programme, une fois sur deux le chiffre *1*, et une fois sur deux le chiffre *2*. En fonction du chiffre rentré, les touches pour les réponses "pareil" et "différents" n'étaient pas les mêmes.

*Axe d'amélioration: j'aurais pu utiliser le module python "sis", pour faire en sorte de rentrer le chiffre en même temps que l'on exécutait le programme sur le terminal, en tant qu'argument (e.g. python experience_apr.py 1), pour gagner du temps et être plus élégant*

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
```

### Elaboration des consignes

Pour créer les consignes, je n'avais quà créer des variables *"expyriment.stimuli.TextLine/TextScreen".*
```
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
```
### Répartition des stimuli dans les différentes conditions

Ensuite, je devais répartir les différents stimuli dans les différentes conditions. Pour ce faire, je me suis servi des noms des fichiers (qui correspondaient aux différents facteurs). Par exemple, un fichier appelé *"P1FDAT.jpg"* correspondait à une paire de visages féminins différents à l'endroit avec un floutage oculaire total. Le programme scanne le nom du fichier et le distribue dans une des conditions.

*Axe d'amélioration:j'aurais pu utiliser les fonctions Expyriment "Block" et "Trials" pour répartir mes différents stimuli dans les différentes conditions; cela aurait été aussi long en terme de code, mais plus élégant et plus efficace pour l'analyse des réponses du participant*

```
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
```

### Création de la liste d'entraînement, de la croix de fixation, et des facteurs enregistrés pour chaque réponse

Pour créer la liste d'entraînement, je prélève 10 stimuli au hasard de la liste des stimuli, puis j'en mélange l'ordre. Cela permet d'avoir à chaque passation 10 stimuli d'entraînement différents, et de ne pas avoir d'effets d'ordre.

Ensuite, j'importe la croix de fixation (précodée par Expyriment avec l'objet *"FixCross"*).

Enfin, je crée les différentes colonnes du fichier *data* contenant les réponses de mon participant (condition du stimulus, réponse correcte/incorrecte, temps de réaction).

```
random.shuffle(list_stim)
list_train = list_stim[0: 10]
#créé une liste d'entraînement de 10 stim au hasard parmi les stimuli
random.shuffle(list_stim)


cross = expyriment.stimuli.FixCross(colour=(255, 255, 255))
cross.preload()
#importe la croix de fixation

exp.data_variable_names = ["Condition", "Correct", "RT"]
#créé les différentes colonnes du fichier 'data'
```

### Présentation des consignes et liste d'entraînement

Je lance l'expérience, présente les consignes, et présenteles stimuli de la liste d'entraînement sans enregistrer les réponses de mes sujets.
```
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
```

### Passation de l'expérience et enregistrement des données

Avant chaque stimuli, la croix de fixation apparaît pendant 1500 ms. Ensuite, en fonction de la condition dans laquelle se trouve le stimulus, les réponses du sujet sont enregistrée (condition, correct/incorrect, temps de réaction).

*Axe d'amélioration: comme dit précédemment, avec les fonctions Block et Trial, ce code-ci eût pu être beaucoup plus bref et simple; la condition aurait pu être enregisté automatiquement, etc.*

```
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

## Analyse des données

### Conversion en fichiers *.csv* et suppression des premières lignes

Il m'a ensuite fallu convertir les fichiers *.xpd* en fichiers *.csv*, pour faciliter l'analyse des données, et supprimer les premières lignes des fichiers qui contenaient des informations inutiles.

Sur [Internet](https://www.sospc95.fr/blog/modifier-lextension-de-plusieurs-fichiers-en-1-clic/), j'ai trouvé cette petite manip' pour changer rapidement l'extension de plusieurs fichiers grâce à un fichier *.bat*.

```
@echo off
ren *.xpd *.csv
```
Il ne me restait plus qu'à supprimer les premières lignes de mes fichiers *.csv*, qui ne contenaient pas les réponses des participants. Pour ce faire, j'ai légèrement modifié le code proposé sur le site [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/chapter14/).

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

### Réduction des données

Une fois cela effectué, l'on dispose donc de fichiers *.csv* utilisables directement.

#### Suppression des sujets "outliers"

Sur les conseils de l'enseignante d'APR3, il fallait supprimer les "outliers". Le critère fixé était ceux dont le score Z pour les temps de réaction étaient supérieurs à 3 (en valeur absolue).

Pour cela, j'ai utilisé le module [Pandas (Python Data Analysis Library)](https://pandas.pydata.org/), qui permet de lire les fichiers *.csv* et d'effectuer des opérations statistiques dessus en créant des *data frame*.

```
import os
import pandas as pd
import statistics as stat

nb_file = 0
list_mean_rt_participants = []
for csvFilename in os.listdir('.'):
	if not csvFilename.endswith('.csv'):
		continue
#ne prend en compte que les fichiers .csv
	data_frame = pd.read_csv(csvFilename)
	list_mean_rt_participants.append(data_frame.RT.mean())

mean_rt_participants = stat.mean(list_mean_rt_participants)
std_rt_participants = stat.pstdev(list_mean_rt_participants)
print(mean_rt_participants)
print(std_rt_participants)
#calcule la moyenne des rt des participants ainsi que l'écart-type de cette distribution

for csvFilename in os.listdir('.'):
	if not csvFilename.endswith('.csv'):
		continue
#ne prend en compte que les fichiers .csv
	data_frame = pd.read_csv(csvFilename)
	if abs(((data_frame.RT.mean() - mean_rt_participants) / std_rt_participants)) > 3:
		print('Must suppress :' + csvFilename)
		print('Mean rt of this file: ' + str(data_frame.RT.mean()))
#informe du sujet aberrant à supprimer (si son score Z est supérieur à 3 en valeur absolue
```

#### Suppression des données aberrantes

Il restait à supprimer les données aberrantes, celles pour lesquelles le sujet avait répondu en moins de 300 ms ou celles dont le score Z était supérieur à 2(les réponses beaucoup trop rapides, ou beaucoup trop lentes par rapport aux autres réponses du sujet). 

```
for csvFilename in os.listdir('.'):
	if not csvFilename.endswith('.csv'):
		continue
	data_frame = pd.read_csv(csvFilename)
	mean_rt = data_frame.RT.mean()
	standard_dev_rt = data_frame.RT.std()
	i = 0
	elt_to_del = []
	for elt in data_frame.RT:
		if elt < 300:
			elt_to_del.append(i)
		elif abs(((elt - mean_rt) / standard_dev_rt)) > 2:
			elt_to_del.append(i)
		else: 
			i += 1
	counter = 0
#supprime les données aberrates par rapport aux  du sujet en question
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

### Statistiques descriptives et graphique (*bar chart*)

Toujours grâce au module *Pandas* ainsi qu'au module *Statistics*, il ne restait plus qu'à lire les fichiers *.csv* de chaque sujet et à sommer les résultats de tous les sujets en fonction des différentes conditions pour obtenir les temps de réaction en ms des réponses correctes et les performances en %. 

#### Statistiques descriptives

```
import os
import pandas as pd
import statistics as stat
import matplotlib.pyplot as plt
import numpy as np

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
prf_upr_tot = round(stat.mean(mean_prf_upr_tot), 2)
print(prf_upr_tot)
std_upr_tot = round(stat.pstdev(mean_prf_upr_tot), 2)
print(std_upr_tot)
print('upr_part\n')
print('rt')
print(round(mean_rt_upr_part / 20))
print(round(sd_rt_upr_part / 20))
print('prf')
prf_upr_part = round(stat.mean(mean_prf_upr_part), 2)
print(prf_upr_part)
std_upr_part = round(stat.pstdev(mean_prf_upr_part), 2)
print(std_upr_part)
print('upd_tot\n')
print('rt')
print(round(mean_rt_upd_tot / 20))
print(round(sd_rt_upd_tot / 20))
print('prf')
prf_upd_tot = round(stat.mean(mean_prf_upd_tot), 2)
print(prf_upd_tot)
std_upd_tot = round(stat.pstdev(mean_prf_upd_tot), 2)
print(std_upd_tot)
print('upd_part\n')
print('rt')
print(round(mean_rt_upd_part / 20))
print(round(sd_rt_upd_part / 20))
print('prf')
prf_upd_part = round(stat.mean(mean_prf_upd_part), 2)
print(prf_upd_part)
std_upd_part = round(stat.pstdev(mean_prf_upd_part), 2)
print(std_upd_part)
#sort les résultats pour tous les sujets
```

### Gaphique

Ensuite, grâce au module Matplotlib, je pouvais utiliser les résultats pour en faire un graphique.

```
list_bar_orien = [prf_upd_tot, prf_upr_tot, prf_upd_part, prf_upr_part]
list_error_orien = [std_upd_tot, std_upr_tot, std_upd_part, std_upr_part]

def bar_chart(VD, name_X, name_C, name_x1, name_x2, name_c1, name_c2, scores, errors):
	"""scores must be a list of 4 elements: c1x1, c2x1, c1x2, c2x2"""

	fig, ax = plt.subplots()
	index = np.arange(2)
	bar_width = 0.35
	opacity = 0.8

	rects1 = plt.bar(index, (scores[0], scores[2]), bar_width,
	alpha=opacity,
	color='b',
	label=name_c1)
	plt.errorbar(index, (scores[0], scores[2]), yerr=(errors[0], errors[2]), fmt='none', ecolor='black', capsize=4)

	rects2 = plt.bar(index + bar_width, (scores[1], scores[3]), bar_width,
	alpha=opacity,
	color='g',
	label=name_c2)
	plt.errorbar(index + bar_width, (scores[1], scores[3]), yerr =(errors[1], errors[3]), fmt='none', ecolor='black', capsize=4)

	plt.xlabel(name_X)
	plt.ylabel(VD)
	titlefig = VD + '_by_' + name_X + '_and_' + name_C + '.png'
	plt.title('\n')
	nb = (bar_width / 2)
	plt.xticks(index + nb, (name_x1, name_x2))
	plt.legend(title=name_C, loc= 'center right')
	
	plt.tight_layout()
	plt.savefig(titlefig)
		
bar_chart('Perf (%)', 'Floutage', 'Orientation', 'Tot', 'Part', 'Upd', 'Upr', list_bar_orien, list_error_orien)	
```

Le résultat est le suivant:

![Graphique obtenu suite à l'analyse des résultats](Perf (%)_by_Floutage_and_Orientation.png)

## Conclusion

### Ce que j'ai retiré de ce projet

J'ai beaucoup retiré de ce travail.

Tout d'abord, il m'a permis de **me familiariser avec la démarche expérimentale**, de voir comment designer une expérience du début à la fin: s'inspirer de la littérature, trouver ses facteurs et les opérationnaliser, fabriquer son matériel en contrôlant les paramètres, créer la procédure, faire passer l'expérience, analyser ses données. Cela m'a permis de concrétiser ce que l'on apprend notamment en TD d'EXPE2.

Ensuite, il m'a permis d'**appliquer ce que j'apprenais en cours de programmation** à l'ENS, et notamment l'utilisation d'*Expyriment* et de *Pandas*, ainsi que de *Github* pour présenter son propre travail.

### Les axes d'amélioration

#### Le travail d'équipe

Ce projet était à réaliser en équipe de trois, et je ne connaissais pas mes partenaires, qui faisaient partie de mon groupe de TD, au début du projet. J'ai souvent eu l'impression d'effectuer une grande partie du travail de mon côté (même en retirant la partie programmation). Si cela m'a permis de gagner en autonomie, je n'ai pas vraiment appris à travailler en équipe aussi bien que j'aurais dû, et inversement, je ne pense pas qu'ils aient retiré autant qu'ils auraient pu de ce projet. Cependant, nous avons quand même bien échangé sur la partie concernant le *design* de l'expérience. 

Enfin, il était un peu frustrant de voir que tout le monde n'apportait pas le même soin à la réalisation du travail. Ainsi,  l'un des partenaires faisait passer ses sujets au CROUS, ou encore au café. De même, alors qu'il n'avait qu'à rajouter les floutages sur les différents stimuli, le floutage partiel a été réalisé de façon différente entre les visages masculins et les visages féminins...

#### Le nombre de visages présentés et le design expérimental

L'expérience ne présentait que 16 visages différents, dans la mesure où tous les facteurs étaient en intra-sujet et que nous ne voulions pas que l'expérience dure trop longtemps (sachant que nos sujets n'étaient pas payés). Peut-être aurait-il fallu passer les facteurs en inter-sujet pour éviter cet écueil, et ainsi présenter un plus grand nombre de visages!

#### La clarté du code

Sachant que j'ai commencé à coder pour l'expérience très tôt dans le semestre, le code n'est pas optimal, ni très propre. J'ai pour projet de le reprendre pour le rendre plus efficace et plus lisible par les autres, ce qui fait partie de la démarche scientifique (principe de *communicabilité*).

#### Les statistiques inférentielles et la condition contrôle

Il était un peu frustrant de devoir se limiter aux statistiques descriptives, dans la mesure où l'UE de Statistiques de Descartes n'avait lieu qu'au second semestre.

De même, il aurait pu être intéressant de rajouter une condition contrôle avec des visages non-floutés, pour comparer les résultats avec les conditions Floutage. Mais les consignes de l'UE de l'Université stipulaient qu'il ne fallait que deux facteurs à deux modalités.

### Remerciements

- **l'enseignante de l'UE APR3** de l'Université Paris Descartes pour ses conseils concernant le design de l'expérience, les facteurs à contrôler, le traitement des données (exclusion des outliers, etc.);
- **mon professeur de programmation du cours PCBS** à l'ENS pour son enseignement de la programmation et les nombreux outils qu'il nous a fournis (Expyriment, Pandas, Github et Git, Automatetheboringstuff, Pygame, son propre site, etc.);
- et bien sûr, **mes deux collègues de L2 de Psychologie** avec qui j'ai effectué ce travail dans le cadre de l'UE APR3.





