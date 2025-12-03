import cv2
import mediapipe as mp

# 1. Setup MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

# 2. Helper function to count fingers
def count_fingers(hand_landmarks):
    # Tip IDs for Thumb, Index, Middle, Ring, Pinky
    finger_tips = [4, 8, 12, 16, 20]
    
    count = 0
    
    # Logic for 4 fingers (Index to Pinky)
    # If the TIP (8) is higher than the PIP joint (6), it is OPEN.
    # Note: In image coordinates, "Higher" means a SMALLER Y value.
    if hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y: count += 1  # Index
    if hand_landmarks.landmark[12].y < hand_landmarks.landmark[10].y: count += 1 # Middle
    if hand_landmarks.landmark[16].y < hand_landmarks.landmark[14].y: count += 1 # Ring
    if hand_landmarks.landmark[20].y < hand_landmarks.landmark[18].y: count += 1 # Pinky
    
    # Logic for Thumb (It moves sideways, not up/down)
    # If thumb tip is to the left/right of the knuckle depending on hand side.
    # For simplicity here, we assume right hand facing camera:
    if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x: count += 1
    
    return count

cap = cv2.VideoCapture(0)

while True:
    success, image = cap.read()
    if not success: continue

    image = cv2.flip(image, 1) # Mirror effect
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    move = "Waiting..."

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Get the finger count
            fingers = count_fingers(hand_landmarks)
            
            # DECIDE THE MOVE
            if fingers == 0:
                move = "ROCK"
            elif fingers == 2:
                move = "SCISSORS"
            elif fingers == 5:
                move = "PAPER"
            else:
                move = f"Fingers: {fingers}"

    # Draw the text on the screen
    # (Image, Text, Position, Font, Scale, Color, Thickness)
    cv2.putText(image, str(move), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    cv2.imshow('Rock Paper Scissors AI', image)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()