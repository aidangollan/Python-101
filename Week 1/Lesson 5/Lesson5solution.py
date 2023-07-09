def main_code(grades):
    gradeDict = {90: 'A', 80: 'B', 70: 'C', 60: 'D'}
    nameOut = {}
    gradesSeen = set()
    curGrade = 0
    maxScore = 0
    for key,value in grades.items():
        for i in value:
            maxScore = max(i, maxScore)
            curGrade += i
        nameOut[key] = curGrade / len(value)
        curGrade = 0
    for key,val in nameOut.items():
        letterGrade = assign_grade(val, gradeDict)
        nameOut[key] = letterGrade
        gradesSeen.add(letterGrade)
    
    for key,val in nameOut.items():
        print("The letter grade for " + key + " is " + val)
    
    best_student = None
    worst_student = None
    for student, grade in nameOut.items():
        if best_student is None or grade < nameOut[best_student]:
            best_student = student
        if worst_student is None or grade > nameOut[worst_student]:
            worst_student = student
    print("The best student is " + best_student + " with a grade of " + nameOut[best_student])
    print("The worst student is " + worst_student + " with a grade of " + nameOut[worst_student])
    print("The scores that showed up are")
    for i in sorted(list(gradesSeen)):
        print(i)
    return maxScore
    
    
def assign_grade(score, gradeDict):
    for key in sorted(gradeDict.keys(), reverse=True):
        if score >= key:
            return gradeDict[key]
    return 'F'

if __name__ == "__main__":
    print(main_code())