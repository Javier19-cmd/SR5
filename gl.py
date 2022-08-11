"""
#Nombre: Javier Valle
#Carnet: 20159

Referencias: 

1. Instanciar un archivo de Python: https://www.youtube.com/watch?v=rYcluou5gEo&ab_channel=LuisCabreraBenito
2. Saber si un número es múltiplo de otro: https://www.youtube.com/watch?v=jOCh6ZpkE1k&ab_channel=JohnOrtizOrdoñez
3. Hacer un return de múltiples variables: https://www.youtube.com/watch?v=QOQTYuynU3w&ab_channel=ProgramaResuelto
4. Formato de archivo BMP: https://en.wikipedia.org/wiki/BMP_file_format#:~:text=The%20BMP%20file%20format%2C%20also,and%20OS%2F2%20operating%20systems. 
5. Acceder a una variable de otra clase: https://programmerclick.com/article/14131486210/
6. Algoritmo de Lineas Bresenham: https://es.wikipedia.org/wiki/Algoritmo_de_Bresenham#:~:text=El%20Algoritmo%20de%20Bresenham%20es,solo%20realiza%20cálculos%20con%20enteros.
7. Algoritmo de Bresenham: https://www.youtube.com/watch?v=yaovJmM-0OM&ab_channel=CodesVille
8. Simular un do-while: https://www.freecodecamp.org/espanol/news/python-bucle-do-while-ejemplos-de-bucles/#:~:text=Para%20crear%20un%20bucle%20do%20while%20en%20Python%2C%20necesitas%20modificar,verdadero%20se%20ejecutará%20otra%20vez.
"""


"""
SR4:

1. Coordenadas baricéntricas (Ejemplo 9): 
    https://www.programcreek.com/python/?CodeExample=get+bounding+box

2. Evitando la división entre cero: 
    https://www.yawintutor.com/zerodivisionerror-division-by-zero/
"""

from Render import * #Importando la clase Render.
from utilidades import *
import random
from vector import *

c1 = Render() #Inicializando la clase Render.

#Pregunar si está bien implementada esta función.
def glInit(): #Se usará para poder inicializar cualquier objeto interno que requiera el software de render.

    pass

def glCreateWindow(width, height): #Preguntar de esta función.
    #Se usará para inicializar el framebuffer con un tamaño (la imagen resultante va a ser de este tamaño)

    try: #Verificar que el tamaño sea un número.
        #Saber si las dimensiones son múltiplos de 4.
        if width % 4 == 0 and height % 4 == 0:
            
            #Creando las dimensiones de la pantalla.

            c1.width = width #Ancho de la pantalla.
            c1.height = height #Alto de la pantalla.

        elif width < 0 or height < 0: #Si las dimensiones son negativas, entonces se imprime un error.
            print("Error")
        else: 
            print("Error")
    
    except (TypeError, ZeroDivisionError): #Si en caso es NoneType, entonces se imprime esta excepción.
        print("Ocurrió un problema con el tamaño de la imagen.")
    #except: #Si en caso se escribió una letra en vez de número, entonces se imprime esta excepción.
     #   print("Se ingresó una letra en vez de número.")

def glViewPort(x, y, width, height): #Se usará para definir el área de la imagen sobre la que se va a poder dibujar.

    colorV = color(0.4, 0.8, 0.08) #Creando el color del viewport.

    #Verificando que las dimensiones del viewport sean múltiplos de 4.
    if width % 4 == 1 and height % 4 == 1:
        
        c1.colorViewPort = colorV #Se manda a hacer el color del viewport.

        c1.View(x, y, width, height) #Se manda a hacer el viewport.
    else: 
        print("Error")


#Preguntar si esta función lo que hace es llenar por primera vez el color de la pantalla.
def glClear(): #Se usará para que llene el mapa de bits con un solo color.   
    

    #print("Colores en glClear ", color(rP, gP, bP)) #Imprimiendo el color que se le pasa.
    
    # if rP < 0 or gP < 0 or bP < 0: #Si los colores son menores a 0, entonces se imprime un error.
    #     print("Error")
    # elif rP > 1 or gP > 1 or bP > 1:
    #     print("Error")
    # else: #Si todo está bien, entonces se llena el mapa de bits con el color que se le pasa.
    #     #print(color(rP, gP, bP))
    
    #c1.Framebuffer() #Llenando el framebuffer con el color que se le pasó en glClearColor.

    c1.framebuffer = [
                    [c1.colorFondo for x in range(c1.width)] #Llenando el framebuffer con el color que se le pasó en glClearColor.
                      for y in range(c1.height)
                    ] #Llenando el framebuffer con el color que se le pasó en glClearColor.

    c1.zBuffer = [
                    [-9999 for x in range(c1.width)] #Llenando el zBuffer con un valor muy pequeño.
                    for y in range(c1.height)
                ] #Llenando el zBuffer con un valor muy pequeño.
    
    #print("zBufferE ", c1.zBufferE) #Imprimiendo el zBufferE.

    #print("zBufferE: ", c1.zBufferE) #Imprimiendo el zBufferE.

def glClearColor(r, g, b): #Función con la que se pueda cambiar el color con el que funciona glClear(). Los parámetros deben ser números en el rango de 0 a 1.
        
    #Verificando que los códigos de los colores no sean negativos.
    if r < 0 or g < 0 or b < 0:
        print("Error")
    elif r > 1 or g > 1 or b > 1: #Verificando que los códigos de los colores no sean mayores a 255.
        print("Error")
    else: #Si todo está bien, entonces se crea el framebuffer con el color que se le pasa.
        
        #print("Color de fondo antes: ", c1.colorFondo) #Antes de cambiar el color, se imprime el color de fondo.
        
        colorPantalla = color(r, g, b) #Creando el color de la pantalla.
        
        c1.colorFondo = colorPantalla #Se manda a hacer el color de la pantalla.

        #print("Color de fondo: ", c1.colorFondo) #Imprimiendo el color de la pantalla.

        #color(rP, gP, bP) #Color inicial de la pantalla.
       
        #Rend2.recibirColor(color(rP, gP, bP))

        #print("Color en glClearColor: ", color(rP, gP, bP)) #Debuggeo.

def glVertex(x, y): #Función que pueda cambiar el color de un punto de la pantalla. Las coordenadas x, y son relativas al viewport que definieron con glViewPort. glVertex(0, 0) cambia el color del punto en el centro del viewport, glVertex(1, 1) en la esquina superior derecha. glVertex(-1, -1) la esquina inferior izquierda
    #Debuggeo de los puntos.
    #print("Punto: ", x, y)

    #print("Ancho: ", c1.width) #Ancho de la pantalla.
    #print("Alto: ", c1.height) #Alto de la pantalla

    #Verificando que las coordenadas no sean negativas.
    if x < 0 or y < 0: #Si las coordenadas son negativas, entonces se da un mensaje de error.
        return
    elif x > c1.width or y > c1.height: #Verificando que las coordenadas no se salgan de la pantalla.
        return
    else: #Si todo está bien, entonces se cambia el color del punto.
        c1.Vertex(x, y) #Se manda a hacer el punto.

#Función que crea una línea entre dos puntos. Esta tiene que estar en el rango de 0 a 1.
def glLine(v1, v2):


    #Redondeo para que no haya problemas con los decimales.
    x0 = round(v1.x)
    y0 = round(v1.y)
    x1 = round(v2.x)
    y1 = round(v2.y)


    #Verifiando las propiedades del viewport.
    #print(ancho, alto, equis, ye)
    
    #Moviendo el punto a la posición deseada.
    # dy = abs(y1 - y0)
    # dx = abs(x1 - x0)

    #print("Posiciones: ", x0, y0, x1, y1)

    #Prueba.
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    #Debuggeo.
    #print("Cambio en y y cambio en x ", dy, dx)
    #print("Cambio en x y cambio en y ", dx1, dy1)


    steep = dy > dx #Verificando si la línea es vertical o horizontal.

    if steep: #Si la línea es vertical, entonces se cambia el orden de los puntos.
        x0, y0 = y0, x0
        x1, y1 = y1, x1
    
    if x0 > x1: #Si el punto 1 está a la derecha del punto 2, entonces se cambia el orden de los puntos.
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    #Calculando los nuevos cambios.
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    offset = 0 #Offset de la línea.
    threshold = dx #Umbral de la línea.	
    y = y0 #Coordenada y de la línea.

    #Verificando las variables.
    #print("Offset, threshold, y ",offset, threshold, y)

    #Dibujando la línea.
    for x in range(x0, x1 + 1):
        
        offset += dy * 2 #Cambiando el offset.
        if offset >= threshold: #Si el offset es mayor o igual al umbral, entonces se cambia la coordenada y.
            y += 1 if y0 < y1 else -1
            threshold += 2 * dx

            #print("Punto inicial: ", movx1, movy1)
            #print("Punto final: ", movx2, movy2)

        if steep: #Si la línea es vertical, entonces se cambia el orden de los puntos.
            c1.Vertex(y, x)
        else: #Si la línea es horizontal, entonces se cambia el orden de los puntos.
            #print("Puntos dados en decimales ", x0, y0, x1, y1)
            c1.Vertex(x, y)


def glColor(r, g, b): #Función con la que se pueda cambiar el color con el que funciona glVertex(). Los parámetros deben ser números en el rango de 0 a 1.
    
    #Convertir el valor de 0 a 1 de 0 a 255 y luego llamar al color.
    if r < 0 or g < 0 or b < 0:
        print("Error")
    elif r > 1 or g > 1 or b > 1:
        print("Error")
    else:
        
        #print("Color antes de ser cambiado: ", c1.colorP)
        Color = color(r, g, b) #Se manda a hacer el color con las utilidades y se setea el color.
        #print("Color en gl: ", Color)
        c1.colorP = Color #Se setea el color del punto.


def cross(V1, V2): #Producto cruz entre dos vectores, pero con return de V3.

    return V3(
        V1.y * V2.z - V1.z * V2.y,
        V1.z * V2.x - V1.x * V2.z,
        V1.x * V2.y - V1.y * V2.x
    )

def bounding_box(A, B, C): #Función que calcula el bounding box de un triángulo.

    coords = [(A.x, A.y), (B.x, B.y), (C.x, C.y)] #Se guardan las coordenadas de los puntos.

    #Se calculan las coordenadas mínimas y máximas.
    xmin = 99999
    xmax = -99999
    ymin = 99999
    ymax = -99999


    for (x, y) in coords: #Se recorren las coordenadas.

        if x < xmin: #Si la coordenada x es menor que la mínima, se setea la mínima.
            xmin = x
        if x > xmax: #Si la coordenada x es mayor que la máxima, se setea la máxima.
            xmax = x
        if y < ymin: #Si la coordenada y es menor que la mínima, se setea la mínima.
            ymin = y
        if y > ymax: #Si la coordenada y es mayor que la máxima, se setea la máxima.
            ymax = y

    #print("Coordenadas: ", x, y)

    return V3(xmin, ymin), V3(xmax, ymax) #Se retornan las coordenadas mínimas y máximas.


    #return V3(xmin, xmax), V3(ymin, ymax) #Retornando los valores mínimos y máximos de x y y.

def baricentrico(A, B, C, P):

    cx, cy, cz = V3(B.x - A.x, C.x - A.x, A.x - P.x) * V3(B.y - A.y, C.y - A.y, A.y - P.y)
                    

    #print("¨Producto cruz: ", V3(B.x - A.x, C.x - A.x, A.x - P.x) * V3(B.y - A.y, C.y - A.y, A.y - P.y))

    #print("Valor de cz: ", cz)

    if cz == 0: #Si el valor de cz es 0, entonces el punto no está en el plano.
        u, v = -1, -1
        w = -1

        return (u, v, w)
    else: #Si el valor de cz es diferente de 0, entonces el punto está en el plano.

        u = cx/cz
        v = cy/cz
        w = 1 - (u + v)

        return (u, v, w)

def triangle(A, B, C, col): #Función que dibuja un triángulo.

    #print(col[0], col[1], col[2])

    #print(A, B, C) #Se imprimen las coordenadas.

    L = V3(0, 0, -1) #Vector de la luz.

    #Calculando la normal.
    N = cross((C - A), (B - A)) #Se calcula la normal.

    #print("Normal: ", N) #Se imprime la normal.

    i = L.normalice() @ N.normalice() #Se calcula el producto punto. Esto es para la intensidad del color.

    #print("Intensidad: ", i) #Se imprime la intensidad.

    if i < 0: #Si i es menor a 1, entonces el punto está opuesto a la luz.
        return
    
    #print("Producto punto: ", i)

    c1.colorP = color(
        col[0] * i, 
        col[1] * i, 
        col[2] * i
        ) #Se setea el color del punto en escala de grises.

    #print("Color: ", c1.colorP)

    # c1.colorP = color(
    #     random.uniform(0, 1),
    #     random.uniform(0, 1),
    #     random.uniform(0, 1)
    # ) #Se setea el color del punto.

    #c1.colorP = col #Se setea el color del punto. (En este caso gris)


    #Calculando los mínimos y máximos de los puntos.
    min, max = bounding_box(A, B, C) #Se calculan los mínimos y máximos de los puntos.

    #print("Mínimos: ", min.x, min.y)
    #print("Máximos: ", max.x, max.y)

    #Redondeando los mínimos y máximos para poderlos meter a los for-loops.
    min.round()
    max.round()


    for x in range(min.x, max.x + 1):
        for y in range(min.y, max.y + 1):
            u, v, w = baricentrico(A, B, C, V3(x, y)) #Se calcula el baricéntrico.

            if u < 0 or v < 0 or w < 0: #Si el baricéntrico es mayor o igual a 0, entonces se dibuja el punto.
                #print("Punto: ", x, y)
                continue
            
            #print("Color del fondo: ", c1.colorFondo)
            #print("Color del punto", c1.colorP)

            z = A.z * u + B.z * v + C.z * w #Se calcula la z.
        

            if (c1.zBuffer[x][y] < z):
                #print(c1.zBuffer[x][y])
                c1.zBuffer[x][y] = z #Se setea la z.
                #print(c1.zBuffer[x][y])
                glVertex(x, y) #Se dibuja el punto.
            #glVertex(x, y) #Se dibuja el punto.

def zBuffer(): 
    
    #Copiar el zBuffer al zBufferE.
    c1.zBufferE = c1.zBuffer.copy() #Copiar el zBuffer al zBufferE.

    #Recorriendo el zBufferE. Si hay un -9999, entonces se cambia por un 0.
    for i in range(c1.height):
        for j in range(c1.width):
            if c1.zBufferE[i][j] == -9999: #Si el zBufferE tiene un -9999, entonces se cambia por un 0.
                c1.zBufferE[i][j] = color(0, 0, 0)
            elif c1.zBufferE[i][j] < 0: #Si el zBufferE tiene un valor menor a 0, entonces se cambia por un 0.
                c1.zBufferE[i][j] = color(0, 0, 0)
            elif c1.zBufferE[i][j] > 1 and c1.zBufferE[i][j] < 255: #Si el zBufferE tiene un valor mayor a 1, pero menor a 255, entonces dividir el número entre 255.
                c1.zBufferE[i][j] = color(int(c1.zBufferE[i][j] / 255), int(c1.zBufferE[i][j] / 255), int(c1.zBufferE[i][j] / 255))
                #print(c1.zBufferE[i][j])
            elif c1.zBufferE[i][j] > 255: #Si hay un valor mayor a 255, entonces se cambia por un 1.
                c1.zBufferE[i][j] = color(1, 1, 1)
            else: #Si hay algún color sesgado entre 0 y 1, entonces se pintan.
                c1.zBufferE[i][j] = color(int(c1.zBufferE[i][j]), int(c1.zBufferE[i][j]), int(c1.zBufferE[i][j]))

def glFinish(): #Función que escribe el archivo de imagen resultante.

   c1.write() #Escribiendo el archivo.
   c1.write2() #Escribiendo el archivo con el zBuffer.


