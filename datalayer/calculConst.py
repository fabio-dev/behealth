# replace all this methods by a datalayer
# calcul source : https://en.wikipedia.org/wiki/Institute_of_Medicine_Equation

def getConsts(sex, age):
	if sex=='man':
		if age >= 18:
			return [662, 9.53, 15.91, 539.6]
		elif age >= 3:
			return [88.5, 61.9, 26.7, 903]
	elif sex=='woman':
		if age>=18:
			return [354, 6.91, 9.36, 726]
		elif age >= 3:
			return [135.3, 30.8, 10, 934]
	return -1

def getEERActivityIndice(age, bmi, sex, activity):
	indices = [[1.00, 1.00, 1.00, 1.00, 1.00, 1.00],
				[1.13, 1.16, 1.12, 1.18, 1.11, 1.12],
				[1.26, 1.31, 1.24, 1.35, 1.25, 1.27],
				[1.42, 1.56, 1.45, 1.60, 1.48, 1.45]]
	xVal = int(activity)
	yVal = 0 if sex=='man' else 1
	if age>=18:
		yVal += 4
	elif bmi>25:
		yVal += 2
	return indices[xVal][yVal]
