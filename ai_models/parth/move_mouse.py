# cursor customization file

from flask import Flask, request, jsonify
import pyautogui
import pyttsx3

app = Flask(__name__)

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

@app.route('/move_mouse', methods=['POST'])
def move_mouse():
    data = request.get_json()
    x = data.get('x')
    y = data.get('y')
    pyautogui.moveTo(x, y)
    return jsonify({'status': 'Mouse moved'})

@app.route('/click', methods=['POST'])
def click_mouse():
    pyautogui.click()
    return jsonify({'status': 'Mouse clicked'})

@app.route('/type', methods=['POST'])
def type_text():
    data = request.get_json()
    text = data.get('text')
    pyautogui.write(text)
    return jsonify({'status': 'Text typed'})

@app.route('/say', methods=['POST'])
def say_text():
    data = request.get_json()
    text = data.get('text')
    speak(text)
    return jsonify({'status': 'Spoken'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
