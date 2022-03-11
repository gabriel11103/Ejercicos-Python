"""
# 1_
#Dado el valor de los tres lados de un triángulo, calcular el perímetro del triángulo.

l1 = float(input("ingrese lado 1: "))
l2 = float(input("ingrese lado 2: "))
l3 = float(input("ingrese lado 3: "))

suma = l1 + l2 + l3

print("El perimetro del triangulo es ", suma)

# 2_
#Se conoce la cantidad de horas que trabaja un empleado en una fábrica, más el importe
#que percibe por cada hora trabajada, además del nombre del empleado. Se pide calcular el importe
#final del sueldo que el empleado deberá cobrar y mostrar el nombre del empleado y el importe final
#del sueldo que se calculó.

nombre = input("Ingrese el nombre del empleado: ")
horas = int(input("Ingrese las horas trabajadas: "))
importe = float(input("Ingrese el importe por hora: "))

sueldo = horas * importe

print('El sueldo a cobrar de', nombre, 'es', sueldo)

# 3_
#Se tiene registrada la temperatura ambiente medida en
#tres momentos diferentes en un depósito de químicos 
#y se necesita calcular el valor  promedio entre las temperaturas 
#medidas, tanto en formato entero (sin decimales) 
#como en formato real (con decimales).

t1 = int(input("Ingrese la temperatura uno: "))
t2 = int(input("Ingrese la temperatura dos: "))
t3 = int(input("Ingrese la temperatura tres: "))

resultado = t1 + t2 +t3

p1 = resultado //3
p2 = resultado /3

r= round(p2,2)

print("Promedio entero", p1, "- Promedio real", r)


# Se conoce la cantidad total de personas que padecen cierta enfermedad 
# en todo el país, y también se sabe cuántas de esas personas viven 
# en una ciudad determinada. Se desea saber qué porcentaje representan 
# estas últimas sobre el total de enfermos del país. 

c1 = int(input("Ingrese la cantidad de pacientes: "))
c2 = int(input("Ingrese cuantos viven en Cordoba: "))

resultado = c2 * 100 /c1

print("El total de los pacientes de Cordoba respresentan el", resultado, "% del pais" )

#EJERCICIOS EXTRA

1. Cuadrados y cubos
Leer dos números y calcular:

#La suma de sus cuadrados.
#El promedio de sus cubos.

num_uno = int(input('Ingrese numero uno: '))
num_dos = int(input('Ingrese numero dos: '))

cuadrados = (num_uno **2) + (num_dos**2)

cubo = (num_uno**3 + num_dos**3) / 2

print('La suma de los cuadrados de', num_uno, 'y', num_dos, 'es', cuadrados,
      'y el promedio de sus cubos es', cubo)

#2. Descuento en medicinas
#Calcular el descuento y el monto a pagar por un medicamento cualquiera en una farmacia
#(cargar por teclado el precio de ese medicamento)
#sabiendo que todos los medicamentos tienen un descuento del 35%.
#Mostrar el precio actual, el monto del descuento y el monto final a pagar.

precio = float(input('Ingrese el precio del medicamento: '))

descuento = (precio * 35) /100

monto_final = precio - descuento

print('El precio del medicamento es $', precio, '\nEl monto de descuento es $', descuento, '\nEl precio final a pagar es $', monto_final)

#3. Ecuación de Einstein
#La famosa ecuación de Einstein para conversión de una masa m en energía viene dada por la fórmula:

#E = mc2

#Donde c es la velocidad de la luz cuyo valor es c = 299792.458 km/seg.
#Desarrolle un programa que lea el valor una masa m en kilogramos
#y obtenga la cantidad de energía E producida en la conversión.

masa = float(input('Ingrese la masa: '))

velociadad_luz = 299792.458

c = velociadad_luz **2

energia = masa * c

print('La cantidad de energia E producida de la masa es: ', energia)


#4. Polinomio de segundo grado
#Desarrollar un programa que cargue por teclado los coeficientes a, b y c de un polinomio de segundo grado,
#y calcule y muestre el valor del polinomio en el punto x (cargando también x por teclado).
#Además, para el mismo polinomio, calcule y muestre el valor del discriminante de la fórmula
#para el cálculo de las raíces de la ecuación.

a = float(input('Ingrese el coeficiente a del polinomio: '))
b = float(input('Ingrese el coeficiente b del polinomio: '))
c = float(input('Ingrese el coeficiente c del polinomio: '))
x = float(input('Ingrese el valor de x: '))

calculo_y = a * (x **2) + b * x + c

discriminante = b ** 2 - 4 * a * c

print('El valor del polinomio en el valor x es:', x, 'en y es:',calculo_y,'\ny el discriminante es: ', discriminante)


#5. Cálculo de ángulos
#Se sabe que la suma de dos ángulos desconocidos (alfa + beta)
#es igual a cierto valor x que se carga por teclado.
#Además se sabe que la diferencia entre esos mismos dos ángulos (alfa - beta)
#es igual a otro valor y que también se carga por teclado.
#Desarrolle un programa que dados los valores x e y, determine el valor de los dos ángulos alfa y beta.
#No es necesario convertir a grados, minutos y segundos el valor de cada ángulo:
#expréselos como números reales, tal cual hayan sido obtenidos.

valor_x = int(input('Ingrese el valor de x: '))
valor_y = int(input('Ingrese el valor de y: '))

suma = valor_x + valor_y

diferencia = valor_x - valor_y

beta = (valor_x + valor_y) /2

alfa = valor_y + beta

print('El valor del angulo alfa es', alfa,'\nEl valor del angulo veta es', beta)

# Procesos:

# se sabe que:
# x = alfa + beta
# y = alfa - beta

# De donde:
# x = alfa + beta
# =>  alfa = x - beta

# Por lo tanto:
# y = alfa - beta
# => y = x - beta - beta
# => y = x - 2*beta
# => y + 2*beta = x
# => 2*beta = x - y
# => beta = (x-y)/2

# Entonces:
# Si y = alfa - beta
# => alfa = y + beta


#6. Precio de venta
#Conociendo el precio de lista de un artículo, determinar:

#Precio de venta al contado (10% de descuento)
#Precio de venta con tarjeta (5% de recargo)

articulo = float(input('Ingrese el valor del producto: '))

contado = (articulo * 10) / 100

valor_contado = articulo - contado

tarjeta = (articulo * 5) / 100

valor_tarjeta = articulo + tarjeta

print ('El valor de contado es: ',valor_contado, '\nEl valor con tarjeta es: ', valor_tarjeta)


#7. Votación en el Congreso
#En el Congreso se vota la sanción de una ley muy importante.
#Desarrollar un programa que permita ingresar la cantidad de votos a favor y en contra,
#e informe el porcentaje obtenido en cada caso.

votos_favor = int(input('Ingrese la cantidad de votos a favor: '))
votos_contra = int(input('Ingrese la cantidad de votos en contra: '))

total = votos_favor + votos_contra

porcentaje_favor = votos_favor / total * 100
porcentaje_contra = votos_contra / total * 100

print('El porcentaje obtenido de votos a favor es', porcentaje_favor, '% \nLa cantidad de votos en contra es', porcentaje_contra,'%')


#8. Rinde de un Campo Agricola
#Un productor agricola desea saber cuantos quintales de trigo puede producir en su parcela.
#Se pide ingresar el largo y el ancho en metros de la parcela
#y determinar el rinde sabiendo que en 10 m2 se obtienen 2 quintales.

largo = float(input('Ingrese el largo de la parcela: '))
ancho = float(input('Ingrese el ancho de la parcela: '))

parcela = largo * ancho

quintales = (parcela * 2) // 10

print('La superficie de su parcela es de', parcela,
      '\nLa cantidad de quintales de trigo que entran en su parcela son: ',quintales)


#9. Datos de un rectángulo
#Hacer un programa que tome como entrada el ancho y el alto de un rectángulo
#y determine el perímetro y la superficie del mismo.

ancho = int(input('Ingrese el ancho del rectangulo: '))
alto = int(input('Ingrese el alto del rectangulo: '))

perimetro = ancho * 2 + alto *2

superficie = ancho * alto

print('El perimetro del rectangulo ingresado es: ',perimetro,
      '\nLa superficie del rectangulo ingresado es: ',superficie)
"""




