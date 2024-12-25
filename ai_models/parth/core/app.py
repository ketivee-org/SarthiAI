import cv2
import numpy as np
import pytesseract
import pyttsx3
import speech_recognition as sr
import pyautogui

import time

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Path to tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Recognizer for speech
recognizer = sr.Recognizer()

# Function to read the screen text
def read_screen():
    # Take a screenshot
    screenshot = pyautogui.screenshot()
    screen_np = np.array(screenshot)

    # Convert the image to grayscale
    gray_screen = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)

    # Use pytesseract to extract text
    text = pytesseract.image_to_string(gray_screen)

    return text.strip()

# Function to get user input through voice
def get_voice_input():
    with sr.Microphone() as source:
        print("Listening for user voice input...")
        engine.say("Please tell me how can I assist you?")
        engine.runAndWait()

        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None

# Function to get text input from the user
def get_text_input():
    engine.say("Please type your input.")
    engine.runAndWait()
    return input("Please enter your input: ")

# Function to interact based on screen or user input
def assist_user(screen_text, user_input):
    if "new tool" in screen_text.lower() or "help" in user_input.lower():
        engine.say("It looks like you need help with a new tool. Do you need guidance?")
        engine.runAndWait()
        guide_user_through_tool()

    elif "open" in user_input.lower():
        open_program(user_input)
    
    elif "click" in user_input.lower():
        click_on_coordinates()

    elif "type" in user_input.lower():
        text_to_type = user_input.split("type ")[1]
        pyautogui.write(text_to_type)

def guide_user_through_tool():
    engine.say("It looks like you are using a new tool. Let me assist you by guiding you through the basics.")
    engine.runAndWait()

    # Simulate guiding user
    engine.say("To get started, open the menu from the top-left corner. From there, you can create a new project.")
    engine.runAndWait()

    # Example of moving the mouse and clicking
    pyautogui.moveTo(100, 100)
    pyautogui.click()

    engine.say("Now, select the option 'New Project'. Let me know if you need further help.")
    engine.runAndWait()

# Function to open a program based on user input
def open_program(command):
    if "browser" in command.lower():
        engine.say("Opening browser...")
        engine.runAndWait()
        pyautogui.hotkey("win", "r")
        time.sleep(1)
        pyautogui.write("chrome")
        pyautogui.press("enter")
    
    elif "notepad" in command.lower():
        engine.say("Opening Notepad...")
        engine.runAndWait()
        pyautogui.hotkey("win", "r")
        time.sleep(1)
        pyautogui.write("notepad")
        pyautogui.press("enter")

# Function to click on specific screen coordinates
def click_on_coordinates():
    engine.say("Please tell me where you want to click.")
    engine.runAndWait()
    x, y = map(int, input("Enter X and Y coordinates (separated by a space): ").split())
    pyautogui.moveTo(x, y)
    pyautogui.click()

# Main loop
def main():
    while True:
        # Read the screen content in real-time
        screen_text = read_screen()
        print("Screen text:", screen_text)

        # Ask user for input
        user_input = get_voice_input() if input("Voice input (v) or text input (t)? ").lower() == 'v' else get_text_input()

        # Assist user based on screen and input
        assist_user(screen_text, user_input)

        # Exit condition (you can modify this)
        if "exit" in user_input.lower():
            engine.say("Exiting the assistant.")
            engine.runAndWait()
            break

if __name__ == "__main__":
    main()
