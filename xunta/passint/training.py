import pandas as pd
import pprint
import random

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

if __name__ == "__main__":
	df = pd.read_csv('C:/JospehShen/XunTa/data/train.csv', index_col=0)
	questions = list(df['Question'])
	answers = list(df['Answer'])
	qapair = list(zip(questions,answers))
	if len(qapair) > 7:
		qapair = random.sample(qapair, 7)
	pp = pprint.PrettyPrinter(indent=2)


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

	print(color.BOLD + color.GREEN + 'Your score is {}'.format(round(score/len(qapair)*100,0)) + color.END)
	print()
	print(color.BOLD + color.RED + 'Now start debugging problems you failed to answer...' + color.END)


	cleaned = sum([i[2] for i in boost])
	while cleaned != 0:
		q, a, w = random.sample(boost,1).pop()
		pp.pprint(q)
		print()
		cont = input('press `c` to continue and press `s` to see solution >')
		if cont =='c':
			cleaned -= 1
		if cont == 's':
			pp.pprint(a)
		if cont != 'c' and cont !='s':
			break


	print(color.GREEN + 'Awesome! This round of training is complete!')