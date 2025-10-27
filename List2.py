students = ["Bob", "Mary", "Lily"]
grades = [8, 9, 10]

max_grade = grades[0]
max = 0

for i in range(len(grades)):
    if grades[i] > max_grade:
        max_grade = grades[i]
        max = i

print("The student with the largest grades is: ",
      students[max], "with grade ", max_grade)
