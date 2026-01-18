import tkinter as tk
from tkinter import ttk, messagebox
from gtts import gTTS
import pygame
import uuid
import os

pygame.mixer.init()

def speak_text():
    text = text_box.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Empty Input", "Please enter some text.")
        return

    try:
        pygame.mixer.music.stop()

        filename = f"tts_{uuid.uuid4().hex}.mp3"
        tts = gTTS(text=text, lang=language_var.get())
        tts.save(filename)

        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        status_label.config(text="🔊 Speaking...")

    except Exception as e:
        messagebox.showerror("Error", str(e))


def stop_audio():
    pygame.mixer.music.stop()
    status_label.config(text="⏹ Stopped")


def cleanup():
    pygame.mixer.quit()
    root.destroy()


# ---------- UI ----------
root = tk.Tk()
root.title("Aura Voice — Text to Speech")
root.geometry("600x460")
root.resizable(False, False)

# Gradient background
canvas = tk.Canvas(root, width=600, height=460, highlightthickness=0)
canvas.pack(fill="both", expand=True)

canvas.create_rectangle(0, 0, 600, 460, fill="#0f172a", outline="")
canvas.create_oval(-300, -300, 400, 400, fill="#6366f1", outline="")
canvas.create_oval(200, 100, 800, 600, fill="#22d3ee", outline="")

container = tk.Frame(root, bg="#0f172a")
container.place(relwidth=0.9, relheight=0.88, relx=0.05, rely=0.06)

style = ttk.Style()
style.theme_use("clam")

style.configure("Title.TLabel", background="#0f172a", foreground="white",
                font=("Segoe UI", 20, "bold"))

style.configure("Modern.TButton",
                font=("Segoe UI", 11, "bold"),
                foreground="white",
                background="#6366f1",
                borderwidth=0,
                padding=10)

style.map("Modern.TButton",
          background=[("active", "#4f46e5")])

style.configure("Stop.TButton",
                font=("Segoe UI", 11, "bold"),
                foreground="white",
                background="#ef4444",
                borderwidth=0,
                padding=10)

style.map("Stop.TButton",
          background=[("active", "#dc2626")])

title = ttk.Label(container, text="🎧 Aura Voice", style="Title.TLabel")
title.pack(pady=(10, 5))

subtitle = ttk.Label(container, text="Modern Text-to-Speech Engine",
                     background="#0f172a", foreground="#94a3b8",
                     font=("Segoe UI", 10))
subtitle.pack(pady=(0, 15))

card = tk.Frame(container, bg="#020617", bd=0)
card.pack(fill="both", expand=True, padx=20, pady=10)

tk.Label(card, text="Enter your text", bg="#020617",
         fg="#e5e7eb", font=("Segoe UI", 11, "bold")).pack(anchor="w", padx=15, pady=(15, 5))

text_box = tk.Text(card, height=7, font=("Segoe UI", 12),
                   wrap="word", bg="#020617", fg="white",
                   insertbackground="white", relief="flat")
text_box.pack(fill="x", padx=15, pady=(0, 15))

control_bar = tk.Frame(card, bg="#020617")
control_bar.pack(fill="x", padx=15, pady=10)

tk.Label(control_bar, text="🌍 Language",
         bg="#020617", fg="#cbd5f5",
         font=("Segoe UI", 10, "bold")).grid(row=0, column=0, padx=5)

language_var = tk.StringVar(value="en")
language_menu = ttk.Combobox(control_bar,
                             textvariable=language_var,
                             values=["en", "si", "hi", "fr", "de", "es", "ja"],
                             width=10,
                             state="readonly")
language_menu.grid(row=0, column=1, padx=5)

speak_btn = ttk.Button(control_bar, text="▶ Speak", style="Modern.TButton", command=speak_text)
speak_btn.grid(row=0, column=2, padx=20)

stop_btn = ttk.Button(control_bar, text="⏹ Stop", style="Stop.TButton", command=stop_audio)
stop_btn.grid(row=0, column=3)

status_label = tk.Label(container, text="✨ Ready",
                        bg="#0f172a", fg="#22d3ee",
                        font=("Segoe UI", 10, "bold"))
status_label.pack(pady=10)

footer = tk.Label(container, text="Built by Eranga 🚀",
                  bg="#0f172a", fg="#64748b",
                  font=("Segoe UI", 9))
footer.pack(side="bottom", pady=8)

root.protocol("WM_DELETE_WINDOW", cleanup)
root.mainloop()
