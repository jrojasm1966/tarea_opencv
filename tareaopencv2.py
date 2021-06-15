# ********************************************************************************
# Prueba 3 - Python - Jorge Rojas Moena
# Parte 2: Entregar a mas tardar al Inicio de Clase Martes 15 Junio 2021
# Ver enlace: https://realpython.com/face-detection-in-python-using-a-webcam/
# ********************************************************************************

import sys
# *******************************************************************
# Función detectaRostoEnWebCam(foto) que Detecta Rostros en WEBCAM
# Utiliza la biblioteca de código abierto OpenCV 
# *******************************************************************
def detectaRostroEnWebCam():
    import cv2

    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)

    video_capture = cv2.VideoCapture(0)

    while (True):
        # Capture frame-by-frame - Captura Cuadro por Cuadro
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        
        # Draw a rectangle around the faces - Dibuja un rectángulo alrededor de las caras
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the resulting frame - Despliega el resultado del cuadro
        cv2.imshow("** WEBCAM ACTIVA ** - Detectando Rostros !!!", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture - Cuando todo esté hecho, livera la captura realizada
    video_capture.release()
    
    # Termina con las sesiones abiertas por la captura
    cv2.destroyAllWindows()

# ******************************************************************************
# Función ingresaOpcion(num) que Despliega el Menú a detectar Rostros en WebCam
# Devuelve el número correspondiente para ingresar o SALIR
# ******************************************************************************
def ingresaOpcion(num):
    print('')
    print("*********************************************************************")
    print("*              Menú WebCam para Detectar Rostros                    *")
    print("*********************************************************************")
    print("*              ¡¡¡¡ RECUERDE SI SE ABRE LA WEBCAM  !!!!             *")
    print("*   ¡¡¡ PARA SALIR/TERMINAR PRESIONE LA TECLA q (minúscula ) !!!    *")
    print("*********************************************************************")
    print("*              OPCIONES Menú WebCam ( 0 / 1 )                       *")
    print("*********************************************************************")
    print("*     0.- SALIR de la aplicación ( Ingrese cero )                   *")
    print("*     1.- Ingresar a WebCam - Detectar Rostros ( Ingrese uno )      *")
    print("*********************************************************************")
    print('')   
    num = int(input("Ingrese Opción para detectar Rostro WEBCAM : "))
    print('')   

    return num

# ***************************************************************************************
# Función decideVerOtraVez(resp) que permite al usuario decidir si continúa viendo más 
# en la WebCam - Devuelve valor booleano si decide continuar en el programa o no
# ***************************************************************************************
def decideVerOtraVez(resp):
    SioNo = ""
    while SioNo not in ("N","S"):
        SioNo = input("¿ Quieres nuevamente entrar a WEBCAM ? : S / N (Mayúscula): ")
    if SioNo == "S":
        resp = True
    else: resp = False
    return resp

# ****************************************************************************************
# Función Principal cicloRevisaWebCam() que controla el mantener al usuario en el programa
# ****************************************************************************************
def cicloRevisaWebCam():
    num = 0
    opcMenu = 0
    respuesta = True
    
    while respuesta:
            opcMenu = ingresaOpcion(num)
            if opcMenu == 0:
                respuesta = False
            else:
                if opcMenu == 1:
                    print('')  
                    detectaRostroEnWebCam()
                    print('')   
                    print('')   
                    print("¿¿¿ Que te pareció ???")
                    print('')   
                    resp = False
                    respuesta = decideVerOtraVez(resp)
                else: 
                    print("***********************************************")
                    print("  ERROR : ¡¡¡¡ Número ingresado NO EXISTE !!!! ")
                    print("-----------¡¡ Ingresa nuevamente !!------------")
                    print("***********************************************")
                    print("")

    if not respuesta:
        print("**********************")
        print("¡¡¡¡ Hasta Pronto !!!!")
        print("**********************")


# **************************************************
# Llamada a Función Principal y Termino de Programa
# **************************************************
cicloRevisaWebCam()
sys.exit()

