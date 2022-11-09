# Crea un programa usando matemáticas y f-Strings que nos diga cuántos días,
# semanas, meses nos quedan si vivimos hasta los 90 años.
# Tomará su edad actual como entrada y salida de un mensaje con nuestro tiempo restante en este formato:#
# Le quedan x días, y semanas y z meses.#
# Donde x, y y z se reemplazan con los números calculados reales.
# Hay 365 días en un año, 52 semanas en un año y 12 meses en un año.
# -------------------------------------------
age = input("What is your current age? ")
age = int(age)

# Edad Limite
age = 90 - age

# Datos de mi Edad
meses = age * 12
semanas = age * 52
dias = age * 365



# Resultado
print("You have " + str(dias) + " days, " + str(semanas) + " weeks, " + "and " + str(meses) + " months left.")