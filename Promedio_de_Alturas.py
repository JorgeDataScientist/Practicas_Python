'''
Vas a escribir un programa que calcule la estatura promedio de los estudiantes a partir de una Lista de estaturas.
Importante No debe usar las funciones sum() o len() en su respuesta.
Debe intentar replicar su funcionalidad utilizando lo que ha aprendido sobre los bucles for.
'''
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])


'''
Importante No debe usar las funciones sum() o len() en su respuesta.
Debe intentar replicar su funcionalidad utilizando lo que ha aprendido sobre los bucles for.
'''
total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(f"number of students = {number_of_students}")

average_height = round(total_height / number_of_students)
print(average_height)

# Aca la lista: 156 178 165 171 187