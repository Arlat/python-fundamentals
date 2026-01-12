def analizar_valor(valor):
    if valor == 0:
        return 1
    
    if valor < 0:
        valor = valor * -1

    contador = 0
    
    while valor > 0:
        valor = valor // 10
        contador = contador + 1
    return contador

while True:
    try:
        valor = int(input("Ingrese el valor a analizar: "))
        break
    except ValueError:
        print("Error: debe ingresar un número entero.")

digitos = analizar_valor(valor)

print(f"El valor ingresado tiene {digitos} digitos")


