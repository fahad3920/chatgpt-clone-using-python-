import tkinter as tk
from tkinter import scrolledtext
import openai

# === OpenRouter API Client Setup ===
openai.api_key = "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"  # Replace with your OpenRouter API key
base_url = "https://openrouter.ai/api/v1"

# === Function to Get AI Response ===
def get_ai_response(message):
    try:
        system_prompt = "You are a helpful assistant. Please respond in English."
        response = openai.ChatCompletion.create(
            model="deepseek/deepseek-r1-0528:free",
            messages=[
                {"role": "system", "content": system_prompt},
                {
                    "role": "user",
                    "content": message
                }
            ],
            api_base=base_url
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

# === ChatBot GUI ===
class ChatBotApp:
    def __init__(self, master):
        self.master = master
        master.title("Simple AI ChatBot")
        master.geometry("600x600")
        master.configure(bg="#2c3e50")

        # === Chat Display ===
        self.chat_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, font=("Segoe UI", 12), bg="#1c1c1c", fg="#ffffff")
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.chat_area.config(state='disabled')

        # === Input Field ===
        self.entry_frame = tk.Frame(master, bg="#2c3e50")
        self.entry_frame.pack(fill=tk.X, padx=10, pady=10)

        self.input_field = tk.Entry(self.entry_frame, font=("Segoe UI", 12), bg="#34495e", fg="#ffffff")
        self.input_field.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10), ipady=6)
        self.input_field.bind("<Return>", self.send_message)

        self.send_button = tk.Button(self.entry_frame, text="Send", font=("Segoe UI", 11), bg="#27ae60", fg="white", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT)

    def send_message(self, event=None):
        user_message = self.input_field.get().strip()
        if not user_message:
            return

        self.display_message("You", user_message)
        self.input_field.delete(0, tk.END)
        self.master.after(100, lambda: self.bot_response(user_message))

    def bot_response(self, message):
        response = get_ai_response(message)
        self.display_message("AI", response)

    def display_message(self, sender, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_area.config(state='disabled')
        self.chat_area.yview(tk.END)

# === Run App ===
if __name__ == "__main__":
    root = tk.Tk()
    app = ChatBotApp(root)
    root.mainloop()
