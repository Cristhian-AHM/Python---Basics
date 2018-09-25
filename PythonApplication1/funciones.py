#En Python las funciones se declaran mediante la palbra clave def y su sintaxi es:
#def nombre_de_la_función(parametro1, parametro2,...,parametroN):

def pow(parametro1, parametro2):
    print(parametro1**parametro2)

#Asignar un valor predefinido a un paramtro
def pow2(parametro1, parametro2=2):
    print(parametro1**parametro2)

pow(5,2)
pow(parametro2=2, parametro1=5)

pow2(3)
pow2(3,2)

#Parametros indefinidos
def sumarLista(*parametros):
    suma = 0
    for numero in parametros:
        suma += numero
    print("La suma es:",suma)

sumarLista(1,2,3,4,5)

#Paso por valor y por referencia

def persistenciaParametros(parametro1, parametro2):
        parametro1 += 5
        parametro2[1] = 6
        print(parametro1)
        print(parametro2)

numeros = [1,2,3,4]
valorInmutable = 2

persistenciaParametros(valorInmutable, numeros)
print(numeros)
print(valorInmutable)

#Retorno de valores 
#Para regrersar un valor se usa la palabra reservada return

def suma(parametro1, parametro2):
    return parametro1 + parametro2

def potencia(parametro1, parametro2):
    return parametro1**parametro2

def sumaPotencia(parametro1, parametro2):
    return parametro1 + parametro2, parametro1 ** parametro2

resultado1 = suma(2,3)
print(resultado1)

resultado2 = potencia(2,3)
print(resultado2)

resultado3 = sumaPotencia(2,3)
print(resultado3)

