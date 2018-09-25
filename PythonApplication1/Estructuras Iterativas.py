#Las estructuras Iterativas nos permiten repetir un segmento de código indefinidamente.

#Bucles for..in

#La estructura es la siguiente: FOR elemento IN secuencia: y a continuación el bloque de código indentado propiamente.

#Ejemplo de un bucle for..in para recorrer un vector de datos


vector = ["Uno", "Dos", "Tres"]

for palabra in vector:
    print(palabra)
    pass
print("Done!")

#Bucles While

#La estructura del bucle While es la siguiente: while condición:

#Ejemplo del bulce While

pares = 2

while pares <= 20:
    print(pares)
    pares += 2
    pass
print("Done! (Again)")
