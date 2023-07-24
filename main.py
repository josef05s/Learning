def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def dividir(a, b):
    if b != 0:
        return a / b
    

def multiplicar(a, b):
    return a * b

def main():
    num1 = float(input("Introduce el primer numero: "))
    num2 = float(input("Introduce el segundo numero: "))

    
    print("1. Sumar")
    print("2. Restar")
    print("3. Dividir")
    print("4. Multiplicar")

    seleccion = input("Tu selección (1-4): ")

    if seleccion == '1':
        resultado = sumar(num1, num2)
        print(f"El resultado de la suma es: {resultado}")
    elif seleccion == '2':
        resultado = restar(num1, num2)

        print(f"El resultado de la resta es: {resultado}")
    elif seleccion == '3':
        resultado = dividir(num1, num2)
        print(f"El resultado de la división es: {resultado}")
    elif seleccion == '4':
        resultado = multiplicar(num1, num2)
        print(f"El resultado de la multiplicación es: {resultado}")
    else:
        print("Selección invalida elige una opción válida (1-4).")

if __name__ == "__main__":
    main()        