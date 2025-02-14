"""
Evidencia Final

Colaboradores:
César Ivann Llamas Macías
Lizbeth Maribel Meléndez Delgado
Luis Humberto Sánchez Vaca
Mónica Jaqueline Íñiguez Moncada
Samuel Alejandro Díaz del Guante Ochoa

Creacion: 16/09/2020
Ultima modificacion: 17/09/2020
"""
#importacion de la libreria Open CV para poder usar algunas funciones
import cv2


if __name__ == '__main__':
    # Asignar la camara por default en computadora
    cap = cv2.VideoCapture(0)

    # Codec; parametro necesario para output de video
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    # Output de video (Nombre de archivo, codec, fps, tamaño de ventana)
    out = cv2.VideoWriter('ConvolutionVideoPrueba.mp4',
                        fourcc, 20.0, (640,480))

    operation = True
    while operation:
        # Captura de un frame de video
        ret, frame = cap.read()

        # Aplicacion de filtros sobre un mismo frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #Creacion de la campana Gaussiana
        gauss = cv2.GaussianBlur(gray, (5,5),0)
        #Algoritmo de canny
        canny = cv2.Canny(gauss,50,150)
        #esta funcion hace que se resalte los bordes con color
        (contornos,_) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, 
                                        cv2.CHAIN_APPROX_SIMPLE)
        #Asignacion de color a los contornos en este caso de usar 
        #RGB para seleccionar el color rojo
        cv2.drawContours(frame,contornos,-1,(0,0,255), 2)

        # Frame guardado en archivo output
        out.write(frame)

        # Muestra de video con filtros en tiempo real
        cv2.imshow("Contornos",frame)

        # Fin de ciclo si se presiona ESCAPE
        key = cv2.waitKey(1)
        if key == 27:
                operation = False

    # Cerrar captura de video
    cap.release()

    # Cerrar archivo de output
    out.release()

    # Cerrar todas las ventanas creadas por el programa
    cv2.destroyAllWindow()
