import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    h, w, _ = frame.shape
    
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    #if results.multi_hand_landmarks:
    #    for landmarks in results.multi_hand_landmarks:
    #        mp_drawing.draw_landmarks(
    #            frame, landmarks, mp_hands.HAND_CONNECTIONS)

    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            for idx, landmark in enumerate(landmarks.landmark):
                cx, cy = int(landmark.x * w), int(landmark.y * h)
                # Draw a circle with the landmark ID
                cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)
                cv2.putText(frame, str(idx), (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    cv2.imshow('Hand Tracking', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
hands.close()
