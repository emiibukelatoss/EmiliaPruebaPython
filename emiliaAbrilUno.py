notas = []

print("Registro de notas del estudiante")
print("Ingresa las notas (entre 0 y 10). Escribí 'fin' para terminar.")

while True:
    entrada = input("Ingresa una nota o 'fin' para terminar: ")

    if entrada.lower() == 'fin':
        break

    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Error: la nota debe estar entre 0 y 10.")
    except ValueError:
        print("Error: Ingresa un número válido o 'fin' para terminar.")

if len(notas) == 0:
    print("No se ingresaron notas.")
else:
    promedio = sum(notas) / len(notas)
    print("El promedio de las notas es:", round(promedio, 2))

    if promedio >= 7:
        print("El estudiante aprobó.")
    else:
        print("El estudiante no aprobó.")