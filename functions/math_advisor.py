def scoreToLevel(score):
    if score > 80:
        level = 5
    elif score > 60:
        level = 4
    elif score > 40:
        level = 3
    elif score > 20:
        level = 2
    else:
        level = 1

def listOfCourses(level, major):
    if level == 1:
        return ['MATH-000']
    elif level == 2:
        return ['MATH-104', 'MATH-000']
    elif level == 3:
        if major in ['MATH', 'CMPSC', 'PHY']
            return ['MATH-121', 'MATH-104', 'MATH-000']
        if major in ['ACCT', 'FIN']
            return ['MATH-134', 'MATH-121', 'MATH-104', 'MATH-000']
        return 
