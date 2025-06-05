# Python-Projects
This Github repository contains 5 great projects on python 


# 🐍 Python Projects Collection 🚀  
👨‍💻 Created by **Rohit Pawale**

Welcome to my curated collection of beginner-to-intermediate level **Python Projects**. Each project showcases the application of core Python concepts, various libraries, and real-world use cases. Dive in and explore! 🔍

---

## 📁 Projects Overview

1. [🤖 Robo Speaker]((https://github.com/Rohitpawale23/Python-Projects/tree/main/01_RoboSpeaker))
2. [🌦️ Weather App](https://github.com/Rohitpawale23/Python-Projects/tree/main/02_WeatherApp)
3. [🖼️ Image Resizer](https://github.com/Rohitpawale23/Python-Projects/tree/main/03_ImageReisizer)
4. [📚 PDF Merger](https://github.com/Rohitpawale23/Python-Projects/tree/main/04_PDF_Merger)
5. [🧠 Facial Recognition Attendance System](https://github.com/Rohitpawale23/Python-Projects/tree/main/05_FacialReocgAttendanceSystem)

---

## 1. 🤖 Robo Speaker

🔊 A simple speech assistant that speaks what the user types using **`pyttsx3`** or **Windows PowerShell TTS**.

### 🛠 Features:
- Takes user input and converts it to speech
- Says goodbye when exited
- Offline functionality (no internet required)
- Version 1.1 used PowerShell; 2.1 uses `pyttsx3` for better control

---

## 2. 🌦️ Weather App

☁️ A console-based weather reporting app that fetches **real-time weather** data using the **WeatherAPI** and speaks the result.

### 🛠 Features:
- Fetches temperature (°C and °F) and weather conditions
- Uses `requests` and `json` modules to parse API data
- Uses `pyttsx3` to speak weather details
- Clean and simple CLI design

📌 Requires a valid [WeatherAPI](https://www.weatherapi.com/) key

---

## 3. 🖼️ Image Resizer

🧩 A utility to resize images using **OpenCV**.

### 🛠 Features:
- Reads and resizes an image by a defined percentage
- Saves the resized image to a new file
- Can be integrated into automation pipelines
- Uses `cv2.imread()`, `cv2.resize()`, and `cv2.imwrite()`

🧠 Tip: Works with `.jpg`, `.png`, etc.

---

## 4. 📚 PDF Merger

📎 A Python script to **merge multiple PDF files** into a single document using `PyPDF2`.

### 🛠 Features:
- Combines two or more PDF files into one
- Lightweight and minimal code
- Customizable list of PDF files
- Generates `merged.pdf` as output

---

## 5. 🧠 Facial Recognition Attendance System

📷 A real-time attendance system using **Face Recognition** and **OpenCV**.

### 🛠 Features:
- Recognizes multiple known faces via webcam
- Writes present students' names with timestamps into a CSV file
- Displays real-time video feed with overlayed text
- Uses `face_recognition`, `cv2`, `numpy`, `datetime`, and `csv`
- Automatically saves attendance with the current date as filename

⚠️ Preload images for each known face inside a `Faces/` folder for best accuracy.

---

