import numpy as np
datatype = [('name', 'S15'), ('class', int), ('height', float)]
studentsdetails = [('Ishaan PM', 10, 175,), ('Atharv A Dua', 8, 177), ('John Vimal', 10, 169)]
students = np.array(studentsdetails, dtype=datatype)
print("The original array is: ")
print(students)
print("The array in ascending order is: ")
print(np.sort(students, order ='height'))
print("The array in descending order is: ")
print(np.flip(np.sort(students, order ='height')))