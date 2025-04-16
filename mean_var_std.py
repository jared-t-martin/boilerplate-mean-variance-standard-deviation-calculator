import numpy as np
np.set_printoptions(legacy='1.13')

def calculate(list):
    calculations = {}
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    fixed = np.array(list).reshape(3,3)
    
    meanT = np.mean(fixed).tolist()
    meanR = np.mean(fixed, 0).tolist()
    meanC = np.mean(fixed, 1).tolist()
    calculations.update({'mean': [meanR,meanC,meanT]})

    varT = np.var(fixed)
    varR = np.var(fixed, 0).tolist()
    varC = np.var(fixed, 1).tolist()
    calculations.update({'variance': [varR,varC,varT]})

    stdT = np.std(fixed)
    stdR = np.std(fixed, 0).tolist()
    stdC = np.std(fixed, 1).tolist()
    calculations.update({'standard deviation': [stdR,stdC,stdT]})

    maxT = np.max(fixed)
    maxR = np.max(fixed, 0).tolist()
    maxC = np.max(fixed, 1).tolist()
    calculations.update({'max': [maxR,maxC,maxT]})

    minT = np.min(fixed)
    minR = np.min(fixed, 0).tolist()
    minC = np.min(fixed, 1).tolist()
    calculations.update({'min': [minR,minC,minT]})

    sumT = np.sum(fixed)
    sumR = np.sum(fixed, 0).tolist()
    sumC = np.sum(fixed, 1).tolist()
    calculations.update({'sum': [sumR,sumC,sumT]})

    return calculations