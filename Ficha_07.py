'''
nombres = ('Juan', 'Pedro', 'Maria')

for nom in nombres:
    print (nom)


################## CON WHILE ###################

secuencia = 'Hola'
i = 0

while i < len(secuencia):
    print (secuencia[i])
    i +=1

################## CON FOR #####################

secuencia = 'Hola'

for car in secuencia:
    print(car)


#Sea n un número entero mayor o igual a 0. El factorial del número n (denotado
#algebraicamente como n!) es el producto de todos los números enteros en el intervalo [1, n] si n > 0.
#En caso que n = 0, entonces se define 0! = 1. Más formalmente:
#n! =        1 si n = 0
#            n * (n-1) * (n-2) * … * 3 * 2 * 1 si n >
#A modo de ejemplo:
#5! = 5 * 4 *3 *2 *1 = 120
#7! = 7 * 6 * 5 * 4 *3 *2 *1 = 5040
#Se pide desarrollar un programa en Python que cargue por teclado un número n y calcule y muestre
#su factorial.

n = int(input('ingrese un numero: '))
factorial = 1

for i in range(1, n+1):
    factorial *= i

print('El factorial de', n,'Es', factorial)


#Determinar el mayor valor de una sucesión de valores que se cargan por teclado.
#Asuma en primera instancia que la cantidad n de números a procesar se conoce de antemano. Y
#luego de resolverlo con esa suposición, replantee su solución asumiendo que la cantidad n de
#números se desconoce y que la carga de datos terminará cuando se ingrese un 0.

n = int(input('Cantidad de numeros a procesar: '))

num = int(input('Ingrese el primer numero: '))

may = num

for i in range(2, n+1):
    num = int(input('Siguiente numero: '))
    if num > may:
        may = num

print('El mayor es:', may)


#Determinar el mayor de una secuencia de valores que ingresan de a uno. Se desconoce
#cuantos valores serán procesados, pero se indicará el final de la secuencia cargando el
#número cero.

may = None
b = False
num = int(input('Ingrese un numero (con 0 finaliza): '))
while num != 0:
    if b == False:
        may = num
        b = True
    else:
        if num > may:
            may = num

    num = int(input('Ingrese otro (con 0 finaliza): '))

print('El mayor es:', may)

#Un pequeño comercio de papelería cuenta con dos vendedores. Cada vendedor está
#codificado con los números 1 y 2. Considere que la carga de datos se realizará desde teclado, de
#forma que una entrada consta de 3 variables que representan una venta realizada: por cada venta,
#cargar el código del vendedor (1 o 2) que hizo la venta, cantidad de artículos vendida en esa
#operación, e importe de la venta. El fin de datos se indicará con código de vendedor igual a 0 (cero).
#El dueño del comercio desea cierta información estadística y para ello solicita un programa que
#obtenga lo siguiente:
#a.) La cantidad de productos vendida por cada vendedor (dos totales).
#b.) El importe total vendido por cada vendedor (otros dos totales).
#c.) El importe de la menor venta realizada por el vendedor 2.
#d.) El importe promedio de ventas por vendedor (importe total acumulado / 2).

# pasó la primera venta del vendedor 2?
aviso = False
# si no se cargan ventas del vendedor 2, menor_importe queda en None...
menor_importe = None
# acumuladores de cantidades...
c1 = c2 = 0
# acumuladores de importes...
i1 = i2 = 0
print('Ventas de un Comercio... ingrese los datos de cada venta...')
# ingresar (y validar) el primer codigo...
codigo = -1
while codigo < 0 or codigo > 2:
 codigo = int(input('Codigo de vendedor (1 o 2) (0 para cortar): '))
 if codigo > 2 or codigo < 0:
 print('Error... se pidio 1 o 2 o 0 para cortar...')
while codigo != 0:
 cantidad = int(input('Cantidad vendida: '))
 importe = float(input('Importe: '))
 if codigo == 1:
 c1 += cantidad
 i1 += importe
 elif codigo == 2:
 c2 += cantidad
 i2 += importe
 # Aplicar mecanismo de cálculo del menor...
 if not aviso:
 aviso = True
 menor_importe = importe
 elif importe < menor_importe:
 menor_importe = importe
 # ingresar el siguiente codigo y volver al ciclo...
 codigo = -1
 while codigo < 0 or codigo > 2:
 codigo = int(input('Codigo de vendedor (1 o 2) (0 para cortar): '))
 if codigo > 2 or codigo < 0:
 print('Error... se pidio 1 o 2 o 0 para cortar...')
# Calcular el importe promedio...

promedio = (i1 + i2) / 2
print('Cantidad de productos vendida por el vendedor 1:', c1)
print('Cantidad de productos vendida por el vendedor 2:', c2)
print('Importe total facturado por el vendedor 1:', i1)
print('Importe total facturado por el vendedor 2:', i2)
print('Importe de la menor venta del vendedor 2:', menor_importe)
print('Importe promedio entre los dos vendedores:', promedio)



#Desarrollar un programa en Python que permita cargar por teclado un texto
#completo (analizar dos opciones: una es cargar todo el texto en una variable de tipo cadena
#de caracteres y recorrerla con un for iterador; y la otra es cargar cada caracter uno por uno a
#través de un while). Siempre se supone que el usuario cargará un punto para indicar el final
#del texto, y que cada palabra de ese texto está separada de las demás por un espacio en
#blanco. El programa debe:
#a. Determinar cuántas palabras se cargaron.
#b. Determinar cuántas palabras comenzaron con la letra "p".
#c. Determinar cuántas palabras contuvieron una o más veces la expresión "ta".


# contador total de palabras
ctp = 0
# contador de letras en una palabra
cl = 0
# contador de palabras que empiezan con p
cpp = 0
car = None
while car != '.':
 # cargar y procesar el caracter ingresado en car
 car = input('Letra (con "." termina): ')
 cl += 1

 # final de palabra?
 if car == ' ' or car == '.':
 # ha terminado una palabra...
 # ...contarla solo si hubo al menos una letra...
 if cl > 1:
 ctp += 1
 # ...reiniciar contador de letras (por próxima palabra)...
 cl = 0

 else:
 # car es una letra... la palabra sigue...
 # ...contar la palabra si comienza con "p"...
 if cl == 1 and car == 'p':
 cpp += 1
print('Cantidad de palabras:', ctp)
print('Cantidad de palabras que empiezan con "p":', cpp)




for i in range(1):
  n1 = int(input('Ingrese el tp 1: '))
  n2 = int(input('Ingrese el tp 2: '))
  n3 = int(input('Ingrese el tp 3: '))

  promedio = (n1+n2+n3) / 3

  if promedio < 4:
   estado = 'Insuficiente'

  if 4 < promedio <7:
   estado = 'Aprobado'

  else:
   estado = ('Promocionado')

print('El estado del alumno es:',estado)


#1. Ciclistas
#La final de una carrera de ciclistas tiene n competidores (n se ingresa por teclado).

#Desarrollar un programa que permita cargar, por cada competidor, nombre y tiempo de carrera.
#Luego se pide:

#a) Determinar y mostrar el nombre del ganador de la carrera.

#b) Ingresar por teclado el tiempo record registrado para dicha carrera.
#Determinar si el tiempo del ganador es menor al tiempo record, mostrar un mensaje.

#c) Calcular y mostrar el tiempo promedio entre todos los ciclistas.

nombre_ganador = 'n'
tiempo_ganador = 0
es_menor = False

cant_competidores = int(input('Ingrese la cantidad de competidores: '))
tiempo_record = input('Ingrese el tiempo record de la carrera: ')

for i in range(1, cant_competidores +1):
    nombre = input('Ingrese el nombre del competidor: ')
    tiempo = float(input('Ingrese el tiempo de la carrera del competidor: '))



if tiempo_ganador < tiempo_record:
        es_menor = True

print(tiempo_ganador)


#SOLUCION DE LA CATEDRA

suma_tiempos = 0
menor_tiempo = None
menor_nombre = None

es_el_primero = True

n = int(input("Ingrese la cantidad de corredores"))

for i in range(n): # La variable i toma los valores entre 0 y n-1
    # Este ciclo va a dar una vuelta por cada ciclista

    nombre = input("Ingrese el nombre del ciclista: ")
    tiempo = int(input("Ingrese el tiempo: "))

    # Búsqueda del menor tiempo
    # Tenemos que garantizar que menor_tiempo empiece igual al primer valor

    # Alternativas válidas
    # if i == 0 or tiempo < menor_tiempo:
    # if es_el_primero or tiempo < menor_tiempo:
    # if menor is None or tiempo < menor_tiempo:
    if es_el_primero or tiempo < menor_tiempo:
        menor_tiempo = tiempo
        menor_nombre = nombre

    # Promedio: acumulador / contador
    suma_tiempos += tiempo
    es_el_primero = False

promedio_tiempos = suma_tiempos / n

# Esta variable podria ser ingresada al principio
tiempo_record = int(input("Ingrese el tiempo record"))

if menor_tiempo < tiempo_record:
    print("El ganador batió el record!!!!")

print("El nombre del ciclista que hizo el menor tiempo es: ", menor_nombre)
print("El promedio de tiempos es:", promedio_tiempos)
suma_tiempos = 0
menor_tiempo = None
menor_nombre = None

es_el_primero = True

n = int(input("Ingrese la cantidad de corredores"))

for i in range(n): # La variable i toma los valores entre 0 y n-1
    # Este ciclo va a dar una vuelta por cada ciclista

    nombre = input("Ingrese el nombre del ciclista: ")
    tiempo = int(input("Ingrese el tiempo: "))

    # Búsqueda del menor tiempo
    # Tenemos que garantizar que menor_tiempo empiece igual al primer valor

    # Alternativas válidas
    # if i == 0 or tiempo < menor_tiempo:
    # if es_el_primero or tiempo < menor_tiempo:
    # if menor is None or tiempo < menor_tiempo:
    if es_el_primero or tiempo < menor_tiempo:
        menor_tiempo = tiempo
        menor_nombre = nombre

    # Promedio: acumulador / contador
    suma_tiempos += tiempo
    es_el_primero = False

promedio_tiempos = suma_tiempos / n

# Esta variable podria ser ingresada al principio
tiempo_record = int(input("Ingrese el tiempo record"))

if menor_tiempo < tiempo_record:
    print("El ganador batió el record!!!!")

print("El nombre del ciclista que hizo el menor tiempo es: ", menor_nombre)
print("El promedio de tiempos es:", promedio_tiempos)
suma_tiempos = 0
menor_tiempo = None
menor_nombre = None

es_el_primero = True

n = int(input("Ingrese la cantidad de corredores"))

for i in range(n): # La variable i toma los valores entre 0 y n-1
    # Este ciclo va a dar una vuelta por cada ciclista

    nombre = input("Ingrese el nombre del ciclista: ")
    tiempo = int(input("Ingrese el tiempo: "))

    # Búsqueda del menor tiempo
    # Tenemos que garantizar que menor_tiempo empiece igual al primer valor

    # Alternativas válidas
    # if i == 0 or tiempo < menor_tiempo:
    # if es_el_primero or tiempo < menor_tiempo:
    # if menor is None or tiempo < menor_tiempo:
    if es_el_primero or tiempo < menor_tiempo:
        menor_tiempo = tiempo
        menor_nombre = nombre

    # Promedio: acumulador / contador
    suma_tiempos += tiempo
    es_el_primero = False

promedio_tiempos = suma_tiempos / n

# Esta variable podria ser ingresada al principio
tiempo_record = int(input("Ingrese el tiempo record"))

if menor_tiempo < tiempo_record:
    print("El ganador batió el record!!!!")

print("El nombre del ciclista que hizo el menor tiempo es: ", menor_nombre)
print("El promedio de tiempos es:", promedio_tiempos)

#SOLUCION DOS

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


print('CARRERA DE CICLISTAS')
print('-' * 40)
cont = acum = 0
ganador = None

n = int(input('Ingrese la cantidad de ciclistas que participan de la carrera: '))

for i in range(n):
    print('Ciclista',i)
    nombre = input('Ingrese nombre: ')
    tiempo = int(input('Ingrese tiempo: '))
    if ganador is None or tiempo < ganador[1]:
        ganador = nombre, tiempo
    cont += 1
    acum += tiempo

print('-' * 40)
if n > 0:
    record = int(input('Ingrese record actual: '))
    print('El ganador es', ganador[0])
    if ganador[1] < record:
        print('El ganador supero el record!')
        if cont > 0:
            promedio = round(acum / cont,2)
        else:
            promedio = 0
        print('Tiempo promedio general', promedio)
else:
    print('No se ingresaron datos')


#2. Secuencia de impares
#Cargar por teclado dos números, e imprimir los números impares que se encuentran comprendidos entre ellos,
#en forma ascendente y descendente.

numeros = int(input('Ingrese un numero: '))

for i in range(2):










#3. Sueldos y aguinaldo
#Ingresar por teclado los sueldos de un vendedor, correspondientes al primer semestre del año y luego:

#a) Calcular su aguinaldo, sabiendo que es la mitad del sueldo más alto del período.

#b) Determinar en qué mes recibió el sueldo más bajo del período.

#c) Informar el sueldo promedio del semestre.


sueldos_meses = 0
meses = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio')

for i in range(6):
    sueldo = float(input('Ingrese su sueldo de el mes' + str(meses) + ': '))
    sueldos_meses += sueldo
    sueldo_promedio = sueldos_meses / 6

sueldo_alto = max(sueldos_meses)

print(sueldo_alto)



#SOLUCION CATEDRA

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('SUELDOS Y AGUINALDO')
print('*' * 80)

#Datos y proceso
total = 0
for mes in range(1,7):
    sueldo = float(input("Ingrese sueldo mes " + str(mes) + ": "))
    if mes==1:
        may = sueldo
        men = sueldo,1
    else:
        if sueldo > may:
            may = sueldo
        if sueldo < men[0]:
            men = sueldo, mes
    total += sueldo

#Resultados
aguinaldo = may / 2
print ("\nEl aguinaldo es de $",aguinaldo)
print("El menor sueldo fue de $",men[0],"y lo obtuvo en el mes",men[1])
promedio = round(total/6,2)
print ("El sueldo promedio es de $",promedio)


__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('SUELDOS Y AGUINALDO')
print('*' * 80)

#Datos y proceso
total = 0
primero = True
semestre = ("Enero","Febrero","Marzo","Abril","Mayo","Junio")
for mes in semestre:
    sueldo = float(input("Ingrese sueldo de " + str(mes) + ": "))
    if primero==True:
        may = sueldo
        men = sueldo, mes
        primero = False
    else:
        if sueldo > may:
            may = sueldo
        if sueldo < men[0]:
            men = sueldo, mes
    total += sueldo

#Resultados
aguinaldo = may / 2
print ("\nEl aguinaldo es de $",aguinaldo)
print("El menor sueldo fue de $",men[0],"y lo obtuvo en el mes de",men[1])
promedio = round(total/len(semestre),2)
print ("El sueldo promedio es de $",promedio)





#4. Decimal a Hexadecimal
#Generar n numeros aleatorios entre el rango de 5000 y 450000,
#por cada uno de ellos mostrar y generar el numero hexadecimal


#SOLUCION CATEDRA

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random
n = int(input('Ingrese la cantidad de numeros a procesar: '))

for i in range(n):
    numero = random.randrange(5000, 450000)
    hexadecimal = ''
    #proceso de conversion hexadecimal
    valor = numero % 16
    siguiente = numero // 16
    digito = ''
    while valor > 0:
        if valor < 10:
            digito = str(valor)
        else:
            digito = chr(55 + valor)
        hexadecimal = digito + hexadecimal
        valor = siguiente % 16
        siguiente //= 16

    print('El numero ', numero, 'en hexadecimal es', hexadecimal)
'''



#5. Números Enteros
#Escribir un programa que permita leer la cantidad de números enteros ingresados por el usuario
#y calcular lo siguiente:

#a) El segundo menor

#b) El promedio de los números positivos.

#c) El mayor de los números negativos.

numeros_positivos = 0
num_pos_ing = 0
numeros_negativos = 0
menor = 0
segundo_menor = 0

n = int(input('Ingrese la cantidad de numeros que va a ingresar: '))

for i in range(n):
    numeros = int(input('Ingrese un numero: '))

    if i==0:
        menor = numeros
    elif i==1:
        if numeros < menor:
            segundo_menor = menor
            menor = numeros
        else:
            segundo_menor = numeros
    else:
        if numeros < menor:
            segundo_menor = menor
            menor = numeros
        elif numeros < segundo_menor:
            segundo_menor = numeros

    if numeros > 0:
        numeros_positivos += numeros
        num_pos_ing += 1
    else:
        if numeros_negativos == 0:
            numeros_negativos += numeros
        elif numeros_negativos < numeros:
            numeros_negativos += numeros

promedio_positivos = numeros_positivos / num_pos_ing

print('El segundo menor es', segundo_menor,
    '\nEl promedio de los numeros positivos es', promedio_positivos,
    '\nEl mayor negativo es', numeros_negativos  )

'''
#SOLUCION CATEDRA

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

n=int(input("Ingrese la cantidad de nros. a procesar: "))
contador_positivos=0
suma_positivos=0
mayor_negativos=0

for i in range(n):

    #Entrada
    print("Ingrese el número ", i+1)
    numero=int(input())

    #Subproblema 1: Búsqueda del segundo menor
    if i==0:
        menor=numero
    elif i==1:
        if numero<menor:
            segundoMenor=menor
            menor=numero
        else:
            segundoMenor=numero
    else:
        if numero<menor:
            segundoMenor=menor
            menor=numero
        elif numero<segundoMenor:
            segundoMenor=numero

    #Subproblema 2: El promedio de los numeros positivos
    if numero>=0:
        contador_positivos+=1
        suma_positivos+=numero

    #Subproblema 3: El mayor de los numeros negativos.
    else:
        if mayor_negativos==0:
            mayor_negativos=numero
        elif mayor_negativos<numero:
            mayor_negativos=numero

if contador_positivos!=0:
    promedio=suma_positivos/contador_positivos
else:
    promedio=0

#Salida
print("El segundo menor es:",segundoMenor)
print ("El promedio de numeros positivos es: ",promedio)
print ("El mayor de los numeros negativos es: ",mayor_negativos)


#6. Puntos en un plano
#Desarrollar un programa que permita ingresar las coordenadas de n puntos en el plano, e informe:

#a) En qué cuadrante se encuentra cada uno.

#b) Determinar cuántos puntos se encuentran en el primer o tercer cuadrante.

#c) Determinar cuál de todos los puntos cargados se encuentra a mayor distancia del origen de coordenadas.


#7. Números: Mayor y Menor
#Cargar por teclado n números enteros positivos, uno a uno.
#Se deberá establecer qué número es el mayor de los números pares y el menor de los números impares.

#Por ejemplo, en una secuencia de números: 8, 15, 9, 2, 27, 18, 0;
#el mayor de los pares sería el número 18 y el menor de los impares el número 9.

n = int(input('Ingrese un numero: '))







#8. Ejercicio Estadística de Guardería Náutica
#Un club náutico de la costa del lago San Roque necesita calcular estadísticas acerca de los barcos que tiene en la guardería.

#Se pretende un programa que cargue uno por uno los datos de cada barco. De ellos se sabe el nombre, el tipo (1 si es velero, 2 si es lancha) 
#y el monto que pagan por mes de guardería.

#El programa debe cargar datos de los barcos de acuerdo a una cantidad n que se carga al comienzo y una vez completada la carga informar:

#El total anual aportado por los veleros y el total anual aportado por las lanchas (2 totales).

#El nombre del velero que mayor cuota mensual paga de guardería y el valor de su cuota mensual.

#El valor promedio de cuota pagada por las embarcaciones de la guardería teniendo en cuenta todas las embarcaciones independientemente del tipo que tengan.

#El porcentaje que representa el monto mensual recaudado por los veleros sobre el total mensual recaudado y 
#el porcentaje que representa el monto mensual recaudado por las lanchas sobre el total mensual recaudado (2 porcentajes).


#9. Validación de cuenta
#Desarrollar un programa que permita validar la cuenta de un usuario que intenta ingresar al sistema.

#La cuenta debe ingresarse con formato nombre@dominio y el programa validará que cumpla con las siguientes reglas:

#•Tener un solo @ en una posición intermedia de la cadena (ni la primera ni la última letra)
#•No contener dos puntos seguidos (uno a continuación del otro)
#•No empezar ni terminar con un punto


#10. Dirección de Tránsito
#La Dirección de Tránsito de Córdoba necesita un programa que permita validar las patentes que se ingresan al sistema.

#El programa debe solicitar el ingreso de una patente (sin espacios intermedios) y luego:

#Informar si se trata de una patentes en formato antiguo (XXX999) o nuevo (XX999YY)
#Verificar que contenga letras y números de acuerdo a los esperado
'''
