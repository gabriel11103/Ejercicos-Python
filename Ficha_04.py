'''
#Cargar por teclado dos números enteros. Mostrarlos ordenados de menor a mayor.

a = int(input("Ingrese un numero: "))
b = int(input('Ingrese otro numero: '))

if a > b:
    may = a
    men = b
else:
    may = b
    men = a

print('Numeros ordenados: ', may, '-', men)


#Cargar por teclado tres números enteros. Determinar si el primero que se cargó es el
#mayor de los tres (informe en pantalla con un mensaje tal como: Es el mayor o No es el mayor).

a = int(input('Ingrese un numero: '))
b = int(input('Ingrese un numero: '))
c = int(input('Ingrese un numero: '))

if a > b and a > c:
    print('El primero es el mayor')
else:
    print('El primero no es el mayor')


#Cargar por teclado tres números enteros que se supone representan las edades de
#tres personas. Determinar si alguno de los valores cargados era negativo, en cuyo caso informe en
#pantalla con un mensaje tal como: Alguna es incorrecta: negativa. Si todos los valores eran positivos
#o cero, informe que todas eran correctas.

edad_1 = int(input('Ingrese la edad: '))
edad_2 = int(input('Ingrese la edad: '))
edad_3 = int(input('Ingrese la edad: '))

if edad_1 < 0 or edad_2 < 0 or edad_3 < 0:
    print('Alguna edad es incorrecta: negativa')

else:
    print('Edades correctas')


#se requiere un programa que calcule la suma de dos angulos y la informe en grados, minutos y segundos

angulo_1 = int(input('Ingrese el angulo uno: '))
grados_1 = int(input('Ingrese los grados: '))
minutos_1 = int(input('Ingrese los minutos'))
segundos_1 = int(input('Ingrese los segundos'))

angulo_2 = int(input('Ingrese el numero dos: '))
grados_2 = int(input('Ingrese los grados: '))
minutos_2 = int(input('Ingrese los minutos'))
segundos_2 = int(iinput('Ingrese los segundos'))

segundos_totales_1 = segundos_1 + minutos_1 * 60 + grados_1 * 3600
segundos_totales_2 = segundos_2 + minutos_2 * 60 + grados_2 * 3600

suma_segundos = segundos_totales_1 + segundos_totales_2

grados_resultado = suma_segundos // 3600
resto = suma_segundos % 3600
minutos_resultado = resto//60
segundos_resultado = resto % 60

print ('Angulo suma: ' str(grados_resultado) + '' + str(minutos_resultado))


#1. Generador de Dirección de Mail
#Se desea un programa que: solicite al usuario un nombre, un apellido y el dominio y luego,
#proponga una dirección de mail para el nombre y apellido ingresado de acuerdo a las siguientes reglas:

#Componer la dirección de correo de la siguiente manera:
#<primera letra del nombre><apellido>@<dominio>
#Por ejemplo para Nombre = Felipe, Apellido= Steffolani
#y Dominio= frc.utn.edu.ar la dirección de mail sería:
#fsteffolani@frc.utn.edu.ar
#Pero si la primera letra del nombre y la primera letra del apellido son la misma entonces utilizar:
#<nombre>.<apellido>@<dominio>
#Por ejemplo para Nombre= Soledad, Apellido= Steffolani y Dominio= colegiorosarito.edu.ar
#la dirección de mail sería:
#soledad.steffolani@colegiorosarito.edu.ar

nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
dominio = input('Ingrese un dominio: ')



if nombre[0] == apellido[0]:
    direccion = nombre + '.' + apellido + '@' + dominio
else:
    direccion = nombre[0] + apellido + '@' + dominio

print(direccion)


#SOLCUION CATEDRA

#__author__ = 'Catedra de Algoritmos y Estructuras de Datos'
# Generador de dirección de Mail
# Entradra:
# Nombre
# Apellido
# Dominio
# Salida:
# Dirección de mail propuesta

print('#' * 30)
print('# ' + 'Generador de Mails' + \
 (' ' * (30-(len('Generador de Mails')+5))) + '#')
print('#' * 30)

print('\nIngreso de datos:')
nombre = input('\tNombre : ')
apellido = input('\tApellido: ')
dominio = input('\tDominio : ')

#transformar las cadenas ingresadas en minúscula
# independientemente de cómo se ingresaron.
nombre = nombre.lower()
apellido = apellido.lower()
dominio = dominio.lower()
primera_letra_nombre = nombre[0]
primera_letra_apellido = apellido[0]

if primera_letra_apellido != primera_letra_nombre:
 mail_propuesto = primera_letra_nombre + apellido + '@' + \
 dominio
else:
 mail_propuesto = nombre + '.' + apellido + '@' + dominio

print()
print('Mail propuesto:\n\t', mail_propuesto)
print('#' * 30)

input('\nPresione enter para finalizar...')



#2. Suma - División - Potencia
#Se necesita desarrollar un programa que permita calcular la suma de tres números.
#Si el resultado es mayor a 10 dividir por 2 (mostrar su resultado sin decimales),
#en caso contrario elevar el resultado al cubo.


numero_uno = int(input('ingrese numero uno: '))
numero_dos = int(input('Ingrese numero dos: '))
numero_tres = int(input('Ingrese numero tres: '))

suma = numero_uno + numero_dos + numero_tres

if suma > 10:
    resultado = suma // 2

else:
    resultado = suma **3

print(resultado)


#SOLUCION CATEDRA

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'
# Carga de datos
a = int(input("Ingrese un número"))
b = int(input("Ingrese un número"))
c = int(input("Ingrese un número"))

# Proceso
suma = a + b + c
if suma > 10:
    resultado = suma // 2
else:
    resultado = suma ** 3

# Presentación de resultados
print("La suma es:", suma)
print("El resultado es:", resultado)



#3. Jornal de un Operario
#Se necesita desarrollar un programa para el área de recursos humanos de una empresa
#que permita informar el jornal de un determinado operario.
#Usted deberá cargar por teclado el código de turno que el operario trabajó ese día
#(1- representa Diurno y 2- representa Nocturno)
#y la cantidad de horas trabajadas.
#La política de trabajo en la empresa es que los operarios de la misma
#pueden trabajar en el turno diurno o nocturno.
#Si un operario trabaja en el turno nocturno el pago es 40.60 pesos la hora,
#si lo hace en el turno diurno cobra 35.50 pesos la hora.


turno = int(input('Jornal \n1- representa Diurno \n2- representa Nocturno \nIngrese un turno: '))
horas = int(input('Ingrese las horas trabajadas: '))

if turno == 1:
    sueldo = horas * 35.50
else:
    sueldo = horas * 40.60

print('El sueldo a pagar es de', sueldo)


#SOLUCION CATEDRA
__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Jornal de Operario')
print('=' * 80 , '\n')

#Datos
turno = int(input('Ingrese el turnos del operario (1 - Diurno, 2 - Nocturno): '))
horas = int(input('Ingrese la cantidad de horas trabajadas: '))

#Proceso
if turno == 1:
    total = horas * 35.5
else:
    total = horas * 40.60

#Resultados
print('La empresa le debe pagar al operario un jornal de $', total)



#4. Temperatura diaria
#Se solicita realizar un programa que permita ingresar tres temperaturas correspondientes
#a diferentes momentos de un día y determinar:

#Cual es el promedio de las temperaturas.
#Si existe alguna temperatura que sea mayor al promedio.

t1 = float(input('Ingrese temperatura uno: '))
t2 = float(input('Ingrese temperatura dos: '))
t3 = float(input('Ingrese temperatura tres: '))

promedio = (t1+t2+t3) / 3

r_promedio = round(promedio, 2)

if t1 > promedio:
    temperatura = 'la primera temperatura ingresada'

elif t2 > promedio:
    temperatura = 'la segunda temperatura ingresada'

else:
    temperatura = 'la tercera temperatura ingresada'

print('\nEl promedio de temperatura es', r_promedio, '\n\nLa temperatura mayor al promedio es', temperatura)


#SOLUCION CATEDRA

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random

print('\nIngreso de temperaturas')
temp1 = int(input("Ingrese la temperatura 1"))
temp2 = int(input("Ingrese la temperatura 2"))
temp3 = int(input("Ingrese la temperatura 3"))

# Procesos calculo del promedio
promedio = (temp1 + temp2 + temp3) / 3

# Salida de resultados
print ('El promedio de las temperaturas ingresadas fue ', promedio, ' grados')

if temp1 > promedio or temp2 > promedio or temp3 > promedio:
    print('Existe al menos una temperatura que supera al promedio')
else:
    print('Todas las temperaturas estan por debajo del promedio')


import random


#5. Tarjeta de Bingo
#Realizar un programa que genere 15 números aleatorios enteros en el rango del 1 al 100,
#que representaria la tarjeta de bingo de una persona.
#Una vez generados los números aleatorios solicitar al usuario que ingrese 3 números enteros
#y a partir de alli mostrar los siguientes mensajes:

#Si el usuario no marcó ninguno de los números indicarlo diciendo
#"El jugador tiene mala suerte, no marcó ninguna casilla"
#Caso contrario mostrar "El jugador marcó algún numero de la tarjeta".

numeros = random.randint(1, 100),random.randint(1, 100),random.randint(1, 100),random.randint(1, 100),\
          random.randint(1, 100),random.randint(1, 100),random.randint(1, 100),random.randint(1, 100),\
          random.randint(1, 100),random.randint(1, 100),random.randint(1, 100),random.randint(1, 100),\
          random.randint(1, 100),random.randint(1, 100),random.randint(1, 100)

num1 = int(input('Ingrese numero uno (1, 100): '))
num2 = int(input('Ingrese numero dos (1, 100): '))
num3 = int(input('Ingrese numero tres (1, 100): '))

if num1 or num2 or num3 == numeros:
    resultado = '\nEl jugador marcó algún numero de la tarjeta'

else:
    resultado = '\nEl jugador tiene mala suerte, no marcó ninguna casilla'

print(resultado)


#SOLUCION CATEDRA

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random

print('Tarjeta de Bingo')
print("=" * 80)

print("\nCarga de Datos")
print('-' * 80)

billete = random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),\
          random.randint(1,100), random.randint(1,100),random.randint(1,100),random.randint(1,100),\
          random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),\
          random.randint(1,100),random.randint(1,100),random.randint(1,100)

primer_numero = int(input('Ingrese la bolilla que salio sorteada (un valor ente 1 y 100): '))
segundo_numero = int(input('Ingrese la bolilla que salio sorteada (un valor ente 1 y 100): '))
tercer_numero = int(input('Ingrese la bolilla que salio sorteada (un valor ente 1 y 100): '))


# Proceso y salida de resultados
print('La tarjeta del usuario es: ', billete)
if primer_numero in billete or segundo_numero in billete or tercer_numero in billete:
    print('El jugador marco algun numero de la tarjeta')
else:
    print('El jugador tiene mala suerte, no marco ninguna casilla')


#6. Analisis de palabra
#Se pide un programa que le solicite al usuario que ingrese una palabra.
#Con esa palabra calcular los siguientes puntos:

#Determinar la cantidad de letras que tiene  la palabra.
#Mostrar un mensaje que informe si la palabra termina en vocal.

import random

palabra = input('Ingrese una palabra: ')

cantidad = len(palabra)
ultima_letra = palabra[cantidad - 1]

vocal = False

if ultima_letra == 'a' or ultima_letra == 'e' or ultima_letra == 'i' or ultima_letra == 'o' \
        or ultima_letra == 'u':

    vocal = True


print('La cantidad de letras de la palabra ingresada es', cantidad)

if vocal == True:
    print('La palabra termina en vocal')
else:
    print('La palabra no termina en vocal')



#SOLUCION CATEDRA

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Analisis de Palabra')
print('=' * 80)

# Lectura de datos
palabra = input('Ingrese la palabara a analizar en mayusculas: ' )

# Proceso
largo = len(palabra)
ultima_letra = palabra[largo - 1]

termina_vocal = False
if ultima_letra == 'A' or ultima_letra == 'E' or ultima_letra == 'I' or \
    ultima_letra == 'O' or ultima_letra == 'U':
    termina_vocal = True

# Salida
print('La palabra ingresada tiene una longitud de ', largo, ' letras')
if termina_vocal:
    print('La palabra ingresada termina en vocal')




#7. Tirada de moneda
#Programar una tirada de una moneda (opciones: cara o cruz) aleatoriamente.
#Permitir que un jugador apueste a cara o cruz y luego informar si acertó o no con su apuesta.

import random

tirada = random.choice(['cara', 'cruz'])

apuesta = input('Elija una apuesta cara o cruz: ')

if tirada == apuesta:
    resultado = 'El jugador acerto su apuesta'

else:
    resultado = 'El jugador no acerto la apuesta'

print(resultado)


#SOLUCION CATEDRA

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random

print('Tirada de la moneda')
print('=' * 80)

caras = 'cara', 'cruz'

apuesta = int(input('Seleccion que cara desea apostar (0 Cara 1 Cruz): '))
jugada = random.choice(caras)

if jugada == caras[apuesta]:
    print('El jugador ha ganado el juego, acerto, salio', jugada)
else:
    print('El jugador ha perdido el juego salio', jugada, 'y el jugador aposto a', caras[apuesta])

import random

#8. Lanzamiento de dados
#Simular un juego en el que se lanzan dos dados.

#Si ambos dados son iguales o la suma entre ellos es impar, gana el usuario.
#En caso contrario, gana la máquina.

print('Tirada de dados')

dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)

suma = dado1 + dado2

if suma % 2 != 0 or dado1 == dado2:
    resultado = 'Gana el usuario'

else:
    resultado = 'Gana la maquina'

print('\nPrimer dado = ', dado1, '\nSegundo dado = ', dado2,'\n\n',resultado)

#SOLUCION CATEDRA

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'
import random

print("Juego de Dados\n")

dado1 = random.randrange(1, 7)
dado2 = random.randint(1, 6)

print("Dado 1:", dado1, "- Dado 2:", dado2)

suma = dado1 + dado2

if dado1 == dado2 or (suma%2) != 0:
 res = "Ganaste!"
else:
 res = "Perdiste!"


print("Resultado:", res)



#9. Edad mínima
#Ingresar por teclado las edades de 3 participantes de un concurso.

#Informar si todos cumplen con la edad mínima establecida para el mismo, también ingresada por teclado.

edad_minima = int(input('Ingrese la edad minima para el concurso: '))

participante1 = int(input('Ingrese la edad del participante uno: '))
participante2 = int(input('Ingrese la edad del participante dos: '))
participante3 = int(input('Ingrese la edad del participante tres: '))

if participante1 >= edad_minima:
    edad1 = 'El participante uno cumple con la edad minima requerida para el concurso'
else:
    edad1 = 'El participante uno no cumple con la edad minima requerida para el concurso'

if participante2 >= edad_minima:
    edad2 = 'El participante dos cumple con la edad minima requerida para el concurso'
else:
    edad2 = 'El participante dos no cumple con la edad minima requerida para el concurso'

if participante3 >= edad_minima:
    edad3 = 'El participante tres cumple con la edad minima requerida para el concurso'
else:
    edad3 = 'El participante tres no cumple con la edad minima requerida para el concurso'

print('\n',edad1,'\n\n',edad2,'\n\n',edad3)


#SOLUCION CATEDRA

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

#Datos
edad1 = int(input('Participante 1 - Ingrese edad: '))
edad2 = int(input('Participante 2 - Ingrese edad: '))
edad3 = int(input('Participante 3 - Ingrese edad: '))

minimo = int(input('Ingrese edad minima para participar: '))

#Proceso y resultado
if edad1 >= minimo and edad2 >= minimo and edad3 >= minimo:
    print('TODOS los participantes cumplen con la edad mínima')
else:
    print('NO TODOS los participantes cumplen con la edad mínima')



#10. Terreno
#Se ingresan las medidas de frente y fondo de un terreno.

#Determinar si es cuadrado o rectangular y calcular su superficie.

frente = float(input('Ingrese las medidas de frente del terreno: '))
fondo = float(input('Ingrese las medidas de fondo del terreno: '))

if frente == fondo:
    forma = 'es un cuadrado'
else:
    forma = 'es un rectangulo'

superficie = frente * fondo

print('el terreno ', forma,'y la superficie es ',superficie)


#SOLUCION CATEDRA

fondo = float(input('Ingrese fondo del terreno (en metros): '))
frente = float(input('Ingrese frente del terreno (en metros): '))

#Proceso
if frente == fondo:
    forma = "CUADRADA"
else:
    forma = "RECTANGULAR"

superficie = round(frente * fondo,2)

#Resultados
print('El terreno tiene forma',forma,'y',superficie,'metros cuadrados de superficie')



#11. Galería de arte
#Una galería de arte desea preparar un catálogo de sus cuadros más famosos.

#Se realiza una prueba con tres cuadros y por cada uno se ingresa el año en que fue creado.
# El programa deberá:

#Verificar si todos los cuadros son anteriores al siglo XX
#(El siglo XX es el siglo pasado. Se inició en el año 1901 y terminó en el año 2000).
#Determinar si alguna de las obras fue creada en un año que se ingresa por teclado.
#Informar la diferencia en años entre la obra más nueva y la más antigua.

cuadro1 = int(input('Ingrese el año en que fue creado el cuadro uno: '))
cuadro2 = int(input('Ingrese el año en que fue creado el cuadro dos: '))
cuadro3 = int(input('Ingrese el año en que fue creado el cuadro tres: '))

anio = int(input('Ingrese un año: '))

iniciosigloXX = 1901
finsigloXX = 2000

if cuadro1 >= iniciosigloXX and cuadro1 <= finsigloXX:
    pertenencia1 = 'El cuadro uno pertenece al siglo XX'
else:
    pertenencia1 = 'El cuadro uno no pertenece al siglo XX'


if cuadro2 >= iniciosigloXX and cuadro2 <= finsigloXX:
    pertenencia2 = 'El cuadro dos pertenece al siglo XX'
else:
    pertenencia2 = 'El cuadro dos no pertenece al siglo XX'


if cuadro3 >= iniciosigloXX and cuadro3 <= finsigloXX:
    pertenencia3 = 'El cuadro tres pertenece al siglo XX'
else:
    pertenencia3 = 'El cuadro tres no pertenece al siglo XX'

if cuadro1 == anio or cuadro2 == anio or cuadro3 == anio:
    anioingresado = 'Hay al menos un cuadro que pertenece al año ingresado'
else:
    anioingresado = 'No hay ningun cuadro que pertenezca a ese año'

if cuadro1 > cuadro2 and cuadro1 > cuadro3:
    mayor = cuadro1
elif cuadro2 > cuadro1 and cuadro2 > cuadro3:
    mayor = cuadro2
else:
    mayor = cuadro3

if cuadro1 < cuadro2 and cuadro1 < cuadro3:
    menor = cuadro1
elif cuadro2 < cuadro1 and cuadro2 < cuadro3:
    menor = cuadro2
else:
    menor = cuadro3

diferencia = mayor - menor

print('\n',pertenencia1,'\n',pertenencia2,'\n',pertenencia3,
      '\n',anioingresado,
      '\n La diferencia de años entre la obra mas nueva y mas antigua es de',diferencia)



#SOLUCION CATEDRA

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

# Presentación e ingreso de datos
print('GALERÍA DE ARTE')
cuadro1 = int(input('Ingrese año de creación del cuadro 1: '))
cuadro2 = int(input('Ingrese año de creación del cuadro 2: '))
cuadro3 = int(input('Ingrese año de creación del cuadro 3: '))

# Proceso
# Todos los cuadros son anteriores al siglo XX?
mensaje_sxx = ' son anteriores al siglo XX'
if cuadro1 < 1900 and cuadro2 <= 1900 and cuadro3 <= 1900:
    mensaje_sxx = 'TODOS' + mensaje_sxx
else:
    mensaje_sxx = 'NO TODOS' + mensaje_sxx
# Alguno fue creado en cierto año?
anio = int(input('\nIngrese año de creación a buscar: '))
mensaje_anio = ' hay cuadros correspondientes al año ' + str(anio)
if cuadro1 == anio or cuadro2 == anio or cuadro3 == anio:
    mensaje_anio = 'SÍ' + mensaje_anio
else:
    mensaje_anio = 'NO' + mensaje_anio
# Diferencia entre más nueva y más antigua
nueva = max(cuadro1, cuadro2, cuadro3)
antigua = min(cuadro1, cuadro2, cuadro3)
diferencia = nueva - antigua

# Resultados
print(mensaje_sxx)
print(mensaje_anio)
print('La diferencia entre la obra más nueva (', nueva, ') y la más antigua (', antigua, ') es', diferencia,'años')


#12. Cartas de Truco
#Desarrollar un programa que genere al azar tres cartas simulando una mano de truco.
# A continuación deberá:

#Informar si entre las cartas se encuentra el as de espadas
#Verificar si las tres cartas son del mismo palo. Si es así, mostrar la suma de las dos mayores.
# En caso contrario, informarlo.

import random

palos = ('Oro', 'Basto', 'Espada', 'Copa')
numeros = (1, 2, 3, 4, 5, 6, 7, 10, 11, 12)

print('CARTAS DE TRUCO')
carta1 = random.choice(numeros), random.choice(palos)
carta2 = random.choice(numeros), random.choice(palos)
carta3 = random.choice(numeros), random.choice(palos)

print(carta1, carta2, carta3)

if (carta1[0] == 1 and carta1[1] == 'Espada') \
        or (carta2[0] == 1 and carta2[1] == 'Espada') \
        or (carta3[0] == 1 and carta3[1] == 'Espada'):
    print('Tiene el as de espadas')
else:
    print('NO Tiene el as de espadas')

if carta1[1] == carta2[1] and carta1[1] == carta3[1]:
    menor = min(carta1[0], carta2[0], carta3[0])
    suma = carta1[0] + carta2[0] + carta3[0] - menor
    print('La suma de las dos cartas mayores es', suma)
else:
    print('No hay tres cartas del mismo palo')



#13. Calculo de Precios con Descuento
#Una empresa nos solicito un programa que nos permita calcular
#los precios de los productos que vende al publico
#para ello, nuestro programa debe pedir el precio unitario,
#la cantidad que se vendio y si se pago en efectivo o no.
#En base a esto determinar

#El Precio final sin descuentos del articulo (precio unitario por cantidad)

#Calcular un descuento si el usuario pago en efectivo y
#la cantidad vendida es superior a 10 unidades del 15% caso contrario solo aplicar un 5% de descuento

precio_unitario = float(input('Ingrese el precio del producto: '))
cantidad_vendida = int(input('Ingrese la cantidad vendida: '))
efectivo = input('¿ La compra se pago con efectivo ? (si o no): ')

if efectivo == 'si' and cantidad_vendida >= 10:
    descuento = precio_unitario * 15 / 100
else:
    descuento = precio_unitario * 5 / 100

precio = precio_unitario * cantidad_vendida
precio_final = precio - descuento

print('El precio del producto es ',precio_unitario,'y el total con descuento es ',precio_final)


#SOLUCION CATEDRA

__author__ = 'Algoritmos y Estructuras de Datos'

print('Calculo de Precio de Venta')
print('=' * 60)

precio_unitario = float(input('Ingrese el precio unitario del articulo: '))
cantidad = int(input('Ingrese la cantidad que se vendio del producto: '))
es_efectivo = input('La venta del articulo, se abono en efectivo? (Responda S o N): ')

print('...Procesando')
precio = precio_unitario * cantidad

if es_efectivo == 'S' and cantidad > 10:
    descuento = precio * 0.15
else:
    descuento = (precio * 0.05)

precio_final = precio - descuento

print('\nSalidas')
print('-' * 60, '\n')
print('El Precio Final que se cobro del articulo fue de $', round(precio_final, 2))
print('se le aplico un ', descuento, '% de descuento a la operacion')
'''




#14. Tarifas de Peaje
#La empresa de peajes AED Pase-Pase S.R.L, festeja su séptimo aniversario y, por tal motivo,
#el día de hoy ofrece premios a a sus clientes.

#Estos premios se calculan de la siguiente manera:

#1) Cada vez que pasa un cliente, se sortea un número del 0 al 9.
#Si el número coincide con el último dígito de la patente del vehículo,
#se le cobra la tarifa promocional de $50, si no, se le cobra la tarifa estándar de $90

#2) Independientemente de la tarifa que deba pagar, si el último dígito de la patente es 7,
#entonces recibe un descuento del 50%, en caso contrario un descuento del 10%.

#Desarrolle un programa en Python que le solicite al usuario los dígitos de su patente
# (únicamente los dígitos),
#simule su paso por el peaje e indique el monto a abonar.

import random

patente = int(input('Ingrese los numeros de su patente: '))

sorteo = random.randint(0, 9)
ultimo_digito = patente % 10

if patente == ultimo_digito:
    tarifa = 50
else:
    tarifa = 90

if ultimo_digito == 7:
    descuento = tarifa * 50 / 100
else:
    descuento = tarifa * 10 / 100

precio_final = tarifa - descuento

print('\n Sorteo',sorteo,'\nLa tarifa que debe pagar es de', tarifa,
      '\nEl precio final con el descuento es de', precio_final )


#SOLUCION CATEDRA

import random

# Programa de cálculo de peajes
print('Bienvenido a Pase-Pase')
print('=' * 20)

# Ingreso de datos
digitos_patente = int(input('Ingrese dígitos:'))

# Sorteo del dígito
sorteo = random.randint(0, 9)
print('Sorteo: ', sorteo)

# Extracción del último dígito de la patente
ultimo_digito = digitos_patente % 10

# Cálculo de la tarifa
if sorteo == ultimo_digito:
    print('Tarifa Promocional')
    # Si coincide el último dígito con lo sorteado
    # Es precio promocional
    tarifa = 50
else:
    print('Tarifa Completa')
    # Si no coincide, es precio completo
    tarifa = 90

# Cálculo del descuento
if ultimo_digito == 7:
    print('Descuento del 50%')
    # Si la patente termina en 7, el
    # descuento es de 50%
    descuento = tarifa * 0.5
else:
    print('Descuento del 10%')
    # Si la patente NO termina en 7, el
    # descuento es del 10%
    descuento = tarifa * 0.1

# Monto final a pagar
monto = tarifa - descuento

# Resultados
print('=== RESULTADOS ===')
print('Debe abonar: $', monto)



