import pandas as pd
import pprint
import random
import os
import webbrowser
from termcolor import colored


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def train(chunk,company):
	df = pd.read_excel('C:/JospehShen/XunTa/data/train.xlsx', index_col=0)
	df = df[df['Company'].isin([company]) & df['Round'].isin(['Onsite'])]
	questions = list(df['Question'])
	answers = list(df['Answer'])
	qapair = list(zip(questions,answers))
	if len(qapair) > chunk:
		qapair = random.sample(qapair, chunk)
	pp = pprint.PrettyPrinter(indent=2)

	# if company == 'Wayfair':
	# 	print('start coding challenge ...')
	# 	os.startfile('C:/JospehShen/XunTa/coding/{}/simulationpi.py'.format(company))
	# 	os.startfile('C:/JospehShen/XunTa/coding/{}/simulationpisol.py'.format(company))
	# 	mianjing = 'https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=674933&ctid=230653'
	# 	webbrowser.open_new_tab(mianjing)
	# 	webbrowser.open_new_tab('https://leetcode.com/problems/sqrtx/')

	boost = []
	score = len(qapair)
	weak = 0
	for q,a in qapair:
		pp.pprint(q)
		print()
		cont = input('press `c` to continue and press `s` to see solution >')
		if cont == 's':
			pp.pprint(a)
			score -= 1
			weak += 1
			boost.append((q,a, weak))
		if cont != 'c' and cont !='s':
			break

	print('Your score is {}'.format(round(score/len(qapair)*100,0)))
	print('Now start debugging problems you failed to answer...')


	cleaned = len(boost)
	while cleaned != 0:
		q, a, w = boost.pop()
		pp.pprint(q)
		print()
		cont = input('press `c` to continue and press `s` to see solution >')
		if cont =='c':
			cleaned -= 1
		if cont == 's':
			boost.append((q,a,w))
			pp.pprint(a)
		if cont != 'c' and cont !='s':
			break


	print('Awesome! This round of training is complete!')


if __name__ == "__main__":
	train(14,'Wayfair')