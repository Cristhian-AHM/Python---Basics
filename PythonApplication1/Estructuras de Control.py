#Estructura If
c = 37

if c > 0:
    print ("El número es positivo\n")
    print ("Que tenga un lindo día\n")

#Continua el programa

#Algo muy importante a tomar en cuenta con el uso de Python es la identación a la hora de usar estructuras control
#En otros lenguajes se tienen palabras reservadas para la utilización de estructuras de control por ejemplo (Begin, End ó {})
#En Python solo se dispone de la identación para este proposito.


#Sentencia If - Elif - Else

c = -10 

if c > 0:
    print("El número es positivo\n")
elif c == 0:
    print("El número es cero\n")
else:
    print("El número es negativo\n")

#Se pueden poner tantos elif como sean necesarios.

#Existe una forma de hacer más compacta la sentencia If y es mediante se tratan de bloques que se escriben de la siguiente manera:
# Acción1 if Condición else Acción2

print("El número es positivo") if c > 0 else print("El número es negativo")