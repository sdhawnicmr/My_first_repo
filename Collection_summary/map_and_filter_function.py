import random

marks = [random.randint(1,100) for mark in range(11)]
print(marks) #[4, 83, 47, 78, 15, 66, 26, 53, 78, 20, 22]

def grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80 and marks < 90:
        return 'B'
    elif marks >= 70 and marks < 80:
        return 'C'
    elif marks >= 60 and marks < 70:
        return 'D'
    elif marks >= 40 and marks < 60:
        return 'E'
    else:
        return 'F'

grades= map(grade,marks)
print("Exam score",marks)
print("Grade",next(grades))
print("Grade",list(grades))

#filter()

f_marks= [77,80,35,99,40]
def failing(score):
    return score < 40

result = filter(failing,marks)
print(list(result))