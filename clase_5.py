#Sesion 5: Funciones en programación.
# En esta sesión, aprenderemos:

# Qué es una función en programación y por qué es útil.
# Cómo se estructuran las funciones en un lenguaje de programación.
# Cuáles son los beneficios de utilizar funciones en nuestros programas.
# Cómo funcionan los parámetros y el retorno de valores (sin aplicarlo en código todavía).
# Ejemplos y ejercicios prácticos para comprender la lógica detrás del uso de funciones.

#que es una funcion en programación?

#una funcion es un bloque de codigo que tiene un proposito especifico dentro de un programa. Se usa para dividir el codigo en partes mas pequeñas y reusables, lo que hace que los proframas sean mucho mas organizados y faciles de entender.


#Como así?

# Imagina que quieres preparar una pizza en casa. En lugar de hacer todo el proceso cada vez que la cocinas, podrías tener pasos organizados:

# Preparar la masa.
# Agregar los ingredientes.
# Hornear la pizza.
# Servir.

# Cada uno de estos pasos es una función dentro del proceso general de hacer una pizza. Cuando quieras hacer otra pizza, simplemente sigues los mismos pasos en orden, sin necesidad de inventar un nuevo proceso desde cero.

# En programación, ocurre lo mismo: en lugar de escribir el mismo código varias veces, utilizamos funciones para organizarlo y reutilizarlo.


#Como funciona...

#Para entender como funciona una funcion, debemos penar en 3 aspectos clave...

#1 Defincion de la funcion: Se establece el bloque de codigo con un nombre que lo identifica

#2 Invocación de la funcion: Se ejecuta la funcion cundo es necesario dentro del programa.

arreglo = []
numero = len(arreglo)

# Retorno de valores: una funcion puede devolver un resultado para ser usado en alguna parte del codigo (return).

#Eso pa que?... por que o que?

#Reusar codigo:
#DRY : don't repeat yourself.
#KISS : Keep it simple, stupid.
# en lugar de escribir lo mismo varias veces, escribo una sola vez en una funcion y la llamo cuando lo necesite. 

#Organizacion y modular.
#dividir un programa en funciones hce que el codigo sea mas estructurdo y facil de entender... 

#Faciliad del mantenimiento.
#si hay errores en la ejecucion, se pueden corregir en una sola funcion, en lugar de buscar en varias partes del programa.

#Escalabilidad
#construir programas mas grandes de una manera mas ordenada y logica.

#Facilitan el trabajo en equipo:
# en proyectos los devs pueden trbajas en funciones separadas sin afectar otras partes del codigo.

#Componentes de una funcion.

#Nombre de la funcion:
#identificador unico que permite llamarla cuando sea necesario.

#parmetros(opcional):
#datos que reciben una funcion para trabajar con ellos.

#Cuerpo de la funcion:
#Bloque de codigo que define el comportamiento de la funcion.

#Valor de retorno(opcional):
#resultdo que a funcion va a devolver al flujo principal.

#diferencia entre una funcion y un bloque de codigo.

print("hola, bienvenido a nuestro programa")
nombre = input("ingrese su nombre: ")
print(f"hola {nombre}, espero que tengo que tengas un buen dia!")

print("hola, bienvenido a nuestro programa")
nombre = input("ingrese su nombre: ")
print(f"hola {nombre}, espero que tengo que tengas un buen dia!")

# //////////////////////////////////////////////////
#Ejemplo en pseudocodigo de como calcular el area de un rectangulo.

#1 pedir la base y la altura.
#2 multiplicar base * altura
#3 mostrar el resutado.

#parmetros y retornos:
#las funciones reciben parametros que devuelven resultados

#parametro es: el insumo con el que trabaja la funcion

#retorno: es el resultado de procesar los parametros.

#1. ingresar "late" y "grande" como parametros a la maquina
#2 la maquina prepra el cafe.
#3 la maquina devuelve el cafe listo.









