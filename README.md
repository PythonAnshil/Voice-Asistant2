<<<<<<< HEAD
# Voice Assistant Project

This is a simple Python-based voice assistant project that uses voice commands to provide various functionalities, such as telling the current time, date, weather, giving compliments, and performing basic calculations. The assistant also responds to a wake word using the Picovoice Porcupine library for wake-word detection.

## Features

- **Wake Word Detection**: The assistant uses Picovoice's Porcupine library to detect wake words like "Hey Google", "Alexa", "Jarvis", and others.
- **Weather Information**: Provides the current weather information for Toronto using the OpenWeatherMap API.
- **Time and Date**: Responds with the current time and date.
- **Compliments**: Offers a random compliment when asked.
- **Basic Calculations**: Can perform simple arithmetic calculations.

## Requirements

To run this project, you'll need the following Python libraries:

- `speech_recognition` for recognizing voice commands
- `pyttsx3` for text-to-speech conversion
- `requests` for fetching weather data
- `pvporcupine` for wake-word detection
- `pyaudio` for audio input

You can install these libraries using pip:

```sh
pip install SpeechRecognition pyttsx3 requests pvporcupine pyaudio
```

Additionally, you will need an access key for Picovoice Porcupine and an API key for OpenWeatherMap.

## Setup Instructions

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/PythonAnshil/Voice-Asistant2.git
   cd Voice-Asistant2
   ```

2. **Install Dependencies**:
   Install the required Python libraries as mentioned above.

3. **Configure API Keys**:
   - Replace `YOUR_ACCESS_KEY` in the code with your Picovoice access key.
   - Replace `YOUR_OPENWEATHERMAP_API_KEY` in the code with your OpenWeatherMap API key.

4. **Run the Program**:
   ```sh
   python main.py
   ```

## Usage

- Say a wake word like "Hey Google" or "Jarvis" to activate the assistant.
- You can ask the assistant for the current time, date, weather, or even a compliment.
- To perform a calculation, say "calculate" followed by the arithmetic operation (e.g., "calculate 5 plus 3").

## Example Commands

- "Hey Google, what is the weather today?"
- "Hey Jarvis, what time is it?"
- "Hey Alexa, compliment me."
- "Hey Assistant, calculate 10 divided by 2."

## Known Issues

- The assistant may have difficulty recognizing certain phrases in noisy environments.
- The wake word detection is limited to the keywords provided by Picovoice.

## Contributing

Feel free to fork the repository and contribute improvements. Pull requests are welcome!

## License

This project is licensed under the MIT License.

=======
# Voice-Asistant2
>>>>>>> 67f615c2d04601dbfea97354d65ad374443dd289
