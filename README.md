# Python-Projects
This Github repository contains 5 great projects on python 


# 🐍 Python Projects Collection 🚀  
👨‍💻 Created by **Rohit Pawale**

Welcome to my curated collection of beginner-to-intermediate level **Python Projects**. Each project showcases the application of core Python concepts, various libraries, and real-world use cases. Dive in and explore! 🔍

---

## 📁 Projects Overview

1. [🤖 Robo Speaker](#1-🤖-robo-speaker)
2. [🌦️ Weather App](#2-🌦️-weather-app)
3. [🖼️ Image Resizer](#3-🖼️-image-resizer)
4. [📚 PDF Merger](#4-📚-pdf-merger)
5. [🧠 Facial Recognition Attendance System](#5-🧠-facial-recognition-attendance-system)

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

## 🛠 Requirements

Install all required libraries using:

```bash
pip install -r requirements.txt
