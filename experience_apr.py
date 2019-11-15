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
#counterbalance the laterality

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
#création des textes précédant l'expérience

upr_tot = []
upd_tot = []
upr_part = []
upd_part = []
same = []
diff = []
l_glob = []
list_stim = []
#4 listes pour les 4 conditions + 2 selon pareil/différent + 2 pour la présentation de tous les stimuli

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
#generate the filenames of the pictures according to the factor sex M/F, same/different S/D, upright/upside-down A/E, and K/T partiel/total 
#and put them in a list (so the pictures need to have precise names for the program to work)

upr_l = []
upd_l = []
part_l = []
tot_l = []
#sous-listes pour distribuer dans les 4 listes des 4 conditions (voir block ci-dessous)

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
	#distribue le stim selon les différents facteurs: 4 conditions

random.shuffle(list_stim)
list_train = list_stim[0: 10]
#créé une liste d'entraînement de 10 stim au hasard
random.shuffle(list_stim)


cross = expyriment.stimuli.FixCross(colour=(255, 255, 255))
cross.preload()
#croix de fixation

upr_tot_rt = 0
upr_tot_prf = 0
upd_tot_rt = 0
upd_tot_prf = 0
upr_part_rt = 0
upr_part_prf = 0
upd_part_rt = 0
upd_part_prf = 0

exp.data_variable_names = ["Condition", "Correct", "RT"]

expyriment.control.start()

text_1.present()
exp.keyboard.wait()
text_2.present()
exp.keyboard.wait()
text_3.present()
exp.keyboard.wait()

for elt in list_train:
	cross.present()
	exp.clock.wait(1500)
	elt.present()
	exp.keyboard.wait([expyriment.misc.constants.K_l,
								expyriment.misc.constants.K_s])
#liste d'entraînement de 10 stimuli dont les données ne sont pas prises en compte

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
					upr_tot_prf += 1
					upr_tot_rt += rt
				else:
					exp.data.add(["upr_tot", "false", rt])
					upr_tot_rt += rt
			if elt in diff:
				if key == nb_key_same:
					exp.data.add(["upr_tot", "false", rt])
					upr_tot_rt += rt
				else:
					exp.data.add(["upr_tot", "correct", rt])
					upr_tot_prf += 1
					upr_tot_rt += rt
		
		if elt in upr_part:
			if elt in same:
				if key == nb_key_same:
					exp.data.add(["upr_part", "correct", rt])
					upr_part_prf += 1
					upr_part_rt += rt
				else:
					exp.data.add(["upr_part", "false", rt])
					upr_part_rt += rt
			if elt in diff:
				if key == nb_key_same:
					exp.data.add(["upr_part", "false", rt])
					upr_part_rt += rt
				else:
					exp.data.add(["upr_part", "correct", rt])
					upr_part_prf += 1
					upr_part_rt += rt
					
		if elt in upd_tot:
			if elt in same:
				if key == nb_key_same:
					exp.data.add(["upd_tot", "correct", rt])
					upd_tot_prf += 1
					upd_tot_rt += rt
				else:
					exp.data.add(["upd_tot", "false", rt])
					upd_tot_rt += rt
			if elt in diff:
				if key == nb_key_same:
					exp.data.add(["upd_tot", "false", rt])
					upd_tot_rt += rt
				else:
					exp.data.add(["upd_tot", "correct", rt])
					upd_tot_prf += 1
					upd_tot_rt += rt
		
		if elt in upd_part:
			if elt in same:
				if key == nb_key_same:
					exp.data.add(["upd_part", "correct", rt])
					upd_part_prf += 1
					upd_part_rt += rt
				else:
					exp.data.add(["upd_part", "false", rt])
					upd_part_rt += rt
			if elt in diff:
				if key == nb_key_same:
					exp.data.add(["upd_part", "false", rt])
					upd_part_rt += rt
				else:
					exp.data.add(["upd_part", "correct", rt])
					upd_part_prf += 1
					upd_part_rt += rt
			
expyriment.control.end(goodbye_text="Merci pour votre participation!")

nb_tot_stim = len(list_stim)

mean_PRF_upr_tot = str(round((upr_tot_prf/(nb_tot_stim/4)) * 100))
mean_PRF_upr_part = str(round((upr_part_prf/(nb_tot_stim/4)) * 100))
mean_PRF_upd_tot = str(round((upd_tot_prf/(nb_tot_stim/4)) * 100))
mean_PRF_upd_part = str(round((upd_part_prf/(nb_tot_stim/4)) * 100))
mean_RT_upr_tot = str(round((upr_tot_rt/(nb_tot_stim/4))))
mean_RT_upr_part = str(round((upr_part_rt/(nb_tot_stim/4))))
mean_RT_upd_tot = str(round((upd_tot_rt/(nb_tot_stim/4))))
mean_RT_upd_part = str(round((upd_part_rt/(nb_tot_stim/4))))

resultsFile = open('results.txt', 'a')
resultsFile.write(mean_PRF_upr_tot + ',' + mean_PRF_upr_part + ',' + mean_PRF_upd_tot + ',' + mean_PRF_upd_part + ',' + mean_RT_upr_tot + ',' + mean_RT_upr_part + ',' + mean_RT_upd_tot + ',' + mean_RT_upd_part + '\n')
resultsFile.close()


