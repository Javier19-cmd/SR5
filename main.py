"""
Referencias: 
 1. Acceder a una variable de una clase: https://www.codigopiton.com/variables-de-clase-y-de-instancia-en-python/#:~:text=Como%20puedes%20ver%2C%20para%20acceder,código%20definido%20en%20la%20clase.
 2. Acceder a un método de una clase: https://j2logo.com/python/tutorial/programacion-orientada-a-objetos/#:~:text=Para%20crear%20un%20objeto%20de,se%20llamara%20a%20una%20función).&text=El%20código%20anterior%20crea%20una,objeto%20a%20la%20variable%20obj%20.
 3. Inicializar una clase: https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=44&codigo=44&inicio=30
 4. Clases en Python: https://tutorial.recursospython.com/clases/#:~:text=Para%20crear%20una%20clase%20vamos,mayúscula%2C%20y%20sin%20guiones%20bajos.
"""
#Archivo que tendrá el método main del programa

from gl import * #Importando el archivo gl.py, para crear la imagen.
from Obj import * #Importando los métodos del archivo Obj.py.
from vector import * #Importando los métodos del archivo vector.py.

def main():
    glCreateWindow(1024, 1024) #Creando la ventana.
    glClearColor(1, 1, 1) #Color del fondo.
    glClear() #Limpiando el framebuffer con el color creado en glClearColor.
    
    
    #glVertex(0.1, 0.3) #Dibujando el punto.

    #glColor(0.5, 0.3, 0.1) #Asignando el color del punto.

    #col1 = color(0.501, 0.501, 0.501) #Color gris.

    col1 = (1, 1, 1) #Negro.

    #triangle(V3(10, 70), V3(50, 160), V3(70, 80), col1) #Llamando al método triangle para dibujar un triángulo.
    #triangle(V3(180, 50), V3(150, 1), V3(70, 180), col2) #Llamando al método triangle para dibujar un triángulo.
    #triangle(V3(180, 150), V3(120, 160), V3(130, 180), col3) #Llamando al método triangle para dibujar un triángulo.


    r = Object('Porsche.obj') #Llamando al método Object del archivo Obj.py.
    scale = (5, 5, 10) #Escala del objeto. Tamaño del objeto.
    translate = (512, 300, 0) #Traslación del objeto. #Posición del objeto en el framebuffer.

    #Recorriendo las caras del objeto y dibujando las líneas en el framebuffer.
    for face in r.faces: 
        #print(face) #Debuggeo.
        
        if len(face) == 4: #Validando que la cara tenga 4 vértices.
            #El array de caras es bidimensional en este código.
            f1 = face[0][0] - 1 #Se le resta 1 porque el array de vértices empieza en 0.
            f2 = face[1][0] - 1 #Agarrando el índice 0.
            f3 = face[2][0] - 1 #Agarrando el índice 1.
            f4 = face[3][0] - 1 #Agarrando el índice 2.

            #Transformando los vértices.
            v1 = r.transform_vertex(r.vertices[f1], scale, translate)
            v2 = r.transform_vertex(r.vertices[f2], scale, translate)
            v3 = r.transform_vertex(r.vertices[f3], scale, translate)
            v4 = r.transform_vertex(r.vertices[f4], scale, translate)

            #print("Cara: ", f1, f2, f3, f4)

            #Dibujando los triangulos.
            triangle(v1, v2, v4, col1)
            triangle(v2, v3, v4, col1)


        elif len(face) == 3: #Validando que la cara tenga 3 vértices.
            f1 = face[0][0] - 1 #Se le resta 1 porque el array de vértices empieza en 0.
            f2 = face[1][0] - 1 #Agarrando el índice 0.
            f3 = face[2][0] - 1 #Agarrando el índice 1.
            #f4 = face[3][0] - 1 #Agarrando el índice 2.

            #print(r.vertices[f1], scale, translate)

            #Transformando los vértices.
            v1 = r.transform_vertex(r.vertices[f1], scale, translate)
            v2 = r.transform_vertex(r.vertices[f2], scale, translate)
            v3 = r.transform_vertex(r.vertices[f3], scale, translate)

            #print("Cara: ", f1, f2, f3)
            #print(v1, v2, v3)

            #colr = color(1, 0, 0) #Color para el triángulo.

            triangle(v1, v2, v3, col1) #Llamando al método triangle para dibujar un triángulo.
    
    zBuffer() #Haciendo la copia del z-buffer.
    glFinish() #Escribiendo el framebuffer en la imagen y guardándola en un archivo.

main()