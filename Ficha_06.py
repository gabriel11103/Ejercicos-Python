'''
#escribir un programa que determine cuantos numeros son negatuvos

cont = 0
vueltas = 0

num = int(input('Ingrese un numero: '))

while vueltas < 3:
    vueltas += 1
    if num < 0
        cont += 1

    num = int(input('Ingrese un numero: '))

print('Cantidad de negativos', num)


#Cargar por teclado una lista de números enteros que irán llegando uno a uno, y que
#representan cantidades mensuales de automóviles nuevos vendidos en el país durante cierto período.
#Para indicar que la carga de datos debe finalizar, se ingresará el valor -1 (menos uno) (note que el
#valor 0 (cero) puede ser un dato valido: es perfectamente posible que no haya habido ventas en un
#mes determinado). Se pide:
#a. Determinar cuántas de esas cantidades fueron mayores o iguales que 0 pero menores que
#10000 unidades, cuántas fueron mayores o iguales a 10000 pero menores que 15000, y
#cuántas fueron mayores o iguales que 15000.
#b. Determinar la cantidad total de automóviles nuevos que se vendieron en el país.
#c. Determinar si se ingresó al menos una cantidad igual a 0 o no. Informe con un mensaje simple
#en pantalla.

cont0 = 0
cont1000 = 0
cont1500 = 0

total = 0

cero = False

autos_mensuales = int(input('Ingrese la cantidad de autos vendidos en el mes(con -1 termina el proceso):'))

while autos_mensuales != -1:
    if 0 <= autos_mensuales < 1000:
        cont0 += 1
    elif 1000 <= autos_mensuales < 1500:
        cont1000 += 1
    else:
        cont1500 += 1

    total += autos_mensuales

    if autos_mensuales == 0:
        cero = True

    autos_mensuales = int(input('Ingrese la cantidad de autos vendidos: '))


print(
      'La cantidad de autos vendidos en el mes entre 0 y 1000 unidades fue', cont0,
      '\nLa cantidad de autos vendidos en el mes entre 1000 y 1500 unidades fue',cont1000,
      '\nLa cantidad de autos vendidos en el mes de mas de 1500 unidades fue',cont1500,
      '\nLa cantidad total vendida fue de',total,
      )
if cero:
    print ('Se registro al menos un mes en el que la venta fue 0')
else:
    print('No se registro al menos un mes en que la venta fue 0')


#Cargar por teclado un conjunto de números enteros, uno a uno. La carga sólo debe
#terminar cuando se ingrese el cero. Determine si los números que se ingresaron eran todos positivos
#o todos negativos (sin importar en qué orden hayan entrado). Por ejemplo, la secuencia {8, 4, 3, 7}
#cumple con la consigna indicada (son todos positivos). La secuencia {-2, -1, -5} también cumple (son
#todos negativos), pero esta otra secuencia {10, -8, 2, 12} no cumple (hay números de distinto signo
#entremezclados). Si todos los números eran efectivamente del mismo signo, muestre también la suma
#de esos números (no mostrar la suma si había números de signos diferentes entremezclados).


ok = True

suma = 0

actual = int(input('Cargue un número (con 0 corta): '))

anterior = actual

while actual != 0:

    if actual * anterior < 0:
      ok = False

    suma += actual
    anterior = actual

    actual = int(input('Cargue otro (con 0 corta): '))

if ok:
    print('Todos los números eran del mismo signo')
    print('La suma de esos números es:', suma)
else:
    print('Los números no eran todos del mismo signo')


#Un polinomio de segundo grado tiene la forma p(x) = ax2 + bx + c donde a, b, y c son
#valores constantes conocidos como los coeficientes del polinomio y x es la variable independiente. Se
#supone que el coeficiente a es diferente de cero (pues de lo contrario el término ax2 desaparece y el
#polinomio se convierte en un de primer grado).
#Si el polinomio se iguala a cero, se obtiene una ecuación de segundo grado: ax2 + bx + c = 0 y
#resolver la ecuación es el proceso de hallar los valores de x que hacen que efectivamente el polinomio
#valga cero.
#Por el Análisis Matemático se sabe que todo polinomio de grado n tiene exactamente n raíces (reales
#y/o complejas) para su ecuación y por lo tanto, una ecuación de segundo grado tiene dos raíces a las
#que tradicionalmente se designa como x1 y x2. El problema de encontrar estos dos valores fue
#estudiado desde varios siglos antes de Cristo al menos por los babilonios, los indios y los árabes (de
#hecho, nuestro ya conocido Al-Jwarizmi contribuyó de forma significativa) y la fórmula de cálculo es
#bien conocida:
#𝑥1−2 = −𝑏 ± √𝑏 2 − 4𝑎𝑐
#          2𝑎
#El valor de x1 se obtiene usando el signo + (más) en el numerador, y el valor de x2 se obtiene usando
#el signo – (menos). Desarrolle un programa que dados los valores de los coeficientes a, b y c (y
#suponiendo que a será diferente de cero) calcule y muestre las dos raíces x1 y x2 de la ecuación,
#incluso si las mismas son complejas. El programa debe permitir resolver más de una ecuación: al
#finalizar con una de ellas, el mismo programa debe preguntar al usuario si desea continuar con otra, y
#en ese caso cargar otro juego de coeficientes y volver a resolver.




#1. Complejo de cines
#Desarrollar un programa que permita procesar funciones de un complejo de cines.
#Por cada función se conoce: cantidad de espectadores y descuento (S/N).
#La carga termina cuando la cantidad de espectadores sea igual a 0 (cero).

#El programa deberá:

#a) Calcular la recaudación total del complejo,
# considerando que el valor de la entrada es de $50 en los días con descuento
# y $75 en los días sin descuento.

#b) Determinar cuántas funciones con descuento se efectuaron y qué porcentaje representan
# sobre el total de funciones.

recaudacion_sin = espectadores * 75
recaudacion_con = espectadores * 50

recaudacion_total = recaudacion_con + recaudacion_sin

funciones = 0
funciones_con_descuento = 0

espectadores = int(input('Ingrese la cantidad de espectadores: '))
descuento = input('Hubo descuento (si o no ): ')

while espectadores != 0:
    funciones += 1
    if descuento == 'si':
        recaudacion_con += 1
        funciones_con_descuento += 1
    else:
        recaudacion_sin += 1

    espectadores = int(input('Ingrese la cantidad de espectadores: '))
    descuento = input('Hubo descuento (si o no ): ')

print('\nLa recaudacion total fue de',recaudacion_total,
      '\nLa cantidad de funciones con descuento que se efectuaron fueron: ',funciones_con_descuento,
     )

porcentaje_sobre_total = funciones_con_descuento / funciones * 100

print('Representan el', porcentaje_sobre_total,'% del total de las funciones')




#SOLUCION CATEDRA


__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('COMPLEJO DE CINES')
print('*' * 80)

# Inicializar contadores y acumuladores
monto = 0
funciones = 0
funciones_dto = 0

# Primera carga de datos de corte antes del ciclo
espectadores = int(input('Espectadores (con 0 termina): '))

# Proceso repetitivo
while espectadores != 0:
    # Carga de datos que no determinan el corte del ciclo
    descuento = input('Descuento (S/N): ')
    # Definir precio
    if descuento == 'S':
        precio = 50
    else:
        precio = 75
    # Acumular monto recaudado por función
    monto = monto + (espectadores * precio)
    # Contar funciones con descuento y total de funciones
    if descuento == 'S':
        funciones_dto += 1
    funciones += 1
    # Nueva carga de datos de corte dentro del ciclo
    espectadores = int(input('Espectadores (con 0 termina): '))

# Resultados
print('*'*80)
print('Recaudación total $',monto)
if funciones != 0:
    porc = funciones_dto * 100 / funciones
else:
    porc = 0
print('Porcentaje de funciones con descuento:', porc,'%')


#2. Ventas por sucursal
#Ingresar una serie de números por teclado que representan la cantidad de ventas
# realizadas en las diferentes sucursales de un país de una determinada empresa.

#Los requerimientos funcionales del programa son:

#a) Informar la cantidad de ventas ingresadas.

#b) Total de ventas.

#c) Cantidad de ventas cuyo valor este comprendido entre 100 y 300 unidades.

#d) Cantidad de ventas con 400, 500 y 600 unidades.

#e) Indicar si hubo una cantidad de ventas inferior a 50 unidades.

#Usted deberá ingresar cantidades de ventas hasta que se ingrese un valor negativo.


ventas_ingresadas = 0
total_ventas = 0
ventas_100_300 = 0
ventas_400 = 0
ventas_500 = 0
ventas_600 = 0
menor_50 = False

ventas = int(input('Ingrese las ventas realizadas en las sucursales del pais: '))

while ventas > -1:
    ventas_ingresadas += 1
    total_ventas += ventas
    if  100 >= ventas <= 300:
        ventas_100_300 += 1
    elif 400 >= ventas < 500:
        ventas_400 += 1
    elif 500 >= ventas < 600:
        ventas_500 += 1
    else:
        ventas_600 += 1

    if ventas < 50:
        menor_50 = True

    ventas = int(input('Ingrese las ventas realizadas en las sucursales del pais: '))



print('\nLa cantidad de ventas ingresadas fue de ',ventas_ingresadas,
      '\nEl total de ventas es de ',total_ventas,
      '\nVentas comprendidas entre 100 y 300: ',ventas_100_300,
      '\nCantidad de ventas con 400 unidades: ', ventas_400,
      '\nCantidad de ventas con 500 unidades: ',ventas_500,
      '\nCantidad de ventas con 600 unidades: ',ventas_600,)

if menor_50 == True:
    print('Hubo una cantidad de ventas menor a 50')
else:
    print('No hubo una cantidad de ventas menor a 50')


#SOLUCION CATEDRA

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

cant_venta = 0
tot_venta = 0
cant_venta1 = 0
cont_venta400 = 0
cont_venta500 = 0
cont_venta600 = 0
hay_menor_50 = False

venta = int(input('Ingrese una cantidad de ventas (negativo para terminar): '))
while venta >= 0:
    # Permite ir contabilizando la cantidad de ventas
    cant_venta += 1
    # Permite acumular el total de ventas.
    tot_venta += venta

    # Permite contabilizar la cantidad de ventas entre 200 y 300 unidades.
    if (venta >= 100 and venta <= 300):
        cant_venta1 += 1
    # Permite contabilizar la cantidad de ventas con 400, 500 y 600 unidades.
    if venta == 400:
        cont_venta400 += 1
    if venta == 500:
        cont_venta500 += 1
    if venta == 600:
        cont_venta600 += 1

    #Determina si hubo una venta inferior a 50 unidades.
    if venta < 50:
        hay_menor_50 = True

    venta = int(input('Ingrese otra cantidad de ventas (0 cero para terminar): '))

print('La cantidad de ventas ingresadas fueron: ', cant_venta)
print('El total de ventas ingresadas fue:', tot_venta)
print('La cantidad de ventas comprendidas entre 200 y 300 unidades es:', cant_venta1)
print('La cantidad de ventas con 400 unidades es:', cont_venta400)
print('La cantidad de ventas con 500 unidades es:', cont_venta500)
print('La cantidad de ventas con 600 unidades es:', cont_venta600)

if hay_menor_50 == True:
    print ('Hubo al menos alguna venta con menos de 50 unidades')
else:
    print('No hubo venta con menos de 50 unidades')




#3. Promedio de números aleatorios
#Realice un programa que permita calcular el promedio de 1000 números aleatorios generados
# en el rango de [0, 100000]

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random

print('Calcular promedio de aleatorios')
print('=' * 80)

acumulador = 0
i = 0
while i < 1000:
    n = random.randint(0, 100000)
    acumulador += n
    i += 1
promedio = acumulador / i
print("El promedio es", promedio)

print("Fin del programa :)")




#4. Busqueda de mayor
#Realizar un programa que permita buscar el mayor de 10.000 números aleatorios generados
# en el rango de [0, 100.000].


__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random

print('Buscar el mayor de los valores')
print('=' * 80)

mayor = 0
i = 0
while i < 10000:
    n = random.randint(0, 100000)
    if mayor < n:
        mayor = n
    i += 1

print('El mayor valor de los 10000 numeros aleatorios es:', mayor)
print("Fin del programa :)")



#5. Menores y promedio
#Realizar un programa que genere 5000 numeros aleatorios en el rango de [0, 100000] y que permita:

#Determinar el menor de los numeros generados en forma aleatoria
#Calcular el valor promedio de los números menores a 10.000.

import random

menor = 0
i = 0

while i < 5000:
    n = random.randint(0, 10000)
    menor += n
    if menor > n:
        menor = n
    i += 1

print('El menor de los numeros generados es ', menor)


#SOLUCION CATEDRA

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

import random

menor = None
i = 0
suma = 0
cont = 0
while i < 5000:
    n = random.randint(0, 100000)
    if menor is None or menor > n:
        menor = n
    if n < 10000:
        suma += n
        cont += 1
    i += 1
if cont != 0:
    p = suma / cont
else:
    p = 0
print("El menor es", menor, "y el promedio de los menores a 10000 es:", p)




#6. Números pares e impares
#Se pide desarrollar un programa que permita leer una serie de números.
#La finalización de carga de datos se presenta cuando el usuario ingrese un número negativo.

#Los requerimientos funcionales del programa son:

#a) La sumatoria de solo los números que estén comprendidos entre 50 y 100.

#b) Cantidad de valores pares ingresados.

#c) Cantidad de valores impares ingresados.

#d) Informar si en la carga de números se ingreso al menos un número 0.

#e) Informar si la serie contiene solo números pares e impares alternados

numeros = 0
num_50_100 = 0
numeros_pares = 0
numeros_impares = 0
numero_cero = False

serie_num = int(input('Ingrese un numero: '))

while serie_num >= 0:
    numeros += 1
    if serie_num >= 50 and serie_num <= 100:
        num_50_100 += serie_num

    if serie_num % 2 == 0:
        numeros_pares += 1
    else:
        numeros_impares += 1

    if serie_num == 0:
        numero_cero = True

    if numeros_pares > 0  and numeros_impares > 0:
        contiene = 'La serie contiene numeros pares e impares'
    elif numeros_pares > 0 and numeros_impares == 0:
        contiene = 'La serie solo contiene numeros pares'
    else:
        contiene = 'La serie solo contiene numeros impares'

    serie_num = int(input('Ingrese un numero: '))

print('\nLa sumatoria de numeros ingresados entre 50 y 100 es',num_50_100,
      '\nNumeros pares ingresados: ',numeros_pares,
      '\nNumeros impares: ',numeros_impares,
      '\n',contiene)

if numero_cero == True:
    print('Se ingreso al menos un numero cero')


#SOLUCION CATEDRA

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Procesamiento de Numeros Pares e Impares')

sumatoria = 0
cantidad_pares = 0
cantidad_impares = 0
ingreso_cero = False
anterior = -1
alternan = True

numero = int(input('Ingrese un numero (finaliza cuando ingrese un numero negativo): '))
while numero >= 0:
    if 50 < numero < 100:
        sumatoria += numero

    paridad = numero % 2
    if paridad == 0:
        cantidad_pares += 1
    else:
        cantidad_impares += 1

    if numero == 0:
        ingreso_cero = True

    if anterior == paridad:
        alternan = False
    anterior = paridad
    numero = int(input('Ingrese otro numero a procesar: '))

print('Resultados')
print('=' * 80)
print('La sumatoria de los numeros comprendidos entre 50 y 100 fue de', sumatoria)
print('La cantidad de numeros pares procesados fue de', cantidad_pares)
print('La cantidad de numeros impares procesados fue de', cantidad_impares)
if ingreso_cero:
    print('El usuario al menos ingreso un numero cero en la secuencia')

if alternan:
    print('La secuencia tiene numeros pares e impares alternados')
else:
    print('La secuencia no tiene numeros pares e impares alternados')



#7. Censo
#Desarrollar un programa que permita procesar los datos del último censo de una pequeña población.

#Por cada habitante se ingresa: sexo (M/F) y edad.
#La carga de datos finaliza al ingresar cualquier otro valor para sexo.

#El programa debe informar:

#a) A qué sexo corresponde la mayor cantidad de habitantes (considerar que puede ser igual)

#b) Cantidad de mujeres en edad escolar (4 a 18 años inclusive)

#c) Si hay algún varón que supere los 80 años de edad

masculino = 0
femenino = 0
mujeres_edad_escolar = 0
hombre_80 = False

sexo = input('Ingrese el sexo(M/F): ')

while sexo == 'M' or sexo == 'F':
    edad = int(input('Ingrese la edad: '))
    if sexo == 'M':
        masculino += 1
    else:
        femenino += 1
    if sexo == 'F' and 4 < edad <= 18:
        mujeres_edad_escolar += 1
    if sexo == 'M' and edad >= 80:
        hombre_80 = True

    sexo = input('Ingrese el sexo(M/F): ')

if masculino > femenino:
    cantidad = 'La mayor cantidad de habitantes corresponde a el sexo masculino'
elif masculino == femenino:
    cantidad = 'Hay igualdad entre hombre y mujer en el sexo de los habitantes'
else:
    cantidad = 'La mayor cantidad de habitantes corresponde al sexo femenino'

print(cantidad,'\nLa cantidad de mujeres en edad escolar es', mujeres_edad_escolar)

if hombre_80 == True:
    print('Hay al menos un hombre que supera los 80 años de edad')



#SOLUCION CATEDRA
#CON CONECTORES LOGICOS

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('CENSO POBLACIONAL')
print('*' * 80)

# Inicializar contadores y acumuladores
cant_hombres = 0
cant_mujeres = 0
cant_escolares = 0
hay_mayores80 = False

# Primera carga de datos de corte antes del ciclo
sexo = input('Ingrese sexo (M/F - Otro valor termina): ')

# Proceso repetitivo
while sexo == 'M' or sexo == 'F':
    # Carga de datos que no determinan el corte del ciclo
    edad = int(input('Ingrese edad: '))
    # Contar hombres y mujeres
    if sexo == 'M':
        cant_hombres += 1
    else:
        cant_mujeres += 1
    # Contar mujeres en edad escolar
    if sexo == 'F' and edad >= 4 and edad <= 18:
        cant_escolares += 1
    # Detectar hombres de más de 80 años
    if sexo == 'M' and edad > 80:
        hay_mayores80 = True
    # Nueva carga de dato de corte dentro del ciclo
    sexo = input('Ingrese sexo (M/F - Otro valor termina): ')

# Resultados
print('*' * 80)
if cant_hombres > cant_mujeres:
    print('Hay más hombres que mujeres')
elif cant_mujeres > cant_hombres:
    print('Hay más mujeres que hombres')
else:
    print('La cantidad de mujeres y hombres es igual')
print('Las mujeres en edad escolar son:', cant_escolares)
if hay_mayores80 == True:
    print('Hay hombres mayores a 80 años')
else:
    print('NO hay hombres mayores a 80 años')


#SOLUCION CON CONDICIONES ANIDADAS

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('CENSO POBLACIONAL')
print('*' * 80)

# Inicializar contadores y acumuladores
cant_hombres = 0
cant_mujeres = 0
cant_escolares = 0
hay_mayores80 = False

# Primera carga de datos de corte antes del ciclo
sexo = input('Ingrese sexo (M/F - Otro valor termina): ')

# Proceso repetitivo
while sexo == 'M' or sexo == 'F':
    # Carga de datos que no determinan el corte del ciclo
    edad = int(input('Ingrese edad: '))
    # Proceso
    if sexo == 'M':
        cant_hombres += 1
        if edad > 80:
            hay_mayores80 = True
    else:
        cant_mujeres += 1
        if edad >= 4 and edad <= 18:
            cant_escolares += 1
    # Nueva carga de dato de corte dentro del ciclo
    sexo = input('Ingrese sexo (M/F - Otro valor termina): ')

# Resultados
print('*' * 80)
if cant_hombres > cant_mujeres:
    print('Hay más hombres que mujeres')
elif cant_mujeres > cant_hombres:
    print('Hay más mujeres que hombres')
else:
    print('La cantidad de mujeres y hombres es igual')
print('Las mujeres en edad escolar son:', cant_escolares)
if hay_mayores80 == True:
    print('Hay hombres mayores a 80 años')
else:
    print('NO hay hombres mayores a 80 años')




#8. Mayor numero en orden par
#Ingresar de a uno una serie de números. Encontrar e imprimir el mayor de todos los números pares
#cuyo número de orden sea par,
#el proceso terminará cuando el número leído sea igual a cero


__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Busqueda del mayor par de orden par')
print('=' * 80)

orden = 0
mayor = None

numero = int(input('Ingrese un numero (finaliza cuando ingrese 0): '))

while numero != 0:
    # Si es número par en orden par,
    if orden % 2 == 0 and numero % 2 == 0:
        # se busca el mayor
        if mayor is None or numero > mayor:
            mayor = numero
    orden += 1
    numero = int(input('Ingrese otro numero: '))

if not mayor is None:
    print('El mayor numero par ingresado en orden par es', mayor)
else:
    print('No se ingresaron números pares en orden par')





#9. Comisión de Vendedores
#Una empresa debe calcular el total de comisiones que debe abonar por ventas realizadas por sus vendedores,
#para ello le solicita un sistemita que le permita calcular dicho montos.

#Se tiene conocimiento que la empresa tiene cuatro categorías de vendedores (1 a 4).
#Usted debe solicitar el ingreso de la categoría del vendedor y el total de la venta
#(el proceso termina cuando se ingrese una categoría igual a cero)
#y acumular las comisiones de las ventas rendidas por los vendedores
#de diferentes en base a los siguientes cálculos:

#a) Categoría 1: cobra una comisión de 10%
#b) Categoría 2: cobra una comisión de 25%
#c) Categoría 3: cobra una comisión de 30%
#d) Categoría 4: cobra una comisión de 40%

#Una vez procesadas todas las ventas mostrar el total de comisiones a pagar por cada categoría
#de vendedores que tiene la empresa junto con el total general

comision_1 = 0
comision_2 = 0
comision_3 = 0
comision_4 = 0

categoria = int(input('Ingrese una categoria (1 - 4) - (termina con 0): '))

while categoria != 0:
    total_venta = float(input('Ingrese el total de la venta: '))
    if categoria == 1:
        comision = total_venta * 10 / 100
        comision_1 += comision
    elif categoria == 2:
        comision = total_venta * 20 / 100
        comision_2 += comision
    elif categoria == 3:
        comision = total_venta * 30 / 100
        comision_3 += comision
    else:
        comision = total_venta * 40 / 100
        comision_4 += comision

    categoria = int(input('Ingrese una categoria (1 - 4) - (termina con 0): '))

suma = comision_1 + comision_2 + comision_3 + comision_4
total = round(suma, 2)

print('\nEl total a pagar a la comision uno es ',comision_1,
      '\nEl total a pagar a la comision dos es ',comision_2,
      '\nEl total a pagar a la comision tres es ',comision_3,
      '\nEl total a pagar a la comision cuatro es ',comision_4,
      '\nEl total general a pagar es ',total)

#SOLUCION CATEDRA

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Sistema de Calculo de Comisiones a Vendedores')
print('*' * 80)

tot_cat_1 = 0
tot_cat_2 = 0
tot_cat_3 = 0
tot_cat_4 = 0

print('Inicio de calculo de comision, al entrar una categoria igual a 0 el proceso termina')
categoria = int(input('Ingrese la categoria de vendedor (1-4): '))

while categoria != 0:
    venta = float(input('Ingrese el total vendido por este vendedor: '))

    if categoria == 1:
        tot_cat_1 += venta * 0.10
    elif categoria == 2:
        tot_cat_2 += venta * 0.25
    elif categoria == 3:
        tot_cat_3 += venta * 0.30
    else:
        tot_cat_4 += venta * 0.40

    categoria = int(input('Ingrese una nueva categoria de vendedor (1-4): '))

total = tot_cat_1 + tot_cat_2 + tot_cat_3 + tot_cat_4

print('Resultados de comisiones calculadas')
print('*' * 80)
print('El total de comisiones a pagar para la categoria 1 es de $', tot_cat_1, sep='')
print('El total de comisiones a pagar para la categoria 2 es de $', tot_cat_2, sep='')
print('El total de comisiones a pagar para la categoria 3 es de $', tot_cat_3, sep='')
print('El total de comisiones a pagar para la categoria 4 es de $', tot_cat_4, sep='')
print('El total de comisiones a pagar es de $', total, sep='')




'''


#10. Proceso de Discriminantes
#Un matemático desea un simple programa que le permita cargar una serie de números
#que representan los discriminantes de diferentes ecuaciones de segundo grado,
#el proceso de la secuencia finaliza cuando el matemático no desea seguir cargando discriminantes.
#Usted debe:

#a) Determinar la cantidad de discriminantes que darán 2 raíces
#b) Determinar la cantidad de discriminantes que darán una única raíz
#c) Determinar la cantidad de discriminantes que daran raíces en el campo de los números imaginarios
#d) Indicar el porcentaje que representa el punto c sobre el total de discriminantes procesados
#por el matemático


