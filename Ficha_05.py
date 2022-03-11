'''
#Cargar por teclado tres números enteros y determinar y mostrar el mayor de ellos. No
#utilice para el proceso la función max() de la librería estándar de Python: diseñe el algoritmo
#suponiendo que tal función no existe en el lenguaje que usará para el desarrollo del programa.

n1 = int(input('Ingrese un numero: '))
n2 = int(input('Ingrese un numero: '))
n3 = int(input('Ingrese un numero: '))

if n1 > n2 and n1 > n3:
    may = n1
else:
    if n2 > n1 and n2 > n3:
        may = n2
    else:
        may = n3

print('El mayor es', may)


#Una compañía de alquiler de automóviles necesita un programa que calcule lo que se
#debe cobrar a cada cliente, teniendo en cuenta el kilometraje recorrido por el cliente al devolver el
#automóvil:
#i. Si el cliente no superó los 300 km recorridos se deberá cobrar $500.
#ii. Para recorridos desde más de 300 km y hasta no más de 1000 km se le cobrará $500 más el
#kilometraje excedente a los 300, a razón de $3 por kilómetro.
#iii. Para recorridos mayores a 1000 km se le cobrará $500 más el kilometraje excedente a los
#300, a razón de $1.5 por kilómetro.

km_recorridos = int(input('Ingrese el km recorrido: '))
excedente = km_recorridos - 300

if km_recorridos <= 300:
    cobrar = 500

else:
    if km_recorridos > 300 and km_recorridos <= 1000:
        cobrar = 500 + 3*excedente

    else:
        cobrar = 500 + 1.5*excedente

print('Debe cobrarse ', cobrar)


#Se cargan por teclado las notas obtenidas por un estudiante en tres parciales
#realizados durante el cursado de una materia universitaria. Además, se carga la nota final que ese
#estudiante obtuvo en el desarrollo de los trabajos prácticos en esa misma materia. Se sabe que al
#terminar el cursado de la materia, todo alumno puede quedar en uno de los siguientes estados
#académicos:
#a. Libre: si no llegó a cumplir con las condiciones para ser Regular.
#b. Regular: si aprobó al menos dos de los tres parciales con nota de 4 o más y además obtuvo
#nota de 4 o más en la nota final de trabajos prácticos.
#c. Promocionado: si aprobó los tres parciales con nota de 7 o más pero con promedio entre ellos
#de 8(ocho) o más, y además obtuvo nota de 8 o más en la nota final del práctico.
#d. Aprobado: si aprobó los tres parciales con nota de 7 o más pero con promedio entre ellos de
#9(nueve) o más, y además obtuvo nota de 8 o más en la nota final del práctico.
#El programa debe determinar y mostrar por pantalla el estado en que finalmente quedó el estudiante.

nota1 = int(input('Ingrese la nota uno (cargue 0 si no hizo el parcial): '))
nota2 = int(input('Ingrese la nota dos (cargue 0 si no hizo el parcial): '))
nota3 = int(input('Ingrese la nota tres (cargue 0 si no hizo el parcial): '))
nota_final_tp = int(input('Ingrese la nota final de trabajos praticos (cargue 0 si no hizo el tp): '))

parciales_aprobados = 0

if nota1 >= 4:
    parciales_aprobados += 1
if nota2 >= 4:
    parciales_aprobados += 1
if nota3 >= 4:
    parciales_aprobados += 1


notas_ok = False

if nota1 >= 7 and nota2 >= 7 and nota3 >= 7 and nota_final_tp >= 8:
 notas_ok = True

promedio_parciales = (nota1 + nota2 + nota3) / 3

condicion = 'Regular'

if parciales_aprobados < 2 or nota_final_tp < 4:
 condicion = 'Libre'
elif notas_ok and promedio_parciales >= 9:
 condicion = 'Aprobado'
elif notas_ok and promedio_parciales >= 8:
 condicion = 'Promocionado'

print('Condicion final del estudiante:', condicion)


#Se cargan por teclado tres números. Se pide mostrarlos en pantalla, ordenados de
#menor a mayor.

n1 = int(input('Cargue un numero: '))
n2 = int(input('Cargue un numero: '))
n3 = int(input('Cargue un numero: '))

if n1 > n2:
    menor, mayor = n2, n1
else:
    menor, mayor = n1, n2

if n3 > mayor:
    medio, mayor = mayor, n3

elif n3 > menor:
    menor = n3

else:
    medio, menor = menor, n3

print('El mayor es:',mayor,'\nEl medio es:',medio,'\nEl menor es:',menor)
'''


#1. Operaciones de orden con 3 nros.
#Realizar un programa que tome tres números, los ordene de mayor a menor,
#y diga si el tercero es el resto de la división de los dos primeros.


#2. Elecciones Presidenciales
#Según la Ley Electoral de la República Argentina, el Presidente y el Vicepresidente
# se eligen de acuerdo a las siguientes reglas:

#Artículo 149. — Resultará electa la fórmula que obtenga más del cuarenta y cinco por ciento (45 %) de los votos afirmativos válidamente emitidos;
#en su defecto, aquella que hubiere obtenido el cuarenta por ciento (40 %) por lo menos de los votos afirmativos válidamente emitidos y, además,
#existiere una diferencia mayor de diez puntos porcentuales respecto del total de los votos afirmativos válidamente emitidos,
#sobre la fórmula que le sigue en número de votos.

#Artículo 150. — Si ninguna fórmula alcanzare esas mayorías y diferencias de acuerdo al escrutinio ejecutado por las Juntas Electorales,
#y cuyo resultado único para toda la Nación será anunciado por la Asamblea Legislativa atento lo dispuesto por el artículo 120 de la presente ley,
#se realizará una segunda vuelta dentro de los treinta (30) días.

#Artículo 151. — En la segunda vuelta participarán solamente las dos fórmulas más votadas en la primera,
#resultando electa la que obtenga mayor número de votos afirmativos válidamente emitidos.

#Desarrollar un programa que permita ingresar,
#para los 3 partidos más votados: fórmula (presidente + vice) y cantidad de votos obtenidos.

#Luego determinar:

#Qué fórmula obtuvo el mayor porcentaje.
#Si la fórmula resulta elegida o se requiere segunda vuelta.
#En este caso, indicar también quienes participan de la segunda vuelta.



#3. Mantenimiento Informático
#El Área de Mantenimiento de un laboratorio informático nos ha solicitado
#el desarrollo de un programa que facilite la gestión de las tareas realizadas en el día.

#El usuario debe ingresar de tres equipos informáticos (PC)
#los siguientes datos: número de identificación de la PC,
#tiempo de reparación (expresado en minutos)
#y la causa de mantenimiento (1- Problema de Hardware 2-Problema de Software)

#Los requerimientos funcionales son:

#a)  ¿Cuál es el tiempo total de las tareas de mantenimiento?

#b)  ¿Cuál es la PC (Número de identificación) que tuvo mayor tiempo en tareas de mantenimiento?

#c)  Tiempo promedio de tareas de mantenimiento.

#d)  Informar con un mensaje si todas las PC (Número de identificación) que se les ha realizado mantenimiento tuvieron problemas de Hardware.


#4. Observatorio meteorológico
#Un observatorio meteorológico ha tomado el registro de temperaturas en distintos momentos del día. Se solicita el desarrollo de un programa que facilite información estadísticas de ellas.

#El usuario debe ingresar cuatro valores de temperatura (considerar que son valores enteros).

#Los requerimientos funcionales son:

#a) Promedio de temperatura diaria.

#b) Temperatura máxima.

#c) Temperatura mínima.

#d) Informar con un mensaje si algunas de las temperaturas supera a la temperatura promedio.




#5. Menú de Opciones Básico
#Diseñar un programa que según la opción ingresada por el usuario permita realizar las siguientes operaciones:

#Si la opción es 1 mostrar la superficie de un triángulo. Para calcular la superficie debe usarse la fórmula de Herón:

#Si la opción ingresada es 2 mostrar el perímetro del triángulo.
#Si la opción ingresada es 3 informar la longitud del lado menor.
#Si la opción ingresada no fue ni 1, 2 o 3 informar un mensaje de error.
#Para ello usted deberá ingresar por teclado el número de opción y el valor de los tres lados del triángulo.




#6. Institución Educativa
#Una institución educativa necesita un programa que facilite la gestión de cupos de los cursos de primer grado. Ingresar tres grados. De cada grado se ingresa el código de identificación (Ejemplo 1A, 1B, ...) y la cantidad de niños y de niñas y cupo máximo (que es el mismo para los tres cursos).

#Los requerimientos funcionales son:

#a)  Código de identificación del curso que tenga menos alumnos inscriptos.

#b)  Porcentaje de niñas de cada curso.

#c)  Porcentaje de niños de cada curso.

#d)  Promedio general de alumnos.

#e) Si algunos de los tres grados supera el cupo máximo informar un mensaje la necesidad de apertura de una nueva división.




#7. Juego de Dados: Pares e Impares
#Desarrollar un programa para simular un juego de dados con las siguientes reglas:

#Participan 3 jugadores: el campeón y 2 retadores.
#Antes de comenzar el juego, se debe ingresar el récord del campeón.
#En las dos primeras rondas, compiten sólo los retadores: se lanzan 2 dados.
#Si la suma de ambos es impar, gana el retador 1; si no, gana el retador 2.
#Primera ronda: el ganador obtiene tantos puntos como indica la suma de los dados
#Segunda ronda: a los puntos de la primera ronda,
#el ganador suma tantos puntos como indique el dado de mayor valor,
#y al perdedor se le restan tantos puntos como indique el dado de menor valor
#Ronda final: se suma a la competencia el campeón actual,
#que participa con un puntaje equivalente a su récord.
#Se pide:

#Mostrar en cada ronda el valor de los dados y los puntajes de cada retador.
#Si ninguno de los retadores supera al campeón, este mantiene su puesto.
#En caso contrario, el que obtenga mayor puntaje será el ganador.
#Al terminar, informar si alguno de los retadores llegó a tener más puntos que el record.



#8. Juego del Punto
#La idea general del Juego del Punto, es lograr el máximo puntaje en 4(cuatro) vueltas de lanzamiento de 3 dados,
#y a continuación enumeramos las reglas en base a las cuales se obtiene puntaje:

#1.) Cada jugador dispone de 4(cuatro) tiradas o lanzamientos para lograr su objetivo, el programa solo deberá simular de a una tirada por vez.

#2.) En cada tirada se lanzan 3(tres) dados. Sólo suman puntaje los dados que salgan con un punto en el centro (esto es: el 1, el 3 y el 5)
#(y de allí el nombre del juego). El puntaje de la tirada se calcula sumando el aporte de cada dado, de acuerdo a  las siguientes  pautas:

#Si sale el 1, se suma 1(un) punto (el único que muestra el dado).
#Si sale el 3, se suman 2(dos) puntos (porque a los costados del punto central hay dos puntos).
#Si sale el 5, se suman 4(cuatro) puntos (porque en este caso, hay cuatro puntos a los costados del central).
#Si sale un número par (2, 4 o 6) no se suma ningún punto (porque ese dado no tiene punto central).
#3.) Si en alguna de las tiradas el jugador saca tres números pares iguales,
#entonces el jugador duplicará los puntos finales que haya sumado al terminar sus cuatro lanzamientos.

#Se pide: que en base a todo lo indicado, se genere un programa que simule 1 tirada de los 3 dados
#y luego habiendo solicitado al usuario que cargue su puntaje previo,
#informe su puntaje acumulado en el caso de haber obtenido puntos,
#su puntaje previo y el mensaje de que duplica puntos si salieron los 3 pares o simplemente su puntaje previo si no sumó ningún punto.




#9. ¿Piedra, Papel o Tijera?
#Desarrollar un programa que permita al usuario jugar contra la computadora el clásico “Piedra, Papel o Tijera” y determine cuál de ellos es el ganador.

#Las reglas son:

#La piedra aplasta (o rompe) la tijera. (Gana la piedra).
#La tijera corta el papel. (Gana la tijera).
#El papel envuelve la piedra. (Gana el papel)
#Si los dos jugadores eligen el mismo elemento, empatan.





#10. Impuesto Automotor
#Crear un programa que permita calcular los impuestos que debe pagar un auto,
#conociendo su modelo (año de fabricación) y tipo (P: Particular/T: Taxi/R: Remis). Para calcular los impuestos, tener en cuenta que:

#a. Los autos particulares de menos de 10 años de antigüedad pagan $200, entre 10 y 20 años pagan $150 y no pagan impuestos los que tienen más de 20 años.

#b. Los taxis pagan impuestos como auto particular, más $150 por la licencia de taxi.

#c. Los remises pagan $100 por cada año de antigüedad de su vehículo.





#11. Calculo de Regularidad
#La facultad pide un simple programa que pida las tres notas de un alumno en cualquier materia y mostrar si el alumno esta libre,
#regular o promocionado. Las tres notas son los dos parciales mas la nota de prácticos y las condiciones de regularidad están descriptas a continuacón:

#El promedio menor a 4 el alumno esta libre.
#El promedio comprendido entre 4 y 8 el alumno esta regular.
#El promedio mayor a 8 el alumno está promocionado.


#12. Punto en el plano
#Se pide realizar un programa que ingresando el valor x e y de un punto determine a que cuadrante pertenece en el sistemas de coordenadas.


#13. Postulantes a un empleo
#Se tienen los datos de tres postulantes a un empleo a los que se les realizó un test de capacitación. Por cada postulante se tiene la siguiente información: nombre del postulante, cantidad total de preguntas que se le realizaron y cantidad de preguntas que contestó correctamente.

#Se pide confeccionar un programa que lea los datos de los tres postulantes, informe el nivel de cada uno según los criterios de aprobación que se indican mas abajo, e indique finalmente el nombre del postulante que ganó el puesto. Los criterios de aprobación son los siguientes, en función del porcentaje de respuestas correctas sobre el total de preguntas realizadas a cada postulante:

#     Nivel Superior:       Porcentaje >= 90%
#     Nivel Medio:          75% <= Porcentaje < 90%
#     Nivel Regular:        50% <= Porcentaje < 75%
#     Fuera de Nivel:       Porcentaje < 50%


#14. Comercio
#Un comerciante tiene a la venta 3 tipos de artículos principales.
#Conociendo la cantidad vendida de cada artículo y el precio unitario de cada artículo,
#hacer un programa que determine cuál fue el producto que realizó el mayor aporte en los ingresos
#y el porcentaje que dicho aporte significa en el ingreso absoluto de los 3 artículos sumados. Ese porcentaje se calcula así:

#Absoluto    ____________  100%

#Mayor aporte   _________     x %

#Por lo tanto:    x = mayor aporte  *  100 / absoluto


#15. Pago a un Proveedor
#Un comercio necesita informar el importe final a pagar a un determinado proveedor.
#Para ello debe ingresar la categoría (que puede ser categoría 'A' o 'B') y el importe original a abonar.

#Considerar las siguientes condiciones para el cálculo del importe final a pagar:

#Si el cliente es categoría A y el monto a pagar supera a los 1000 pesos debe aplicarse un descuento del 5%.
#Si el cliente es categoría B y el importe a pagar oscila entre 1500 y 2500 pesos debe aplicarse un descuento del 2%.
#Para ambas categorías en caso de no cumplirse las condiciones especificadas no se aplicará ningún tipo de descuento sobre el importe que se le debe abonar.


#16. Raíces de un polinomio de segundo grado
#Realizar un programa que permita calcular las raíces de un polinomio de segundo grado y mostrar un mensaje indicando si son reales o imaginarias.
#Si son reales distintas, mostrar sus dos valores, si son reales iguales, mostrar solo una.

#Ayudita: A partir del discriminante ?,
#es posible determinar la naturaleza de las raíces de la ecuación (considerando coeficientes reales) y se pueden presentar 3 situaciones:

#•  Si ? es negativo, ambas raíces son números complejos.

#•  Si ? es igual a cero, existen dos raíces reales e iguales, por lo tanto hay una solución.

#•  Si ? es positivo, ambas raíces son reales y distintas.


#17. Índice de Masa Corporal
#Realice un programa que le permita calcular el Índice de Masa Corporal (IMC) de una persona en función de su peso (en kgs.) y su altura (en mts.),
#sabiendo que el IMC es igual al peso dividido la altura al cuadrado.
#En función del valor del IMC, el programa debe mostrar por pantalla el diagnóstico resultante del análisis del índice según las siguientes situaciones:

#Si  el IMC es menor o igual a 16: “Necesita asistencia de un médico, los riesgos para su salud son muy altos”.
#Si el IMC es menor o igual a 17: "Usted tiene infrapeso, aliméntese más".
#Si el IMC es menor o igual a 18: "Usted tiene bajo peso, aliméntese mejor".
#Si el IMC es mayor a 18 y menor o igual a 26: "Usted tiene un peso saludable, continúe así!".
#Si el IMC es mayor a 26 y menor a 30: "Tiene sobrepeso de grado I, hoy es un buen día para empezar a hacer ejercicios".
#Si  el IMC es mayor o igual a 30 y menor o igual a 35: "Tiene obesidad de grado II, necesita el apoyo de un plan nutricional".
#Si  el IMC es mayor a 35 y menor o igual a 40: "Tiene obesidad grado III (pre-mórbida), consulte con su médico los riesgos para su salud".
#Si  el IMC es mayor a 40: "Usted tiene obesidad de grado IV (mórbida), los riesgos para su salud son muy altos, consulte con su médico a la brevedad”.


#18. Lluvias
#En una localidad nos piden que realicemos un análisis de las lluvias caídas en un trimestre (3 cantidades).

#Para ello se debe ingresar por teclado la cantidad de milímetros caídos por mes y con dichos datos resolver lo siguiente:

#Promedio de milímetros caídos.
#Cantidad de meses con más o igual lluvia que el promedio.
#Mes con menos lluvias en el trimestre.
#Si dicho mes tuvo 0 mm caídos indicar con un mensaje.


#19. Premio por Ventas (*)
#Para calcular el premio de un vendedor, se ingresan 3 montos correspondientes a sus ventas mensuales del último trimestre.

#El premio es equivalente al 50% del menor monto vendido. Si además todos los montos superan los $1000, se agrega un 10% adicional al premio calculado.

#(*) Ejercicio tipo parcial


#20. Análisis Estadístico
#Para un análisis estadístico, se pide ingresar 3 valores y determinar:

#Si alguno de los valores es múltiplo de 5
#Si todos ellos son impares
#Si el mayor de ellos supera a la suma de los otros 2

valor1 = int(input('Ingrese el valor uno: '))
valor2 = int(input('Ingrese el valor dos: '))
valor3 = int(input('Ingrese el valor tres: '))

if valor1 % 5 == 0 or valor2 % 5 == 0 or valor3 % 5 == 0:
    multiplo5 = 'Hay al menos un valor que es multiplo de cinco'
else:
    multiplo5 = 'No hay ningun valor que sea multiplo de cinco'

if valor1 % 2 != 0 and valor2 % 2 != 0 and valor3 != 0:
    paridad = 'Son todos impares'
else:
    paridad = 'No son todos impares'

maximo = max(valor1, valor2, valor3)

valores = valor1 + valor2 + valor3

suma_dos = valores - maximo

if maximo > suma_dos:
    sumatoria_otros_dos = 'El valor maximo supera a la suma de los otros dos'
else:
    sumatoria_otros_dos = 'El valor maximo no supera el valor de los otros dos'

print('\n',multiplo5,'\n',paridad,'\n',sumatoria_otros_dos)


#SOLUCION CATEDRA

__author__ = 'Catedra Algoritmos y Estructuras de Datos'

print("Análisis Estadístico")

num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))
num3 = int(input("Ingrese el tercer valor: "))

multiplo_5 = False
if num1 % 5 == 0 or num2 % 5 == 0 or num3 % 5 == 0:
    multiplo_5 = True

todos_impares = False
if num1 % 2 == 1 and num2 % 2 == 1 and num3 % 2 == 1:
    todos_impares = True

if num1 > num2 and num1 > num3:
    may = num1
    #otro1 = num2
    #otro2 = num3
    suma = num2 + num3
else:
    if num2 > num3:
        may = num2
        #otro1 = num1
        #otro2 = num3
        suma = num1 + num3
    else:
        may = num3
        #otro1 = num1
        #otro2 = num2
        suma = num1 + num2

supera_suma = False
#suma = otro1 + otro2
if may > suma:
    supera_suma = True


if multiplo_5:
    print("Al menos uno de los valores es múltiplo de 5")
else:
    print("Ningún valor es múltiplo de 5")

if todos_impares:
    print("Todos los valores son impares")
else:
    print("No todos los valores son impares")

if supera_suma:
    print("El mayor de los valores supera la suma de los otros dos")
else:
    print("El mayor de los valores no supera la suma de los otros dos")



#21. Análisis Estadístico (*) - Variante
#Para un análisis estadístico, se pide ingresar 3 valores y determinar:

#Si alguno de los valores es múltiplo de 5
#Cuántos de los valores son impares
#Si el mayor de ellos supera a la suma de los otros 2
#(*) Ejercicio tipo parcial


__author__ = 'Catedra Algoritmos y Estructuras de Datos'

print('ANALISIS ESTADISTICO')

# Ingreso de datos
val1 = int(input('Ingrese 1er valor: '))
val2 = int(input('Ingrese 2do valor: '))
val3 = int(input('Ingrese 3er Valor: '))

# Alguno es multiplo de 5?
algun_multiplos_5 = 'NO'
if val1 % 5 == 0 or val2 % 5 == 0 or val3 % 5 == 0:
    algun_multiplos_5 = 'SI'

# Contar impares
cant_impares = 0
if val1 % 2 != 0:
    cant_impares += 1
if val2 % 2 != 0:
    cant_impares += 1
if val3 % 2 != 0:
    cant_impares += 1

# El mayor supera a la suma de los otros dos?
if val1 > val2 and val1 > val3:
    may = val1
    suma = val2 + val3
elif val2 > val3:
    may = val2
    suma = val1 + val3
else:
    may = val3
    suma = val1 + val2

if may > suma:
    mensaje_may = 'Supera'
else:
    mensaje_may = 'No supera'
mensaje_may = mensaje_may + ' a la suma de los otros dos.'

# Resultados
print('-' * 50)
print(algun_multiplos_5, 'hay algun multiplo de 5')
print('Hay', cant_impares, 'valores impares')
print('El valor mayor es', may, '.', mensaje_may)


#22. Votación en el Senado (*)
#Se vota una ley en el Senado, y se ingresan votos a favor, en contra y abstenciones
#de los senadores presentes.

#Informar cuál fue el resultado de la votación.
# Si la ley fue aprobada, indicar si fue por mayoría absoluta (más del 50% de los votos)
# o por mayoría simple.

#Por último, considerando que la Cámara está formada por 72 senadores,
# determinar cuantos se encontraban ausentes.

#(*) Ejercicio tipo parcial



