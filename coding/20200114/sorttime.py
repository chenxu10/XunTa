import datetime

def sorttime(timelist):
	return sorted(timelist, key=lambda x:datetime.datetime.strptime(x, '%d-%b-%Y'), reverse=True)

if __name__ == "__main__":
	print(sorttime(["23-Jun-2015","2-Dec-2013","2-Jun-1999"]))