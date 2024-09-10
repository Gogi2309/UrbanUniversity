grades=[[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students={'johnny','Bilbo','Steven','Khendrik','Aaron'}
print(grades[0])
print(sum(grades[0]))
print(len(grades[0]))
avereg_marks = [sum(grades[0])/len(grades[0]),
                sum(grades[1])/len(grades[1]),
                sum(grades[2])/len(grades[2]),
                sum(grades[3])/len(grades[3]),
                sum(grades[4])/len(grades[4])]
print(avereg_marks)
students = sorted(students)
print(students)
result = dict(zip(students,avereg_marks))
print(result)