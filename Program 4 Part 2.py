all_grades = []
passing_grades = []
grade_sum = 0
grade = int(input("Please enter grade: "))

while grade != -1:
    if 60 <= grade <= 100:
        passing_grades.append(grade)
        all_grades.append(grade)
        grade_sum += grade
    elif 0 <= grade < 60:
        all_grades.append(grade)
        grade_sum += grade
    else:
        print("Invalid grade entered.")
        
    if len(all_grades) == 0:
        pass
    else:
        average = float(grade_sum / len(all_grades))

    if len(all_grades) == 1:
        print(f'You have entered {len(all_grades)} valid grade with a score of {grade_sum}.\n')
    elif len(all_grades) == 0:
        print("You have not entered any valid grades.\n")
    else:
        print(f'You have entered {len(all_grades)} valid grades with an average score of {average:.4g}.\n')

    grade = int(input("Please enter another grade: (Enter -1 to stop entering grades.) "))

pass_pct = float((len(passing_grades) / len(all_grades)) * 100)

print()
print(f'The total number of valid grades entered is {len(all_grades)} with an average score of {average:.4g}.')
print(f'The total number of passing grades entered is {len(passing_grades)} which is {pass_pct:.4g}% of the total.')
