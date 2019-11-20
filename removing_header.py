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
