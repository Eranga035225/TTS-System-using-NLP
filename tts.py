import tkinter as tk
from tkinter import scrolledtext
from gtts import gTTS
from playsound import playsound



def speak_text():
    text = text_input.get("1.0", tk.END).strip()
    if text:
        tts = gTTS(text=text, lang="en")
        tts.save("output.mp3")
        playsound("output.mp3")



root = tk.Tk()
root.tile("Simple TTS App")

text_input = scrolledtext.ScrolledText(root, width=50, height=8)
text_input.pack(pady=10)

speak_button = tk.Button(root, text="Speak", command=speak_text, width=20)
speak_button.pack(pady=5)


root.mainloop()