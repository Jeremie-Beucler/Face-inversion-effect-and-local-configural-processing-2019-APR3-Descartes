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
		elif abs(((elt - mean_rt) / standard_dev_rt)) > 3:
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
		