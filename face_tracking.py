import cv2
import mediapipe as mp

# Inisialisasi
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success: break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        for landmarks in results.multi_face_landmarks:
            h, w, _ = frame.shape
            # Titik: 1(Hidung), 33(Mata L), 263(Mata R), 13(Mulut)
            for idx in [1, 33, 263, 13]:
                pt = landmarks.landmark[idx]
                cv2.circle(frame, (int(pt.x*w), int(pt.y*h)), 5, (0, 255, 0), -1)

    cv2.imshow('Tracking Wajah', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()