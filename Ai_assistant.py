import speech_recognition as sr
import pyttsx3
import random

# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 160)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print("You:", command)
        return command.lower()
    except:
        speak("Sorry, I didn't get that.")
        return ""

# Question and Answer list
qa_pairs = {
    "what is your name": ["I am your assistant.", "You can call me AI bot."],
    "how are you": ["I'm doing great!", "Feeling awesome!"],
    "what can you do": ["I can talk with you!", "I can answer your questions."],
    "who created you": ["I was created by you!", "You're my creator."],
    "tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!", 
                       "Why did the math book look sad? Because it had too many problems."]
}

def respond_to_question(question):
    for q in qa_pairs:
        if q in question:
            return random.choice(qa_pairs[q])
    return "I don't know the answer to that yet."

def main():
    speak("Hi, I am your voice assistant. Ask me anything!")
    while True:
        query = listen()
        if query in ["exit", "quit", "bye", "stop"]:
            speak("Goodbye!")
            break
        response = respond_to_question(query)
        speak(response)

main()
