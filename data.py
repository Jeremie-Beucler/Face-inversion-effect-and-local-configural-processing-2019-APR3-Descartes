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
		
bar_chart('Perf (%)', 'Floutage', 'Orientation', 'Local', 'Configural', 'Envers', 'Endroit', list_bar_orien, list_error_orien)

		