# 🚗 Voice-Controlled Car using Python & Arduino

A **voice-controlled car** project where you can control the movement of a robotic car using **voice commands**.  
This project uses **Python**, **SpeechRecognition**, and **Arduino** (via PyFirmata) to control motors in real-time.

---

## 🛠 Technologies Used
- **Python**  
  - `speech_recognition` – To capture and process voice commands  
  - `difflib` – For matching spoken words to valid commands  
  - `pyfirmata` – To communicate with Arduino  
- **Arduino** – Motor control  
- **PWM Motor Drivers** – For speed control of motors  

---

## ⚡ Features
- Real-time voice recognition for car commands  
- Supports commands:
  - 🟢 `forward` – Move car forward  
  - 🟢 `backward` – Move car backward  
  - 🟢 `left` – Turn left  
  - 🟢 `right` – Turn right  
  - 🛑 `stop` – Stop movement  
  - 🔴 `exit` / `quit` / `stop listening` – Stop voice control  
- Automatically adjusts for ambient noise  
- Logs recognized commands to a file  

---

## 🧠 How It Works

SpeechRecognition listens to your microphone and captures audio.

The audio is converted to text using Google Speech Recognition.

The recognized text is matched to valid commands using difflib.

Arduino receives the command via PyFirmata and controls the motors:

Forward / Backward – Both motors move in same direction

Left / Right – One motor stops or reverses for turning

Stop – Motors stop

Commands are logged in commands_log.txt for debugging.

---

## 🔗 References

PyFirmata Documentation

SpeechRecognition Python

Arduino PWM Motor Control

---



## 💻 How to Run
1. Connect Arduino to your computer (e.g., COM8).  
2. Clone the repository:
```bash
git clone https://github.com/Rou-maissa/Voice_controlled_Car.git

