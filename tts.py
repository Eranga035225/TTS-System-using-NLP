import tkinter as tk
from tkinter import scrolledtextfrom 
from gtts import gTTS
from playsound import playsound



def speak_text():
    text = text_input.get("1.0", tk.END).strip()
    if text:
        tts = gTTS(text=text, lang="en")
        tts.save("output.mp3")
        playsound("output.mp3")





