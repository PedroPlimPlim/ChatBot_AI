import tkinter as tk
import google.generativeai as genai
import pathlib
import textwrap
from IPython.display import display
from IPython.display import Markdown

GOOGLE_API_KEY="Insert your API key here"
genai.configure(api_key=GOOGLE_API_KEY)

generation_config = {
  "candidate_count": 1,
  "temperature": 0.5,
}  

model = genai.GenerativeModel(model_name='gemini-1.0-pro',
                                  generation_config=generation_config,
                                  safety_settings=safety_settings,)


chat = model.start_chat(history=[])

def send_prompt(event=None):
  prompt = entry.get()
  entry.delete(0, tk.END)
  
  if not prompt.strip():
    text_area.insert(tk.END, "Please enter a message.\n")
    return

  text_area.insert(tk.END, f"You: {prompt}\n")
  
  response = chat.send_message(prompt)
  text_area.tag_config("chatbot", background="lightblue")
  text_area.insert(tk.END, f"Marigó: {response.text}\n", "chatbot")


window = tk.Tk()
window.geometry("900x600")
window.configure(bg="Blue")
window.title("Marigó")

frame = tk.Frame(window)
frame.pack(side="bottom", padx=10, pady=10)

entry = tk.Entry(frame)
entry.configure(bg="White")
entry.configure(fg="Black")
entry.configure(font="TkFixedFont")
entry.configure(justify="center")
entry.configure(width=50)
entry.pack(side="left", padx=10, pady=10)

send_button = tk.Button(frame, text="Send", command=send_prompt)
send_button.pack(side="left", padx=10, pady=10)

text_area = tk.Text(window)
text_area.pack(expand=True, fill="both")

entry.bind("<Return>", send_prompt)

window.mainloop()