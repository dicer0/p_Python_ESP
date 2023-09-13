import cv2
import os
import imutils
usuario = "di_cer0"
ruta = "ReconocimientoFacial_AsistenteVirtual_MarkI"
usuarioPath = ruta + "/" + usuario

if not os.path.exists(usuarioPath):
    os.makedirs(usuarioPath)
rostro = cv2.VideoCapture("C:/Users/diego/Pictures/Camera Roll/Rostro_di_cer0.mp4")
clasificacionFacial = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
numeroCara = 0
if not rostro.isOpened():
    print("No es posible abrir la cámara")
    exit()
while True:
    ret, frame = rostro.read()
    if not ret:
        print("No es posible obtener la imagen")
        break
    frame = imutils.resize(frame, width = 640)
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    imagenAuxiliar = frame.copy()

    caras = clasificacionFacial.detectMultiScale(img_gray, 1.3, 7)

    color_rectangulo = (0, 0, 255)
    grosor_rectangulo = 2
    for (x, y, ancho, altura) in caras:
        cv2.rectangle(frame, (x, y), (x + ancho, y + altura), color_rectangulo, grosor_rectangulo) 
        cara = imagenAuxiliar[y:y + altura, x:x + ancho]
        cara = cv2.resize(cara, (150, 150), interpolation = cv2.INTER_CUBIC)
        cv2.imwrite(usuarioPath + f"/cara_{numeroCara}.jpg", cara)
        numeroCara += 1
    cv2.imshow('Reconocimiento facial', frame)
    if (cv2.waitKey(1) == ord('r')) or (numeroCara >= 300):
        rostro.release()
        cv2.destroyAllWindows()
        break