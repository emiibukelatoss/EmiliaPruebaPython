# Inicializamos la lista para guardar las notas
notas = []

print("Registro de notas del estudiante.")
print("Ingresá las notas (entre 0 y 10). Escribí 'fin' para terminar.\n")

while True:
    entrada = input("Ingresá una nota o 'fin' para terminar: ")

    if entrada.lower() == 'fin':
        break

    