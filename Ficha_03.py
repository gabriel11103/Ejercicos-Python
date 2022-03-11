"""
#La fuerza de atracción entre dos masas m1 y m2 separadas por una distancia d, está
#dada por la siguiente fórmula2 de la mecánica clásica:
#F=G*(m1*m2)/d**2

G = 6.673 * pow(10,-8)

print('Ejemplo 4 - Cálculo de la fuerza de atracción')
m1 = float(input('Masa del primer cuerpo: '))
m2 = float(input('Masa del segundo cuerpo: '))
d = float(input('Distancia entre ambos: '))

f = (G * m1 * m2) / d**2

print('Fuerza de atracción:', f)


#La dirección de la carrera de Ingeniería en Sistemas de la UTN Córdoba necesita un
#programa que permita cargar el nombre de un estudiante de quinto año, el nombre del profesor
#responsable de la Práctica Profesional Supervisada de ese estudiante, y el promedio general (con
#decimales) del estudiante en su carrera. Una vez cargados los datos, se pide simplemente mostrarlos
#en la consola de salida a modo de verificación, pero de forma que el nombre del practicante vaya
#precedido de la cadena "est." y el nombre del profesor supervisor se preceda con "prof.". El promedio
#del alumno debe mostrarse redondeado, sin decimales, en formato entero.

print('Ejemplo 6 - Datos de Práctica Profesional Supervisada')
nom_est_orig = input('Nombre del estudiante: ')
prom_orig = float(input('Promedio general: '))
nom_pro_orig = input('Nombre del profesor: ')

nom_est_final = 'est. ' + nom_est_orig
nom_pro_final = 'prof. ' + nom_pro_orig
prom_final = round(prom_orig)

print('Practicante:', nom_est_final, '\t-\tPromedio:', prom_final)
print('Supervisor:', nom_pro_final)


#Una pequeña oficina de correos dispone de cinco casillas o boxes para guardar las
#cartas que debe despachar. Cada casilla (que puede contener muchas cartas) está numerada con
#números correlativos del 0 al 4. Cada carta que se recibe tiene un código postal numérico, y en base a
#ese código el despachante debe determinar en qué box guardará la carta, pero de tal forma que el
#mismo sistema sirva luego para saber en qué caja buscar una carta, dado su código postal. Diseñe un
#esquema de distribución que permita cumplir este requerimiento, cargando por teclado el código
#postal de tres cartas y mostrando en qué casilla será almacenada cada una.

n = 5

print('Ejemplo 7 - Distribución de cartas')
c1 = int(input('Primer código postal: '))
c2 = int(input('Segundo código postal: '))
c3 = int(input('Tercer código postal: '))

n1 = c1 % n
n2 = c2 % n
n3 = c3 % n

print('Código postal:', c1, '\tasignado al box: ', n1)
print('Código postal:', c2, '\tasignado al box: ', n2)
print('Código postal:', c3, '\tasignado al box: ', n3)

#se solicita la creacion de un programa para calcular de ladrillos/bloques necesarios para
#la construccion de un muro o pared

ancho_mezcla = 2.5

alto_pared = int(input('Ingrese el alto de la pared: '))
largo_pared = int(input('Ingrese el largo de la pared: '))
alto_ladrillo = float(input('Ingrese el alto del ladrillo: '))
largo_ladrillo = float(input('Ingrese el largo del ladrillo: '))

ladrillos_fila = largo_pared / (largo_ladrillo + ancho_mezcla)

cantidad_filas = alto_pared / (alto_ladrillo + ancho_mezcla)

cantidad_ladrillos = ladrillos_fila * cantidad_filas

print('Los ladrillos por fila son', ladrillos_fila)
print('La cantidad de filas son', cantidad_filas)

print('La cantidad de ladrillos para contruir pared de', largo_pared, 'cm de largo por', alto_pared,
      'cm de alto es: ', int(cantidad_ladrillos), 'ladrillos')


#1. Plazo fijo
#Desarrollar un programa que cargue por teclado la cantidad de dinero depositada en plazo fijo
#por un cliente de un banco
#y calcular el saldo que tendrá esa cuenta al vencer el plazo fijo,
#sabiendo que el interés pactado era de 2.3%
#y que el banco cobra una tasa fija de gastos por servicios financieros igual $20 por cuenta.

plazo_fijo = float(input('Ingrese el dinero depositado: '))
tiempo = int(input('Ingrese la duracion del plazo fijo: '))

interes = plazo_fijo * 2.3 / 100

gastos = 20

calculo = (interes - gastos) * tiempo

saldo = plazo_fijo + calculo

print('El saldo que tendra es', saldo)


#Solución CATEDRA AED
#__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

# Titulo y carga de datos
print('Calculo de interés y saldo final en un plazo fijo')
capital = float(input('Ingrese el capital del plazo fijo: '))

# Procesos
capital_final = capital * 1.023 - 20

# La función round(x, n) retorna el número flotante x,
# pero redondeado a n digitos a la derecha del punto decimal.
capital_final = round(capital_final, 2)

# Presentacion de resultados
print('El capital final que se obtiene del plazo fijo es:', capital_final)


#2. Fecha como cadena
#Desarrollar un programa que cargue por teclado una cadena de caracteres
# que se supone representa una fecha en formato 'dd/mm/aaaa',
#y muestre por separado el día, el mes y el año.
# Ejemplo: si la cadena ingresada es '16/03/2016'
# el programa debe mostrar: 'Día: 16  -  Mes: 03  -  Año: 2016'.

fecha = input('Ingrese la fecha (dd/mm/aaaa - incluyendo cero): ')

dia = fecha [0] + fecha [1]
mes = fecha [3] + fecha [4]
año = fecha [6] + fecha [7] + fecha[8] + fecha[9]

print('Dia:',dia,'- Mes:',mes,'- Año:',año)


#3. Importe como cadena
#Desarrollar un programa que cargue por teclado un importe (cantidad de dinero)
#expresado como número en coma flotante
#y muestre un mensaje con esa cantidad pero en dos formatos: en uno debe aparecer
#precedida por el signo '$'
#y en el otro debe aparecer precedida por la palabra "pesos".

dinero = float(input('Ingrese el importe: '))

tipo1 = '$ ' + str(dinero)
tipo2 = str(dinero) + ' pesos'

print(tipo1,'\t',tipo2)


#4. Duración de un vuelo
#Desarrollar un programa que, conociendo el horario de partida y llegada de un vuelo (hora y minutos),
#determine cuál es su duración en minutos.
# Si el viajero necesita luego 45 minutos más para ir del aeropuerto al hotel que ha reservado,
#¿a qué hora llegara al mismo?


partida = float(input('Ingrese el horario de partida (hora y minutos): '))
llegada = float(input('Ingrese el horario de llegada (hora y minutos): '))

duracion_vuelo = llegada - partida
r = round(duracion_vuelo, 2)

minutos = duracion_vuelo * 60
r2 = round(minutos, 2)

reserva = 0.75 + r


print('La duracion del vuelo en horas es de: ',r,'horas',
    '\nLa duracion del vuelo en minutos es de: ',r2,'minutos'
    '\nLa duracion del viaje desde la partida del hotel es de: ', reserva)


Solución
__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

TIEMPO_TAXI = 45

# Titulo y carga de datos
print('Determinacion de tiempo de llegada a aeropuerto')
print('Las horas se ingresaran en formato hh:mm (ejemplo: 14:45 o 05:30)')
partida = input('Ingrese la hora de partida en formato hh:mm :')
llegada = input('Ingrese la hora de llegada en formato hh:mm :')

# Procesos

# Sacamos la hora de partida y la convertimos a número entero...
hp = partida[0] + partida[1]
hora_partida = int(hp)

# Ahora los minutos de esa hora, en formato entero...
mp = partida[3] + partida[4]
minutos_partida = int(mp)

# Sacamos la hora llegada y hacemos lo mismo...
hl = llegada[0] + llegada[1]
hora_llegada = int(hl)

# Igual se procede con los minutos...
ml = llegada[3] + llegada[4]
minutos_llegada = int(ml)

# Transformamos hh de la hora de partida a minutos
# y la acumulamos a los mm de los minutos de partida
minutos_partida = minutos_partida + hora_partida * 60

# Transformamos la hh de la hora de llegada a minutos
# y la acumulamos a los mm de los minutos de llegada
minutos_llegada = minutos_llegada + hora_llegada * 60

# Duracion del viaje...
duracion_viaje_minutos = minutos_llegada - minutos_partida
hora_llegada_hotel = (minutos_llegada + TIEMPO_TAXI) // 60
minutos_llegada_hotel = (minutos_llegada + TIEMPO_TAXI) % 60

# Presentacion de resultados
print('La duracion del viaje es de:', duracion_viaje_minutos, 'minutos')
print('Llega a las', (str(hora_llegada_hotel) + ':' + str(minutos_llegada_hotel)))



#5. Control electoral
#Desarrollar un programa de control electoral en un centro vecinal,
#en el que se ingresen, para cierto candidato: apellido, nombre y cantidad de votos.
#Luego presentar en pantalla un resumen que muestre: iniciales del candidato,
#cantidad de votos entre paréntesis,
#y debajo una línea con tantas  "x" como votos obtenidos (por ejemplo, el candidato obtuvo 4 votos,
#deberá aparecer una línea como esta:  "xxxx"  con cuatro letras "x")
#(Asumimos que en el centro vecinal no hay demasiados electores,
#de forma que podamos estar seguros que no habrá miles o millones de votos...
#sólo unos pocos para darle sentido al enunciado).


nom_cand_1 = input('Ingrese el nombre del candidato: ')
ape_cand_1 = input('Ingrese el apellido del candidato: ')
votos_cand_1 = int(input('Ingrese la cantidad de votos: '))

x = nom_cand_1[0]
y = ape_cand_1[0]

letras = votos_cand_1 * 'x'

print(x, y, '(',votos_cand_1,')',
      '\n',letras)


#Solucion de la catedra

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

# Titulo y Carga de datos
print('Resumen eleccion centro vecinal')
apellido = input('Ingrese el apellido del candidato: ')
nombre = input('Ingrese el nombre del candidato: ')
votos = int(input('Ingrese la cantidad de votos que obtuvo: '))

# Procesos
iniciales = nombre[0] + apellido[0]
cantidad_x = 'x' * votos

# Presentacion de resultados
print(iniciales, '(', votos, ')')
print(cantidad_x)


#6. Cálculo de sueldo
#Se conoce el monto del salario actual de un empleado, el nombre del empleado
#y el área funcional al cual pertenece.
#Se pide calcular el nuevo salario del empleado sabiendo que obtuvo un incremento
#del 8% sobre su salario actual
#y un descuento de 2.5% por servicios,
#informando los resultados con el formato que se especifica a continuación:

#       Nombre Empleado:  xxxxxxxxx            Nuevo Salario: $ xxx

#       Área Funcional:  xxxxxxxxxxxx

#       Salario Actual: $ xxxx


nombre = input('Ingrese el nombre y apellido del empleado: ')
area = input('Ingrese el area funcional del empleado: ')
salario_actual = int(input('Ingrese el salario actual del empleado: '))

aumento = (salario_actual * 8) /100
servicios = (salario_actual * 2.5) /100

descuentos = aumento - servicios

nuevo_salario = salario_actual + descuentos

print('\nNombre empleado: ',nombre,'\nArea funcional: ',area,'\nSalario actual: ',salario_actual,'$',
      '\nNuevo salario: ',nuevo_salario,'$')



#SOLUCION CATEDRA

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

# Titulo y carga de datos
print('Actualización del sueldo de un empleado')
nombre = input('Ingrese el nombre del empleado: ')
area = input('Ingrese el area funcional en la que trabaja: ')
sueldo = float(input('Ingrese el importe de su sueldo actual: '))

# Procesos
aumento = sueldo * 0.08
descuento = sueldo * 0.025
nuevo_sueldo = sueldo + aumento - descuento

# Presentacion de resultados
print('Nombre empleado:', nombre, '\t\tNuevo sueldo $:', nuevo_sueldo)
print('Area funcional:', area)
print('Sueldo anterior: $', sueldo)



#7. Cálculo presupuestario
#En un hospital existen 3 áreas de servicios: Urgencias, Pediatría y Traumatología.
# El presupuesto anual del hospital se reparte de la siguiente manera:

#Área             Presupuesto

#Urgencias        37%

#Pediatría        42%

#Traumatología    21%


#Cargar por teclado el monto del presupuesto total del hospital,
# y calcular y mostrar el monto que recibirá cada área.

presupuesto = int(input('Ingrese el monto anual del hospital: '))

urgencias = (presupuesto * 37) /100
pediatria = (presupuesto * 42) /100
traumatologia = (presupuesto * 21) /100

print('Urgencias: ',urgencias,
    '\nPediatria: ',pediatria,
    '\nTraumatologia: ',traumatologia)



#SOLUCION CATEDRA

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

# Titulo y carga de datos
print('Calculo presupuestario en un hospital')
presupuesto = float(input('Ingrese monto del presupuesto total: '))

# Procesos
urgencias = presupuesto * 0.37
pediatria = presupuesto * 0.42
traumatologia = presupuesto * 0.21

# Presentacion de resultados
print('Monto asignado a Urgencias:', urgencias)
print('Monto asignado a Pediatria:', pediatria)
print('Monto asignado a Traumatologia:', traumatologia)



#8. Calculo Distancia de Viaje
#Un persona cautivada por los paisajes argentinos se le ocurrió la loca idea de unir
#los puntos mas extremos (Ushuahia y La Quiaca) en bicicleta,
#es decir se propuso hacer 3641.3 Km en bicicleta.

#Nuestro aventurero efectivamente inició la travesía pero se accidentó
#y sólo recorrió x metros según su GPS.

#Usted debe solicitar ese valor x e informar cuántos kilómetros y metros recorrió nuestro aventurero
#y qué porcentaje represento lo recorrido del total de kms a recorrer de Ushuahia a La Quiaca
#(para el porcentaje usted deberá realizar los calculos en metros).

total = 3641.3 * 1000
x = int(input('Ingrese los metros recorridos: '))
kilometros = x // 1000
porcentaje = (x * 100 ) / total
redondeo = round(porcentaje, 2)

print('Los metros recorridos son: ',x,'Los kilometros recorridos son: ',kilometros,
      'El porcentaje del viaje recorrido es de', redondeo,'%')


#SOLUCION CATEDRA

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

print('Conversion de metros a kilimetros de viaje recorridos')
print('=' * 80)
print('\n')

distancia = 3641.3 * 1000
x = int(input('Ingrese la cantidad de metros recorridos: '))

km = x // 1000
mts = x % 1000

porc = (x * 100) / distancia

print('El viajero recorrio ', km , ' kilometros con ', mts, ' metros')
print('Siginifica que el viajero recorrio solo un ', porc, '% del total del viaje')



#9. Costos del Proyecto
#Una pequeña empresa de informática tiene que desarrollar un sistema de información
#y para ello tiene un presupuesto de x pesos para cubrir los costos de crear el sistema.
#Sabiendo que tiene pensado ganar al menos 17% por el proyecto,
#determine cuál es el valor máximo que pueden alcanzar los costos del proyecto.


presupuesto = int(input('Ingrese el el presupuesto: '))

porcentaje = (presupuesto * 17) /100

total = presupuesto - porcentaje

print('El valor maximo de los costos del proyecto es de ',total)

#SOLUCION CATEDRA

__author__ = 'Catedra de Algoritmos y Estructuras de Datos'


print('Calculo de Costos')
print('*' * 80)

presupuesto = float(input('Ingrese el monto total presupuestado: '))

ganancia = presupuesto * 0.17
costos = presupuesto - ganancia

print('Los costos del proyecto no deben exceder los $', costos)


#10. Tiempos de Triatlon
#Un triatlón es una competición deportiva en que los participantes realizan tres carreras:
# una de natación, una ciclista y una pedestre.

#Desarrollar un programa que permita ingresar el tiempo (en minutos y segundos)
# logrados en cada etapa por uno de los deportistas participantes.

#Con esos datos determinar:

#Tiempo total de la prueba (en formato hh:mm:ss)
#Tiempo máximo y mínimo (en segundos)
#Tiempo promedio de la prueba (en segundos, redondeado a 2 decimales)
#Consejo: convertir a segundos los horarios ingresados, para facilitar las operaciones


__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

# Titulo y carga de datos
print('TRIATLÓN')
natacion = input("Ingrese tiempo de natación (mm:ss):")
ciclismo = input("Ingrese tiempo de ciclismo (mm:ss):")
pedestre = input("Ingrese tiempo de carrera pedestre (mm:ss):")

# Procesos

# Identificar componentes y convertir a segundos
natacion_seg = int(natacion[0] + natacion[1])*60 + int(natacion[3] + natacion[4])
ciclismo_seg = int(ciclismo[0] + ciclismo[1])*60 + int(ciclismo[3] + ciclismo[4])
pedestre_seg = int(pedestre[0] + pedestre[1])*60 + int(pedestre[3] + pedestre[4])

# Calcular el total en segundos
total = natacion_seg + ciclismo_seg + pedestre_seg
horas = divmod(total,3600)
total_hh = horas[0]
minutos = divmod(horas[1],60)
total_mm = minutos[0]
total_ss = minutos[1]

#Determinar el mayor y menor tiempo
mayor_tiempo = max(natacion_seg,ciclismo_seg,pedestre_seg)
menor_tiempo = min(natacion_seg,ciclismo_seg,pedestre_seg)

#Determinar tiempo promedio y redondearlo
promedio = (natacion_seg + ciclismo_seg + pedestre_seg)/3
promedio = round(promedio,2)

# Resultados
print("\nEstadísticas")
print("El tiempo total es: ", total_hh,":",total_mm,":",total_ss)
print("El mayor tiempo (en segundos) es: ",mayor_tiempo)
print("El menor tiempo (en segundos) es: ",menor_tiempo)
print("El tiempo promedio(en segundos) es: ",promedio)



#11. Palabra enmascarada
#Desarrollar un programa que permita ingresar una palabra por teclado y la devuelva enmascarada,
#mostrando la primer letra y la última, pero reemplazando los caracteres intermedios por asteriscos.

#Por ejemplo: si se ingresa la palabra “verde” se debe obtener “v***e”.


#SOLUCION CATEDRA
__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

# Titulo y carga de datos
print('Palabra enmascarada')
palabra = input('Ingrese palabra a enmascarar: ')

# Procesos

n = len(palabra)
asteriscos = "*" * (n-2)
enmascarada = palabra[0] + asteriscos + palabra[n-1]

# Resultados
print('\nLa palabra enmascarada es:', enmascarada)
"""


#12. Calculo de Posta de Natacion
#En la disciplina olímpica una de las pruebas mas esperadas en la natacion es la posta 4x100.
#En esta disciplina el equipo ganador registró los siguientes tiempos en cada estilo:

#Espalda: 52 segundos 15 centésimas.
#Pecho: 1 minuto 2 segundos 75 centésimas.
#Mariposa: 59 segundos 80 centésimas.
#Libre: 48 segundos 15 centésimas.
#Usted debe averiguar el tiempo total de la carrera del equipo ganador
#y representarlo en minutos, segundos y centésimas.


#Para recordar:

#1 minutos son 60 segundos.
#1 segundo son 100 centesimas.


#espalda = 52
#centecimas_espalda = (15 / 100)
#segundos_espalda = espalda + centecimas_espalda
#minutos_espalda = segundos_espalda / 60
#redondeo_espalda = round(minutos_espalda, 2)

espalda = 52.15 / 60
r_espalda = round(espalda, 2)
pecho = 62.75 / 60
r_pecho = round(pecho, 2)
mariposa = 59.80 / 60
r_mariposa = round(mariposa, 2)
libre = 48.15 / 60
r_libre = round(libre, 2)

sumatoria_total = r_espalda + r_pecho + r_mariposa + r_libre
r_sumatoria_total = round(sumatoria_total, 2)



print(r_sumatoria_total)



#13. Triángulo Rectángulo
#Desarrollar un programa que, ingresando los dos catetos de un triángulo rectángulo, informe:

#Valor de la hipotenusa (redondeado a 2 decimales)
#Valor del lado mayor
#Valor del lado menor





#14. Sumador de Ángulos
#Se desea un programa que dados 2 ángulos expresados en grados minutos y segundos, informe la suma de ambos en grados minutos y segundos.

#A modo de ejemplo se agrega la siguiente gráfica:



#Tener en cuenta que en el algoritmo implementado no necesariamente hay que seguir el mecanismo empírico propuesto por la imagen.


