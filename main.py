import speech_recognition as sr
import pyttsx3
from datetime import datetime
import requests
import json
import pvporcupine
import pyaudio
import struct
import random
# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Porcupine wake word detection
access_key = "BGaqXL72T+IExKK42fq4tW1BR2dncsKfEY0J5oC8NPKFVxZCb9qk6A=="  # Replace with your actual Picovoice access key
porcupine = pvporcupine.create(access_key=access_key, keywords=["hey google", "terminator", "alexa", "picovoice", "jarvis"])
pa = pyaudio.PyAudio()
audio_stream = pa.open(
    rate=porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=porcupine.frame_length
)


def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()


def get_greeting():
    """Get an appropriate greeting based on the current time."""
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        return "Good morning"
    elif 12 <= current_hour < 18:
        return "Good afternoon"
    elif 18 <= current_hour < 22:
        return "Good evening"
    else:
        return "Good night"


def get_weather():
    """Fetch the current weather from OpenWeatherMap."""
    api_key = "867ebae30919133c3fd40693469a7e62"
    city = "Toronto"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    weather_data = response.json()
    if response.status_code == 200:
        temp = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        return f"The current temperature in {city} is {temp} degrees Celsius with {description}."
    else:
        return "Sorry, I couldn't fetch the weather information."


def get_time():
    """Return the current time."""
    current_time = datetime.now().strftime("%I:%M %p")
    return f"The current time is {current_time}."


def get_date():
    """Return the current date."""
    current_date = datetime.now().strftime("%B %d, %Y")
    return f"Today is {current_date}."


def give_compliment():
    """Give a random compliment."""
    compliments = [
        "You are doing a great job!",
        "You are amazing!",
        "You have a great sense of humor!",
        "You're incredibly smart!"
    ]
    return random.choice(compliments)



def calculate(command):
    """Handle basic arithmetic calculations."""
    try:
        result = eval(command)
        return f"The result is {result}."
    except Exception as e:
        return "Sorry, I couldn't perform the calculation."


def listen_for_command():
    """Listen for commands and act accordingly."""
    print("Listening for 'Hey Assistant'...")
    pcm_data = audio_stream.read(porcupine.frame_length)
    pcm_data = struct.unpack_from("h" * porcupine.frame_length, pcm_data)
    keyword_index = porcupine.process(pcm_data)

    if keyword_index >= 0:
        speak("I'm listening, what can I do for you?")
        with sr.Microphone() as source:
            # Adjust settings to improve recognition accuracy
            recognizer.energy_threshold = 3000
            recognizer.pause_threshold = 1

            audio = recognizer.listen(source)
            try:
                command = recognizer.recognize_google(audio).lower()
                print(f"Recognized command: {command}")

                # Handle different commands
                if "weather" in command:
                    weather_info = get_weather()
                    speak(weather_info)
                elif "time" in command:
                    time_info = get_time()
                    speak(time_info)
                elif "date" in command:
                    date_info = get_date()
                    speak(date_info)
                elif "compliment me" in command:
                    compliment = give_compliment()
                    speak(compliment)

                elif "calculate" in command:
                    calculation = command.replace("calculate", "").strip()
                    result = calculate(calculation)
                    speak(result)
                else:
                    speak("Sorry, I didn't understand that command.")
            except sr.UnknownValueError:
                speak("Sorry, I didn't catch that.")
            except sr.RequestError:
                speak("Speech service seems unavailable.")


def customize_voice():
    """Allow user to select between different voice types."""
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Switch to a different voice, e.g., female


# Customize voice before starting
customize_voice()

# Main loop to keep listening for the command
try:
    while True:
        listen_for_command()
except KeyboardInterrupt:
    print("Shutting down...")
finally:
    if porcupine is not None:
        porcupine.delete()
    if audio_stream is not None:
        audio_stream.close()
    if pa is not None:
        pa.terminate()
