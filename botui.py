from tkinter import *
from core import GenerativeAI

def chat(event=None):
    input_text = te_enter.get()
    if not input_text.strip():
        return 

    try:
        response_text = GenerativeAI(input_text)
    except Exception as e:
        response_text = f"Error: {str(e)}"

    output.insert(END, f"👤 You: {input_text}\n")
    output.insert(END, f"🤖 Bot: {response_text}\n\n")
    output.see(END)
    te_enter.delete(0, END)

def main1212():
    global te_enter, output
    app = Tk()
    app.geometry("650x550")
    app.title("Gemini Student Chat Bot")
    app.config(bg="white")

    Label(app, text="Ask anything about the student database:", font="Roboto 14", bg="white").pack(pady=10)

    te_enter = Entry(app, font="Roboto 14", width=50, bg="lightyellow", justify="left")
    te_enter.pack(pady=10)
    te_enter.bind("<Return>", chat)  # ENTER key

    Button(app, text="Ask", font="Roboto 13 bold", bg="#4CAF50", fg="white", command=chat).pack(pady=5)

    output = Text(app, font="Roboto 12", width=70, height=20, bg="white", wrap=WORD)
    output.pack(pady=10)
    output.config(state=NORMAL)

    app.mainloop()

# Run it
# if _name_ == "_main_":
#     main1212()