import tkinter as tk
from tkinter import messagebox
from Chat_gpt import chat_gpt  # Import the chatbot function

class Gui():
    
    def __init__(self):
        self.window = tk.Tk()

        self.window.geometry("800x500")
        self.window.title("PyChat-GPT")

        self.label = tk.Label(self.window, text="PyChat-GPT", font=('Arial', 24))
        self.label.pack(padx=20, pady=20)

        self.textbox = tk.Text(self.window, height=5)
        self.textbox.pack(padx=10, pady=20)
        
        self.check_state = tk.IntVar()
        
        self.check = tk.Checkbutton(self.window, text="Show me message", variable=self.check_state)
        self.check.pack(padx=10, pady=20)

        self.button = tk.Button(self.window, text="Enter", font=('Arial', 18), command=self.show_message)
        self.button.pack(padx=10, pady=20)
        
        self.window.protocol("WM_DELETE_WINDOW", self.closing)
        self.window.mainloop()
    
    def show_message(self):
        user_input = self.textbox.get('1.0', tk.END).strip()  # Get user input from the textbox
        if not user_input:
            return

        response = chat_gpt(user_input)  # Get response from the chatbot

        if self.check_state.get() == 0:
            print(response)
        else:
            messagebox.showinfo(title="Response", message=response)

    def closing(self):
        if messagebox.askyesnocancel(title="Closing?", message="Do you want to close the window?"):
            self.window.destroy()

if __name__ == "__main__":
    Gui()
