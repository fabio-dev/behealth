'''
Created on 15th August 2016
@author: Daniel Durrenberger
'''

def calculateBMR(sex, mass, size, age):
    '''
    sex = 0 for women, 1 for men
    mass in kg
    size in m
    age in years
    BMR in kcal/d (1000 kcal = 4,186 Mj)
    Black and al. (1996) formula
    '''
    if age>18:
        if sex==0:
            BMR = 230 * mass**(0.48) * size**(0.50) * age**(-0.13)
        else:
            BMR = 259 * mass**(0.48) * size**(0.50) * age**(-0.13)
    elif age<1:
        BMR = 92 * mass
    return BMR

def activityFactor(sex, activityLevel, weeklySports):
    '''
    sex = 0 for women, 1 for men
    activityLevel is
        - 0 lit ou fauteuil
        - 1 travail assis ; déplacements et activités de loisirs faibles
        - 2 travail assis ; déplacements faibles et activités de loisirs
            peu fatigantes
        - 3 travail debout
        - 4 travail ou activités physiques de loisirs intenses
    weeklySports is the number of
        - activités physiques intenses de sport ou de loisirs
            (de 30 à 60 minutes, quatre ou cinq fois par semaine).
    '''
    woman = [1.2, 1.4, 1.6, 1.8, 2.2]
    man = [1.3, 1.5, 1.7, 1.9, 2.4]
    if sex==0:
        factor = woman[activityLevel] + 0.3*weeklySports
    else:
        factor = man[activityLevel] + 0.3*weeklySports
    return factor

def calculateBMI(mass, size):
    return mass / size**2

def bmiFactor(bmi):
    '''
    il faut diminuer de 1% la DEJ calculée par point d’IMC au-dessus de 22 
    et l’augmenter symétriquement au-dessous de 22
    '''
    return 1 + (22-bmi)/100.

def calculateDEE(sex, mass, size, age, activityLevel, weeklySports):
    bmr = calculateBMR(sex, mass, size, age)
    actFactor = activityFactor(sex, activityLevel, weeklySports)
    bmi = calculateBMI(mass, size)
    bmiFactor = bmiFactor(bmi)
    return bmr * actFactor * bmiFactor
