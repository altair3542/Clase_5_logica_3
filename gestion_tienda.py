productos = []
precios = []

for i in range(3):
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input(f"Ingrese el precio de {nombre}: "))
    productos.append(nombre)
    precios.append(precio)

total = 0
for precio in precios:
    total += precio

if total > 100:
    total = total * 0.90  

print("\nResumen de compra:")
for i in range(len(productos)):
    print(f"{productos[i]} - ${precios[i]:.2f}")

print(f"Total a pagar: ${total:.2f}")
print("funciones")

def registrar_productos():
    productos = []
    precios = []
    for i in range(3):
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input(f"Ingrese el precio de {nombre}: "))
        productos.append(nombre)
        precios.append(precio)
    return productos, precios

def calcular_total(precios):
    total = sum(precios)
    if total > 100:
        total *= 0.90  
    return total

def mostrar_resumen(productos, precios, total):
    print("\nResumen de compra:")
    for i in range(len(productos)):
        print(f"{productos[i]} - ${precios[i]:.2f}")
    print(f"Total a pagar: ${total:.2f}")

# Flujo del programa
productos, precios = registrar_productos()
total = calcular_total(precios)
mostrar_resumen(productos, precios, total)

