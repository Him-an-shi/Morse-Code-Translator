# Vision-Based Morse Code Translator (Eye & Light Controlled)

A real-time computer vision–based system that translates eye blinks and blinking light signals into Morse code and readable text, enabling hands-free communication using a standard webcam.

---

## 📌 Overview

This project implements a vision-driven Morse code translation pipeline using Python, OpenCV, and MediaPipe. The system captures live video input, detects intentional eye blinks or light flashes, classifies them into Morse code symbols based on signal duration, and decodes them into readable text. Decoded output is displayed in real time and also saved persistently to a text file.

The project demonstrates practical applications of computer vision, signal timing analysis, and assistive technology design.

---

## ✨ Features

- 👁️ Eye blink–based Morse input using facial landmark detection  
- 💡 Light blink–based Morse input using ROI-based intensity analysis  
- ⏱️ Duration-based signal classification (dot, dash, letter gap, word gap)  
- 📄 Persistent text output saved to user-named files  
- 🧩 Modular architecture with clean separation of concerns  
- 🖥️ Real-time visual feedback with bounding boxes and decoded text  

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Computer Vision:** OpenCV  
- **Facial Landmark Detection:** MediaPipe Face Mesh  
- **Numerical Computing:** NumPy  
- **Version Control:** Git & GitHub  

---

## 📂 Project Structure

vision-morse-translator/
│
├── main.py               # Entry point and application control
├── config.py             # Configurable parameters and thresholds
├── blink_detector.py     # Eye blink detection logic
├── light_detector.py     # Light blink detection logic
├── dictionary.py         # Morse dictionary and decoding
├── test/                 # Folder for decoded text output files
├── requirements.txt      # Project dependencies
└── README.md

---

## ⚙️ Installation

1. Clone the repository
git clone https://github.com/Him-an-shi/DS_Mini-Project.git
cd vision-morse-translator

2. Install dependencies
pip install -r requirements.txt

▶️ How to Run
-python main.py
-Runtime Inputs
-Enter output file name (without extension)
-Choose input mode:
    1 → Eye Blink Morse
    2 → Light Blink Morse

Decoded text is displayed in real time and saved inside the test/ folder.

🧪 How It Works
-Captures live video input from a webcam
-Detects eye blinks or blinking light signals
-Measures signal duration to classify dots and dashes
-Identifies letter and word gaps using timing thresholds
-Decodes Morse code into readable text
-Displays and stores the decoded output