from operaciones import sumar, restar, multiplicar

while True:
    print("\nMenú de Operaciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == '4':
        break
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))

    if opcion == '1':
        print("Resultado:", sumar(a, b))
    elif opcion == '2':
        print("Resultado:", restar(a, b))
    elif opcion == '3':
        print("Resultado:", multiplicar(a, b))
    else:
        print("Opción inválida.")
