# Solicitar al usuario que ingrese dos números
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Definir la función suma
def suma(num1, num2):
    return num1 + num2 # No need to assign the result to a variable inside the function

# Sumar los dos números usando la función suma
resultado = suma(num1, num2) # Store the result in a variable

# Imprimir el resultado
print("La suma de", num1, "y", num2, "es:", resultado)

