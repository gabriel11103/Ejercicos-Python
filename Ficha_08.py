'''
#Desarrollar un Programa Controlado por Menú de Opciones, que incluya opciones
#para realizar las siguientes tareas:

#1. Cargar un valor entero n por teclado, y obtener la suma de los enteros del 1 al n.
#2. Cargar un valor entero n por teclado, y obtener su factorial.
#3. Cargar por teclado los coeficientes a, b, y c de un polinomio de segundo grado, y obtener el
#valor del polinomio en el punto x, siendo x un valor que también se carga por teclado.


print ('Ingrese 1 para calcular la suma de los enteros del 1 al numero ingresado'
       '\nIngrese 2 para calcular el factorial de un numero'
       '\nIngrese 3 para calcular el valor de un polinomio en el punto x'
       '\nIngrese 4 para salir'  )

opcion = int(input('Ingrese un numero del menu: '))

while opcion >= 0 and opcion < 4:
    if opcion == 1:
        n = -1
        while n < 0:
            n = int(input('Ingrese n (>=0, por favor): '))
        if n < 0:
            print('Error... se pidio >=0... cargue de nuevo...')
            s = n * (n+1) // 2
            print('Suma de los enteros del 1 al', n, ':', s)

    elif opcion == 2:
        n = -1
        while n < 0:
            n = int(input('Ingrese n (>=0, por favor): '))
            if n < 0:
                print('Error... se pidio >=0... cargue de nuevo...')
        f = 1
        for i in range(2, n+1):
            f *= i
        print('Factorial de', n, ':', f)

    elif opcion == 3:
        a = float(input('a: '))
        b = float(input('b: '))
        c = float(input('c: '))
        x = float(input('x: '))
        p = a*pow(x, 2) + b*x + c
        punto_x =('Valor de p(', x,'):', p)

        print(punto_x)


    opcion = int(input('Ingrese un numero del menu: '))


#El Juego del Número Secreto consiste en lo siguiente: la computadora tiene un
#número guardado (que el jugador obviamente no conoce) y el jugador debe tratar de adivinarlo. Si lo
#logra, gana el juego y la computadora le avisa en cuántos intentos lo hizo. Si no lo logra en cierta
#cantidad predefinida intentos, el juego termina y se avisa que el jugador ha perdido. La cantidad
#máxima de intentos que el jugador tendrá a su disposición es un número que debe cargarse por
#teclado antes de comenzar a jugar, al igual que el límite derecho del intervalo que contendrá al
#número secreto elegido por el computador (es decir, el usuario debe poder indicar el número estará
#entre 1 y 30 o bien entre 1 y 50 o bien en el intervalo que el propio usuario decida). Desarrolle un
#programa completo que implemente este juego

import random

n = int(input('Ingrese el numero de intentos que puede tener: '))
intentos = 0
acierto = False

for i in range(n):
        int_derecho = int(input('Ingrese hasta que numero se adivinara: '))
        numero = int_derecho -1
        print('El intervalo estara entre el numero 1 y el numero',int_derecho)
        numero_pc = random.randint(1,int_derecho)

        while not acierto and intentos < n:
            intentos += 1
            num_elegido = int(input('Elija el numero que cree que saldra: '))
            if num_elegido == numero_pc:
                acierto = True


if acierto == True:
    print('Felicidades adivinaste el numero correcto en',intentos,'intentos')
else:
    print('Perdio no adivino el numero que era', numero)



#SOLUCION CATEDRA

import random
# Títulos y carga de datos básicos...
print('Juego del Número Secreto... Configuración Inicial...')
limite_derecho = int(input('El número secreto estará entre 1 y: '))
cantidad_intentos = int(input('Cantidad máxima de intentos: '))
# limites iniciales del intervalo de búsqueda...
izq, der = 1, limite_derecho
# contador de intentos...
intentos = 0
# bandera de estado: si es False, el
# número aún no ha sido encontrado...
encontrado = False
# el numero secreto...
secreto = random.randint(1, limite_derecho)
# el ciclo principal... siga mientras no
# haya sido encontrado el número, y la
# cantidad de intentos máxima no sea superada...
while not encontrado and intentos < cantidad_intentos:
 intentos += 1
 print('\nEl numero está entre', izq, 'y', der)
 # un valor para forzar al ciclo a ser [1, N]...
 # ... ver Ficha 7.
 num = izq - 1
 # carga y validación del número sugerido por el usuario...
 while num < izq or num > der:
 num = int(input('[Intento: ' + str(intentos) + '] => Ingrese: '))
 if num < izq or num > der:
 println('Error... le dije entre', izq, 'y', der, '...')
 # controlar si num es correcto y avisar en ese caso...
 if num == secreto:
 encontrado = True
 # ... pero si no lo es, ajustar los límites
 # del intervalo de búsqueda...
 elif num > secreto:
 der = num
 else:
 izq = num
# control final...
if encontrado:
 print('\nGenio!!! Acertaste en', intentos, 'intentos')
else:
 print('\nLo siento!!! Acabaron los intentos. El número era:', secreto)


'''

#Desarrollar un programa que implemente el conocido juego de manos llamado
#"Piedra , Papel y Tijera". En este juego participan dos jugadores, uno contra el otro. Cada uno de
#ellos, al mismo tiempo que el otro, debe mostrar con una de sus manos, alguna de las tres figuras
#básicas llamadas Piedra (la mano cerrada), Papel (la mano abierta y extendida) o Tijera (los dedos de
#la mano formando una V). Luego se comparan las figuras que cada uno mostró, y se determina el
#ganador de acuerdo a la siguiente secuencia de reglas generales:
#• Piedra vence a Tijera (ya que Tijera se rompe si intenta cortar a Piedra)
#• Tijera vence a Papel (ya que Tijera corta a Papel)
#• Papel vence a Piedra (ya que Papel envuelve a Piedra)
#Típicamente, se juega "a la mejor de tres": los jugadores se enfrentan en tres jugadas, y se declara
#ganador al que gane en dos o más de esas tres.






'''
#1. Menu de Opciones con secuencias
#Escribir un programa que le permita al usuario,
#a través de un menú de opciones,las siguientes operaciones:

#a) Dada la serie de números naturales desde 1 hasta n
#(n ingresado por teclado y validando que sea mayor a cero) mostrar la suma de los cuadrados

#b) Ingresar un texto finalizado por un punto y determinar
#la cantidad de palabras que finalizan con vocales

#c) Ingresar una serie de números (la carga finaliza con cero)
#y determinar si hay mayor cantidad de valores pares o de impares

#d) Salir

print = ('Ingrese 1 para calcular la suma de los cuadrados de un numero'
       '\nIngrese 2 para calcular la cantidad de palabras que finalizan con vocales'
       '\nIngrese 3 para ingresar una serie de numeros y determinar pares e impares'
       '\nIngrese 4 para salir'  )

opcion = int(input('Ingrese un numero: '))

while opcion >= 0:
    if opcion == 1:
        n = int(input('Ingrese un numero: '))
        if n > 0:
            suma = n * (n+1) // 2
        else:
            suma = ('Error ingreso un numero negativo')

    if opcion == 2:
        texto = input('Ingrese un texto finalizando con un punto(.): ')
        if texto










#2. Secuencia numérica
#Ingresar una secuencia de números, de a uno por vez,
#la carga finaliza cuando el usuario ingresa el cero. Determinar

#a) Porcentaje que representan los números divisibles por 3
#sobre el total de números ingresados en la secuencia

#b) Determinar la cantidad de números que son el cuadrado del número anterior

#c) Determinar la posición del mayor elemento impar de la secuencia


#3. Secuencia de n números
#Ingresar una secuencia de n números, de a uno por vez.
#El valor de n se ingresa por teclado, validar que sea mayor a 0. Determinar:

#a) Cuántos números ingresados terminan en 5

#b) La cantidad de veces que aparece el primer número ingresado por el usuario en la secuencia

#c) Cuántos números ingresados son mayores al anterior



#4. Secuencia numérica II
#Ingresar un secuencia de números, de a uno por vez,
#la carga finaliza cuando el usuario ingresa el cero. Determinar:

#a) El promedio de los números que son múltiplos de 6

#b) Cantidad de números que son divisor exacto del anterior

#c) Indicar la cantidad de veces que se generó una secuencia ascendente de 3 o más números impares


#5. Tito el robot
#Desarrollar un programa controlado por menú de opciones,
#que permita simular el desplazamiento de un robot sobre un plano.

#Inicialmente se genera la posición aleatoria del robot en forma de punto (x,y).
#Luego se presenta un menú de opciones que permita los siguientes movimientos:

#a) Girar al norte y avanzar 10 pasos

#b) Girar al sur y avanzar 20 pasos

#c) Girar al este y avanzar 10 pasos

#d) Girar al oeste y avanzar 20 pasos

#El programa debe mostrar la ubicación del robot al inicio de cada desplazamiento.


#6. Menú de opciones y validación
#Se pide desarrollar un programa controlado por menú de opciones que permita lo siguiente:

   #a) Ingresar números (la carga finaliza cuando se ingresa el -1) y calcular su promedio.

   #b) Generar n valores aleatorios entre -100 y 100 (n se ingresa por teclado).
      #Determinar la cantidad de valores negativos y positivos.

   #c) Cargar la nota de un alumno e informar si está aprobado teniendo en cuenta
      #que la nota es un valor entre 0 y 10, siendo mayor o igual a 4 si está aprobado.


#7. Validación Datos Personales
#Escribir un programa, que le permita a un usuario a través de un menu de opciones,
#las siguiente operaciones:

  #a) Ingresar el numero de CUIT de una persona (99-99999999-9)
     #y determinar si el mismo el valido bajo las siguientes condiciones:

         #1 - Contiene 13 caracteres, todos dígitos con dos guiones en la 3er y en la 11a posición

         #2 - El dígito verificador es igual al ultimo dígito del CUIT,
             #para obtener el dígito verificador se debe multiplicar cada uno de los 10 dígitos
             #por la secuencia 5432765432 e ir acumulando el producto,
             #luego se calcula el resto modulo 11 y por ultimo a 11
             #se le resta el resto del modulo obtenido. El resultado es el dígito verificador

  #b) Ingresar el DNI de una persona y determinar si el mismo el valido (X9.999.999)

  #c) Salir
'''

#8. Menu de Opciones con Secuencias
#Se pide desarrollar un programa controlado por menu de opciones
#que permita realizar las siguientes operaciones:

    #a) Ingresar un secuencia de n números, validar que n sea mayor a cero,
       #y determinar cual la cantidad de los números múltiplos de 3 y 5,
       #y que porcentaje representan sobre el total de números

    #b) Ingresar un texto, el mismo termina con punto,
       #determinar cuantas palabras de mas de 4 letras hay en el texto

    #c)  Ingresar el nombre y las notas finales de tres alumnos de postgrado,
        #indicar el nombre del alumno con peor nota de los tres

    #d) Salir


num = -1
mul_3y5 = 0
letra = 0
pal_4 = 0
peor_nota = ''

while num != 0:
    print('\nMENU DE OPCIONES: '
          '\n1 si quiere ingresar unas secuencia de numeros'
          '\n2 si quiere ingresar un texto'
          '\n3 si quiere cargar las notas de tres alumnos'
          '\n0 si quiere salir')
    num = int(input('Ingrese la opcion elegida: '))

    if num == 1:
        sec = int(input('\nIngrese una secuencia de numeros(mayor a 0): '))
        while sec > 0:
            if sec % 3 == 0 and sec % 5 == 0:
                mul_3y5 += 1
            if sec < 1:
                print('ingrese un numero valido')
            sec = int(input('Ingrese una secuencia de numeros(mayor a 0): '))
        print('La cantidad de numeros multiplos de 3 y 5 son: ',mul_3y5)

    if num == 2:
        text = input('\nIngrese un texto(termina con punto): ')
        if text[-1] != '.':
           text += '.'
        for letras in text:
            if letras != '' and letras != '.':
                letra += 1
        if letra > 4:
            pal_4 += 1
        print('hay ',pal_4,'palabras de mas de cuatro letras')

    if num == 3:
        nom1 = input('\nIngrese el nombre del alumno uno: ')
        notas1 = int(input('Ingrese las notas del alumno uno: '))
        nom2 = input('Ingrese el nombre del alumno dos: ')
        notas2 = int(input('Ingrese las notas del alumno dos: '))
        nom3 = input('Ingrese el nombre del alumno tres: ')
        notas3 = int(input('Ingrese las notas del alumno tres: '))

        if notas1 > notas2:
            peor_nota = nom2
        elif notas2 > notas3:
            peor_nota = nom3
        elif notas3 > notas1:
            peor_nota = nom1

        print('El alumno con peor nota es', peor_nota)
'''
#SOLUCION CATEDRA

__author__ = 'Algoritmos y Estructuras de Datos'

print('Ejericio tipo parcial')
print('=' * 60)
print('\n')

menu = 'Menu de Opciones\n' \
       '==================================\n' \
       '1 ------- Ingresar n numero y calcular porcentaje\n' \
       '2 ------- Analisis de texto\n' \
       '3 ------- Buscar peor alumno\n' \
       '0 ------- Salir\n' \
       'Ingrese su opcion: '

opcion = -1
while opcion != 0:
    # presentar las opciones
    opcion = int(input(menu))
    if opcion == 1:
        # Ingreso a la opcion 1
        n = 0
        cont_multiplos = 0
        while n <= 0:
            n = int(input('Ingresar la cantidad de numeros a procesar: '))
            if n <= 0:
                print('Error!!! Usted debe ingresar un numero mayor a cero')

        for i in range(n):
            numero = int(input('Ingrese el ' + str(i + 1) + '° de la secuencia: '))
            if numero % 3 == 0 or numero % 5 == 0:
                cont_multiplos += 1
        porcentaje = cont_multiplos * 100 / n
        print('La cantidad total de multiplos de 3 y 5 fueron:', cont_multiplos)
        print(' y representan un ', round(porcentaje, 2), '% sobre el total de numero')

    elif opcion == 2:
        # Ingreso a la opcion 2
        texto = input('Ingresar un texto (debe terminar con punto): ')
        if texto[-1] != '.':
            texto += '.'

        cl = cp = 0
        for caracter in texto:
            # tengo que identificar cuando recorro una palabra y cuando deje de recorrerla
            if caracter != ' ' and caracter != '.':
                # dentro de la palabra, leyendo de letras
                cl += 1
            else:
                # termine de recorrer la palabra y pregunto si he encontrado lo que estaba buscando en esa palabra
                if cl > 4:
                    cp += 1
                cl = 0

        print('La cantidad total de palabras de mas de cuatro letras fue de:', cp)

    elif opcion == 3:
        # Ingreso a la opcion 3
        nombre_alumno_1 = input('Ingrese el nombre del primer alumno: ')
        nota_alumno_1 = int(input('Ingrese la nota final del primer alumno: '))
        nombre_alumno_2 = input('Ingrese el nombre del segundo alumno: ')
        nota_alumno_2 = int(input('Ingrese la nota final del primer alumno: '))
        nombre_alumno_3 = input('Ingrese el nombre del tercer alumno: ')
        nota_alumno_3 = int(input('Ingrese la nota final del primer alumno: '))

        if nota_alumno_1 < nota_alumno_2 and nota_alumno_1 < nota_alumno_3:
            peor_alumno = nombre_alumno_1
        elif nota_alumno_2 < nota_alumno_3:
            peor_alumno = nombre_alumno_2
        else:
            peor_alumno = nombre_alumno_3

        print('El alumno de posgrado con la peor nota fue:', peor_alumno)
    print('\n\n')
'''


