import cv2
import numpy as np
import mediapipe as mp
from config import EAR_THRESHOLD

LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

def euclidean(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

def eye_aspect_ratio(eye, points):
    v1 = euclidean(points[eye[1]], points[eye[5]])
    v2 = euclidean(points[eye[2]], points[eye[4]])
    h = euclidean(points[eye[0]], points[eye[3]])
    return (v1 + v2) / (2.0 * h)

def detect_eye_blink(frame):
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if not results.multi_face_landmarks:
        return False, frame

    h, w, _ = frame.shape
    landmarks = results.multi_face_landmarks[0].landmark
    points = [(int(l.x * w), int(l.y * h)) for l in landmarks]

    left_ear = eye_aspect_ratio(LEFT_EYE, points)
    right_ear = eye_aspect_ratio(RIGHT_EYE, points)
    ear = (left_ear + right_ear) / 2.0

    blink = ear < EAR_THRESHOLD
    color = (0, 0, 255) if blink else (0, 255, 0)

    for eye in [LEFT_EYE, RIGHT_EYE]:
        xs = [points[i][0] for i in eye]
        ys = [points[i][1] for i in eye]
        cv2.rectangle(frame,
                      (min(xs)-8, min(ys)-8),
                      (max(xs)+8, max(ys)+8),
                      color, 2)

    cv2.putText(frame, f"EAR: {ear:.2f}",
                (10, 60), cv2.FONT_HERSHEY_SIMPLEX,
                0.6, color, 2)

    return blink, frame
