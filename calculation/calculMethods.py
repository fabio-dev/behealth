from datalayer import calculConst

def calculBMI(weight, size):
    size = size / 100
    return weight / (size * size)
    
def calculEER(age, weight, size, sex, activity):
    consts = calculConst.getConsts(sex, age)
    bmi = calculBMI(weight, size)
    indice = calculConst.getEERActivityIndice(age, bmi, sex, activity)
    sizeInMeter = size / 100
    
    return (consts[0] - consts[1] * age) + indice * (consts[2] * weight) + (consts[3] * sizeInMeter)