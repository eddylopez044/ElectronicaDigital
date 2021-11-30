import pyfirmata 
import cv2
import mediapipe as mp 
import math

puerto = "/dev/ttyUSB0"
print("Conectando con Arduino por USB...")
tarjeta = pyfirmata.Arduino(puerto)

def numero(n):
    for i in range(6, 13):
        tarjeta.digital[i].write(0)
    if n == 0:
        for i in range(6, 13):
            if not i == 7:
                tarjeta.digital[i].write(1)
    elif n == 1:
        tarjeta.digital[6].write(1)
        tarjeta.digital[8].write(1)
    elif n == 2:
        tarjeta.digital[11].write(1)
        tarjeta.digital[6].write(1)
        tarjeta.digital[7].write(1)
        tarjeta.digital[10].write(1)
        tarjeta.digital[9].write(1)
    elif n == 3:
        tarjeta.digital[11].write(1)
        tarjeta.digital[6].write(1)
        tarjeta.digital[7].write(1)
        tarjeta.digital[8].write(1)
        tarjeta.digital[9].write(1)
    elif n == 4:
        tarjeta.digital[12].write(1)
        tarjeta.digital[7].write(1)
        tarjeta.digital[6].write(1)
        tarjeta.digital[8].write(1)
    elif n == 5:
        tarjeta.digital[11].write(1)
        tarjeta.digital[12].write(1)
        tarjeta.digital[7].write(1)
        tarjeta.digital[8].write(1)
        tarjeta.digital[9].write(1)
    elif n == 6:
        tarjeta.digital[11].write(1)
        tarjeta.digital[12].write(1)
        tarjeta.digital[7].write(1)
        tarjeta.digital[10].write(1)
        tarjeta.digital[8].write(1)
        tarjeta.digital[9].write(1)
    elif n == 7:
        tarjeta.digital[11].write(1)
        tarjeta.digital[6].write(1)
        tarjeta.digital[8].write(1)
    elif n == 8:
        for i in range(6, 13):
            tarjeta.digital[i].write(1)
    elif n == 9:
        for i in range(6, 13):
            if not i == 10:
                tarjeta.digital[i].write(1)
    elif n == 13:
        for i in range(5, 13):
            tarjeta.digital[i].write(0)
    else:
        tarjeta.digital[5].write(1)
    
                
mp_drawing = mp.solutions.drawing_utils
mo_hands = mp.solutions.hands
cap = cv2.VideoCapture(0)
aux = []
numero(0)
with mo_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5) as hands:
    
    while True:
        ret, frame = cap.read()
        if ret == False:
            break
        
        height, width, _ = frame.shape
        frame = cv2.flip(frame,1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        result = hands.process(frame_rgb)
        
        if result.multi_handedness is not None:
            mano = str(result.multi_handedness[0]).split('\n')[3].split(" ")[3]
            #print(mano)
            if mano == '"Right"':
                numero(11)
            elif mano == '"Left"':
                numero(51)
        else:
            numero(13)
        
            
        if result.multi_hand_landmarks is not None:
            for hand_landmarks in result.multi_hand_landmarks:
                #mp_drawing.draw_landmarks(frame, hand_landmarks, mo_hands.HAND_CONNECTIONS)
                
                ################dedo pequeño###############################################
                unoX = int(hand_landmarks.landmark[mo_hands.HandLandmark.PINKY_TIP].x*width)
                unoY = int(hand_landmarks.landmark[mo_hands.HandLandmark.PINKY_TIP].y*height)
                unoCX = int(hand_landmarks.landmark[mo_hands.HandLandmark.PINKY_MCP].x*width)
                unoCY = int(hand_landmarks.landmark[mo_hands.HandLandmark.PINKY_MCP].y*height)
                distancia = math.sqrt((unoCX-unoX)**2+(unoCY-unoY)**2)
                
                ################dedo pequeño###############################################
                dosX = int(hand_landmarks.landmark[mo_hands.HandLandmark.RING_FINGER_TIP].x*width)
                dosY = int(hand_landmarks.landmark[mo_hands.HandLandmark.RING_FINGER_TIP].y*height)
                dosCX = int(hand_landmarks.landmark[mo_hands.HandLandmark.RING_FINGER_MCP].x*width)
                dosCY = int(hand_landmarks.landmark[mo_hands.HandLandmark.RING_FINGER_MCP].y*height)
                distancia1 = math.sqrt((dosCX-dosX)**2+(dosCY-dosY)**2)
                
                ################dedo pequeño###############################################
                tresX = int(hand_landmarks.landmark[mo_hands.HandLandmark.MIDDLE_FINGER_TIP].x*width)
                tresY = int(hand_landmarks.landmark[mo_hands.HandLandmark.MIDDLE_FINGER_TIP].y*height)
                tresCX = int(hand_landmarks.landmark[mo_hands.HandLandmark.MIDDLE_FINGER_MCP].x*width)
                tresCY = int(hand_landmarks.landmark[mo_hands.HandLandmark.MIDDLE_FINGER_MCP].y*height)
                distancia2 = math.sqrt((tresCX-tresX)**2+(tresCY-tresY)**2)
                
                ################dedo pequeño###############################################
                cuatroX = int(hand_landmarks.landmark[mo_hands.HandLandmark.INDEX_FINGER_TIP].x*width)
                cuatroY = int(hand_landmarks.landmark[mo_hands.HandLandmark.INDEX_FINGER_TIP].y*height)
                cuatroCX = int(hand_landmarks.landmark[mo_hands.HandLandmark.INDEX_FINGER_MCP].x*width)
                cuatroCY = int(hand_landmarks.landmark[mo_hands.HandLandmark.INDEX_FINGER_MCP].y*height)
                distancia3 = math.sqrt((cuatroCX-cuatroX)**2+(cuatroCY-cuatroY)**2)
                
                ################dedo pequeño###############################################
                cincoX = int(hand_landmarks.landmark[mo_hands.HandLandmark.THUMB_TIP].x*width)
                cincoY = int(hand_landmarks.landmark[mo_hands.HandLandmark.THUMB_TIP].y*height)
                distancia4 = math.sqrt((unoX-cincoX)**2+(unoY-cincoY)**2)
                dedos =0
                if distancia > 50:
                    dedos+=1
                if distancia1 > 50:
                    dedos+=1
                if distancia2 > 50:
                    dedos+=1
                if distancia3 > 50:
                    dedos+=1
                if distancia4 > 140:
                    dedos+=1
                print(dedos, distancia4)
                numero(dedos)
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
        
cap.release()
cv2.destroyAllWindows()