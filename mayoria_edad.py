#sin funciones.

edad = int(input("ingrese su edad: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Te redirijo a google.")
    
print("Flujo con funcion.")

#con funciones
def verificar_edad(edad):
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Te redirijo a google.")
        
edad_usuario = int(input("ingrese su edad: "))
verificar_edad(edad_usuario)