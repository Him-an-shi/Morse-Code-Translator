import cv2
import time
import os
from config import DOT_DASH_TIME, LETTER_GAP, WORD_GAP
from blink_detector import detect_eye_blink
from light_detector import detect_light_blink
from dictionary import decode_morse

# OUTPUT FILE SETUP 
FOLDER_NAME = "test"

# Create folder if it doesn't exist
os.makedirs(FOLDER_NAME, exist_ok=True)

file_name = input("Enter output file name (without extension): ").strip()
OUTPUT_FILE = os.path.join(FOLDER_NAME, f"{file_name}.txt")

# Clear previous content / create file
with open(OUTPUT_FILE, "w") as f:
    f.write("Decoded Morse Output:\n")

# MODE SELECTION 
print("\nSelect Mode:")
print("1 -> Eye Blink Morse")
print("2 -> Light Blink Morse")
mode = input("Enter choice (1/2): ").strip()

cap = cv2.VideoCapture(0)

signal_on = False
prev_signal = False
start_time = None
last_off_time = time.time()

current_morse = ""
decoded_text = ""

print("\nSystem started. Press Q or ESC to quit.\n")

# Create window explicitly
cv2.namedWindow("Vision-Based Morse Translator", cv2.WINDOW_NORMAL)

#  MAIN LOOP 
while True:
    ret, frame = cap.read()
    if not ret:
        break

    current_time = time.time()

    if mode == "1":
        signal_on, frame = detect_eye_blink(frame)
    else:
        signal_on, frame = detect_light_blink(frame)

    # Signal started
    if signal_on and not prev_signal:
        start_time = current_time

    # Signal ended
    if not signal_on and prev_signal:
        duration = current_time - start_time
        symbol = "." if duration < DOT_DASH_TIME else "-"
        current_morse += symbol
        last_off_time = current_time

    # Letter gap
    if not signal_on and (current_time - last_off_time) > LETTER_GAP and current_morse:
        letter = decode_morse(current_morse)
        decoded_text += letter

        with open(OUTPUT_FILE, "a") as f:
            f.write(letter)

        current_morse = ""
        last_off_time = current_time

    # Word gap
    if not signal_on and (current_time - last_off_time) > WORD_GAP:
        if decoded_text and decoded_text[-1] != " ":
            decoded_text += " "
            with open(OUTPUT_FILE, "a") as f:
                f.write(" ")

    prev_signal = signal_on

    # Display
    cv2.putText(frame, f"Decoded: {decoded_text}",
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (0, 255, 0), 2)

    cv2.putText(frame, "Press Q or ESC to quit",
                (10, 60), cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (255, 255, 255), 1)

    cv2.imshow("Vision-Based Morse Translator", frame)

    key = cv2.waitKey(10) & 0xFF
    if key == ord('q') or key == 27:
        break

# ================= CLEANUP =================
cap.release()
cv2.destroyAllWindows()

with open(OUTPUT_FILE, "a") as f:
    f.write("\n\n--- End of Session ---\n")

print("\nFinal Decoded Text:")
print(decoded_text)
print(f"\nSaved to: {OUTPUT_FILE}")
