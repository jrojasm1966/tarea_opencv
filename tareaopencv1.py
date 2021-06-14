# ********************************************************************************
# Prueba 3 - Python - Jorge Rojas Moena
# Parte 1: Entregar a mas tardar al Inicio de Clase Lunes 14 Junio 2021
# Ver Información en enlace: https://realpython.com/face-recognition-with-python/
# ********************************************************************************

import sys
# ***************************************************************************************
# Función detectaRostoEnFoto(foto) que Detecta Rostros en foto elegida por el usuario
# Utiliza la biblioteca de código abierto OpenCV 
# ***************************************************************************************
def detectaRostoEnFoto(foto):
    import cv2

    # Get user supplied values - Obtener valores proporcionados por el usuario
    imagePath = foto
    cascPath = "haarcascade_frontalface_default.xml"

    # Create the haar cascade - Se crea la cascada para la imagen
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image - Leer la imagen
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image - Detecta rostros en la imagen
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    if len(faces) > 1:
        print("Detectados {0} Rostros!".format(len(faces)))
    else: print("Detectado {0} Rostro!".format(len(faces)))

    # Draw a rectangle around the faces - Dibuja un rectángulo alrededor de las caras
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    if len(faces) > 1: 
        cv2.imshow("Rostros Encontrados en Foto : "+imagePath, image)
    else: cv2.imshow("Rostro Encontrado en Foto : "+imagePath, image)
    
    print("PRESIONE ENTER PARA CONTINUAR......")
    cv2.waitKey(0)
    
    cv2.destroyAllWindows()

# ***************************************************************************************
# Función ingresaFoto(num) que Despliega el Menú de Fotos disponibles a detectar Rostros
# Devuelve el número correspondiente a uno de los diccionarios de la lista de fotos
# ***************************************************************************************
def ingresaFoto(num):
    print('')
    print("***************************************")
    print("* Menú de Fotos para Detectar Rostros *")
    print("***************************************")
    print('')
    for i in range(len(fotos)):
        print(str(i+1)+".- Foto "+fotos[i]['foto']+ ", Nombre Foto - " +fotos[i]['nombre'])

    print(str(len(fotos)+1)+".- Para SALIR ingrese 0 ( Cero )")
    print('')   
    num = int(input("Ingrese número de Foto a detectar Rostro: "))
    print('')   

    return num

# ***************************************************************************************
# Función decideVerOtraFoto(resp) que permite al usuario decidir si continúa viendo más 
# fotos del menú - Devuelve valor booleano si decide continuar en el programa o no
# ***************************************************************************************
def decideVerOtraFoto(resp):
    SioNo = ""
    while SioNo not in ("N","S"):
        SioNo = input("¿ Quieres nuevamente ver otra foto ? : S / N : ")
    if SioNo == "S":
        resp = True
    else: resp = False
    return resp
    

# ***************************************************************************************
# Función Principal cicloRevisaFotos() que controla el mantener al usuario en el programa
# ***************************************************************************************
def cicloRevisaFotos():
    num=0
    respuesta = True
    
    while respuesta:
            numfoto = ingresaFoto(num)
            if numfoto == 0:
                respuesta = False
            else:
                if numfoto > 0 and numfoto < 8:
                    print('')   
                    fotoelegida = fotos[numfoto-1]['nombre']
                    detectaRostoEnFoto(fotoelegida)
                    print("¿¿¿ Que te pareció ???")
                    print('')   
                    resp = False
                    respuesta = decideVerOtraFoto(resp)
                else: 
                    print("****************************************************")
                    print("ERROR : ¡¡¡¡ Número de Foto ingresada NO EXISTE !!!!")
                    print("-------------¡¡ Ingresa nuevamente !!---------------")
                    print("****************************************************")
                    print("")

    if not respuesta:
        print("**********************")
        print("¡¡¡¡ Hasta Pronto !!!!")
        print("**********************")

# ******************************************************************
# Lista de Diccionarios con Fotos Disponibles y Rostros a Detectar
# ******************************************************************
fotos = [
        {'foto':  'Rostro Mujer', 'nombre' : 'UnRostro.jpg'},
        {'foto':  'Rostros de Chilenos(as)', 'nombre' : 'rostros-chilenos.jpg'},
        {'foto':  'Rostros Actrices Famosas', 'nombre' : 'actricesFamosas.jpg'},
        {'foto':  'Rostros Modelos Mujeres', 'nombre' : 'Modelos-mujeres.jpg'},
        {'foto':  'Rostros y Personalidad', 'nombre' : 'forma-rostro-personalidad.jpg'},
        {'foto':  'Rostros Futbolistas Veteranos', 'nombre' : 'futbolistasveteranos.jpg'},
        {'foto':  'Rostros Futbolistas TOP', 'nombre' : 'ronaldo-neymar-messi.jpg'}
    ]

# **************************************************
# Llamada a Función Principal y Termino de Programa
# **************************************************
cicloRevisaFotos()
sys.exit()
