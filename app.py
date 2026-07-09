import customtkinter as ctk
import pyttsx3
import ollama

# Voix
moteur = pyttsx3.init()

# Fenêtre
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("💙 Dalloway")
app.geometry("700x500")

titre = ctk.CTkLabel(
    app,
    text="💙 Dalloway",
    font=("Helvetica", 30, "bold")
)
titre.pack(pady=20)

message = ctk.CTkLabel(
    app,
    text="Bonjour Kevin ! Heureuse de te revoir.",
    font=("Helvetica", 20),
    wraplength=620,
    justify="left"
)
message.pack(pady=20)

entree = ctk.CTkEntry(app, width=450)
entree.pack(pady=10)


def parler():
    texte = entree.get().strip()

    if not texte:
        return

    try:
        resultat = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Tu t'appelles Dalloway. "
                        "Tu es l'assistante personnelle de Kevin. "
                        "Tu réponds toujours en français. "
                        "Tu es chaleureuse, intelligente et utile. "
                        "Ne parle jamais du roman Mrs Dalloway sauf si Kevin te le demande."
                    )
                },
                {
                    "role": "user",
                    "content": texte
                }
            ]
        )

        reponse = resultat["message"]["content"]

        message.configure(text="💙 " + reponse)

        moteur.say(reponse)
        moteur.runAndWait()

        entree.delete(0, "end")

    except Exception as e:
        message.configure(text="❌ " + str(e))


bouton = ctk.CTkButton(
    app,
    text="🎤 Parler",
    command=parler
)
bouton.pack(pady=20)

quitter = ctk.CTkButton(
    app,
    text="Quitter",
    command=app.destroy
)
quitter.pack()

app.mainloop()