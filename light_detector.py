import cv2
from config import LIGHT_THRESHOLD, ROI_SIZE

def detect_light_blink(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    h, w = gray.shape

    cx, cy = w // 2, h // 2
    roi = gray[cy-ROI_SIZE:cy+ROI_SIZE, cx-ROI_SIZE:cx+ROI_SIZE]
    brightness = roi.mean()

    blink = brightness > LIGHT_THRESHOLD

    cv2.rectangle(frame,
                  (cx-ROI_SIZE, cy-ROI_SIZE),
                  (cx+ROI_SIZE, cy+ROI_SIZE),
                  (255, 255, 0), 2)

    cv2.putText(frame, f"ROI Brightness: {int(brightness)}",
                (10, 90), cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (255, 255, 0), 2)

    return blink, frame
