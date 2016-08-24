# -*- coding: utf-8 -*-
'''
Created on 15th August 2016
@author: Daniel Durrenberger
'''
def LBM(sex, mass, size):
    '''
    Lean Body Mass on Wikipedia
    sex = 0 for women, 1 for men
    mass in kg
    size in m
    '''
    if sex==0:
        lbm = (0.29569*mass)+(41.813*size)-43.2933
    else:
        lbm = (0.32810*mass)+(33.929*size)-29.5336
    return lbm

def TBM(sex, mass, size):
    '''
    Typical Body Mass
    http://www.hussmanfitness.org/bmrcalc.htm
    '''
    lbm = LBM(sex, mass, size)
    if sex==0:
        factor = 1.20
    else:
        factor = 1.15
    return factor * lbm

def BMR(sex, mass, size, age):
    '''
    Metabolisme de base
    Base Metabolic Rate
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

def activityFactor(sex, activityLevel=3, weeklySports=0):
    '''
    sex = 0 for women, 1 for men
    activityLevel is
        1 - resting
        2 - mainly sitting
        3 - sitting + few calm activities
        4 - standing work
        5 - sport
    weeklySports is how many times a week you practice
    '''
    woman = [1.2, 1.4, 1.6, 1.8, 2.2]
    man = [1.3, 1.5, 1.7, 1.9, 2.4]
    if sex==0:
        factor = woman[activityLevel] + 0.3*weeklySports
    else:
        factor = man[activityLevel] + 0.3*weeklySports
    return factor

def BMI(mass, size):
    '''
    Body Mass Index
    '''
    return mass / size**2

def bmiFactor(bmi):
    '''
    il faut diminuer la DEJ calculee de 1 pour cent par point d'IMC
    en-dessus de 22 et l'augmenter systematiquement en-dessous de 22
    '''
    return 1 + (22-bmi)/100.

def DEE(sex, mass, size, age, activityLevel=3, weeklySports=0):
    '''
    calculates Daily Energy Expenditure in kcal
    sex = 0 for women, 1 for men
    activityLevel is
        1 - resting
        2 - mainly sitting
        3 - sitting + few calm activities
        4 - standing work
        5 - sport
    weeklySports is how many times a week you practice
    '''
    bmr = calculateBMR(sex, mass, size, age)
    actFactor = activityFactor(sex, activityLevel, weeklySports)
    bmi = calculateBMI(mass, size)
    bmiFactor = bmiFactor(bmi)
    return bmr * actFactor * bmiFactor

def protein(mass, sex=1, age=30, pregnant=False, breastfeeding=False):
    '''
    calculates the appropriate amount of protein one needs daily in grams
    ANC = 0.83g/kg/j
    '''
    prot = 0.83*mass
    if age>70 or sex==1:
        prot = 1.*mass
    if pregnant:
        prot += 0.1*mass
    if breastfeeding:
        prot += 0.3*mass
    return prot
