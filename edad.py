def calculator(edad):
    if edad >= 18:
        msg = "mayor de edad"
    else:
        msg = "menor de edad"
    return msg

def main():
    edad = int(input("Ingrese su edad: "))
    if edad <= 0:
        print("Error: La edad debe ser un número positivo mayor que cero.")
    else:
        msg = calculator(edad)
        print("Usted es", msg)

if __name__ == "__main__":
    main()