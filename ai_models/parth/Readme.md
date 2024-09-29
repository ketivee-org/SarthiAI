# ParthAI

note : -- This ai model is part of SarthiAI devlopment program 

This AI Assistant is designed to help users interact with new tools or programs on their computers, even if they have no prior experience with those tools. The assistant can read the user's screen in real-time, accept user input via voice or text, and then control the device to provide guidance or perform tasks.

Features
Real-time Screen Reading: Captures and reads the text from the user's screen using computer vision (OpenCV and PyTesseract).
Voice and Text Input: Accepts user commands through either text input or voice recognition.
Voice Interaction: Provides real-time feedback and instructions to the user using a text-to-speech engine.
Program Control: Controls the mouse and keyboard to interact with the computer (e.g., clicking buttons, typing text, opening programs).
Tool Guidance: Assists the user by guiding them through unfamiliar software tools.
Requirements
To run the AI assistant, you'll need the following Python libraries:

bash
Copy code
pip install opencv-python pytesseract SpeechRecognition pyttsx3 pyautogui keyboard
Additionally, for text recognition, you'll need to install Tesseract-OCR and add it to your system path.

Tesseract Installation:
Windows: Download the Tesseract installer from here, install it, and make sure to add the installation path to your system environment variables.
Usage
1. Screen Text Recognition
The assistant uses pyautogui to capture the screen and pytesseract to extract text. This allows the AI to understand what is currently on the user's screen and provide context-sensitive assistance.

1. Voice Commands
The AI can listen to the user's voice input using SpeechRecognition. It processes voice commands and performs corresponding actions, such as opening programs or providing guidance.

1. Text Input
If voice input is not available or preferred, the user can interact with the assistant through text input. The AI will respond based on the user's commands.

1. Real-time Feedback and Assistance
Using pyttsx3, the AI provides spoken feedback and instructions to the user. It can guide the user through the use of new tools, offering help when needed.

1. Program Interaction
The assistant uses pyautogui to control the mouse and keyboard. It can:

Open programs (e.g., browser, Notepad)
Click on specified coordinates on the screen
Type text automatically
How It Works
The AI captures the screen content and extracts the visible text using Optical Character Recognition (OCR).
The user can give input either by voice or by typing. If voice is selected, the AI listens for the command using a microphone.
Based on the detected screen content and user input, the AI responds by:
Giving instructions on how to use a program
Opening a program
Performing clicks or typing on behalf of the user
The AI provides real-time spoken feedback using text-to-speech to guide the user step by step.
File Structure
bash
Copy code
/AI-Assistant
│
├── assistant.py               # Main script that runs the AI assistant
├── README.md                  # Documentation for the project
├── requirements.txt           # Required libraries for the project
└── .gitignore                 # Git ignore file
Example Usage
To run the assistant, simply execute the main Python script:

bash
Copy code
python assistant.py
Voice Interaction: When prompted, choose whether to use voice or text input. If using voice, the AI will listen and respond to commands.
Text Input: If using text input, the AI will ask for user commands and respond accordingly.
Program Guidance: The AI will detect if you're interacting with a new tool and offer help.
Extending the Assistant
You can extend the assistant to support additional features:

Advanced Voice Commands: Add more specific commands for controlling the system (e.g., closing applications, adjusting volume).
New Tool Assistance: Implement tool-specific guidance by detecting specific elements on the screen (e.g., menus, buttons).
Custom Actions: Add new actions that the AI can perform, such as controlling hardware, adjusting system settings, or providing software tutorials.
Troubleshooting
Tesseract not detecting text: Ensure that Tesseract is installed correctly and added to your system path.
Microphone issues: If the AI isn't picking up your voice, check that your microphone is set up and working correctly in your system settings.
Program control issues: If the AI isn't clicking or typing correctly, check that pyautogui is properly installed and that you're running the program with the necessary permissions.
License
This project is licensed under the MIT License. You are free to use, modify, and distribute it as long as the original license is included.

Contributing
Contributions are welcome! Feel free to submit pull requests or open issues for feature requests or bug reports.


