import tkinter as tk
from tkinter import ttk, scrolledtext
import subprocess
import threading
import signal
import os

def show_overview():
    overview = tk.Tk()
    overview.title("Project Overview")
    overview.geometry("1000x600")

    name = tk.Label(overview, text="Rene Reyna", font=("Arial", 18, "bold"), anchor=tk.W)
    name.pack(padx=20, pady=10, fill='x')

    title = tk.Label(overview, text="CSCE 3335 Project 1: Problem Analysis, Problem Solving, and Programming\n– Socket Programming Using TCP/IP", font=("Arial", 22, "bold"), wraplength=900)
    title.pack(pady=15)

    description = tk.Label(overview, text="This project is a client-server program using TCP/IP sockets. The client sends a sequence of letters (‘T’, ‘A’, ‘M’) ending with ‘#’ to the server, which sorts them and returns the sorted sequence.", font=("Arial", 18), wraplength=900, justify="center")
    description.pack(padx=40, pady=20)

    instructions = tk.Label(overview, text=(
        "Instructions for Use:\n"
        "- Start the server with the Start Server button.\n"
        "- Start the client with the Start Client button.\n"
        "- Enter a sequence of ‘T’, ‘A’, ‘M’ ending with ‘#’ in the input box.\n"
        "- Send the input using the Send Input button.\n"
        "- View the sorted output in the output box.\n"
        "- Stop server/client with the Stop buttons.\n"
        "- Exit the app with the Exit button.\n\n"
        "*Note:* Click Run Tests to execute automated tests at any time."
    ), font=("Arial", 14), wraplength=900, justify="left")
    instructions.pack(padx=30, pady=20)

    start_button = tk.Button(overview, text="Start", command=lambda: start_main_gui(overview), width=25, height=3, font=("Arial", 14, "bold"))
    start_button.pack(pady=30)

    overview.mainloop()

def start_main_gui(overview):
    overview.destroy()
    root = tk.Tk()
    app = ServerClientGUI(root)
    root.mainloop()


class ServerClientGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Server-Client GUI")
        self.root.geometry("850x500")

        self.style = ttk.Style()
        self.style.theme_use("clam")

        button_frame = ttk.Frame(root, padding=10)
        button_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

        #Start Server button
        self.server_button = ttk.Button(button_frame, text="Start Server", command=self.toggle_server, width=20)
        self.server_button.grid(row=0, column=0, padx=5, pady=5)

        #Start Client button
        self.client_button = ttk.Button(button_frame, text="Start Client", command=self.toggle_client, width=20)
        self.client_button.grid(row=0, column=1, padx=5, pady=5)

        #Run Tests button
        self.test_button = ttk.Button(button_frame, text="Run Tests", command=self.run_tests, width=20)
        self.test_button.grid(row=0, column=2, padx=5, pady=5)

        #Exit button
        self.exit_button = ttk.Button(button_frame, text="Exit", command=self.exit_app, width=20)
        self.exit_button.grid(row=0, column=3, padx=5, pady=5)

        #Input field
        input_frame = ttk.Frame(root, padding=10)
        input_frame.grid(row=1, column=0, columnspan=2, sticky="ew")
        self.input_label = ttk.Label(input_frame, text="Enter Input:")
        self.input_label.pack(side="left", padx=5)
        self.input_field = ttk.Entry(input_frame, width=60)
        self.input_field.pack(side="left", padx=5)

        #Send button
        self.send_button = ttk.Button(input_frame, text="Send Input", command=self.send_input, state=tk.DISABLED, width=15)
        self.send_button.pack(side="left", padx=5)

        #Output text box
        self.output_display = scrolledtext.ScrolledText(root, width=100, height=20, font=("Courier", 14))
        self.output_display.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        root.grid_rowconfigure(2, weight=1)
        root.grid_columnconfigure(0, weight=1)

        self.server_process = None
        self.client_process = None

    def toggle_server(self):
        """Start or Stop the Server"""
        if self.server_process is None:
            self.append_output("[SERVER] Starting server...\n", "server")
            self.server_process = subprocess.Popen(
                ["python", "main.py", "server"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1
            )
            self.server_button.config(text="Stop Server")
            threading.Thread(target=self.read_output, args=(self.server_process, "server"), daemon=True).start()
        else:
            self.append_output("[SERVER] Stopping server...\n", "server")
            self.stop_process(self.server_process)
            self.server_process = None
            self.server_button.config(text="Start Server")

    def toggle_client(self):
        """Start or Stop the Client"""
        if self.client_process is None:
            self.append_output("[CLIENT] Starting client...\n", "client")
            self.client_process = subprocess.Popen(
                ["python", "main.py", "client"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1
            )
            self.client_button.config(text="Stop Client")
            threading.Thread(target=self.read_output, args=(self.client_process, "client"), daemon=True).start()
            self.send_button.config(state=tk.NORMAL)
        else:
            self.append_output("[CLIENT] Stopping client...\n", "client")
            self.stop_process(self.client_process)
            self.client_process = None
            self.client_button.config(text="Start Client")
            self.send_button.config(state=tk.DISABLED)

    def send_input(self):
        """Send user input to the server via the client"""
        user_input = self.input_field.get().strip() + "\n"
        if self.client_process and self.client_process.stdin:
            try:
                self.client_process.stdin.write(user_input)
                self.client_process.stdin.flush()
                self.append_output(f"[CLIENT] Sent to server: {user_input}", "client")
                self.input_field.delete(0, tk.END)


            except Exception as e:
                self.append_output(f"[ERROR] Failed to send input: {str(e)}\n", "error")
        threading.Thread(target=self.read_output, args=(self.client_process, "client"), daemon=True).start()

    def run_tests(self):
        """Run Test Script"""
        self.append_output("[TEST] Running tests...\n", "test")
        test_process = subprocess.Popen(
            ["python", "main.py", "tests"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1
        )
        threading.Thread(target=self.read_output, args=(test_process, "test"), daemon=True).start()

    def read_output(self, process, source):
        """Continuously read and display process output"""
        while True:
            line = process.stdout.readline()
            if not line:
                break
            self.append_output(line, source)


    def append_output(self, message, tag="default"):
        """Append text to the output box with color"""
        self.output_display.insert(tk.END, message, tag)
        self.output_display.yview(tk.END)

        #Color tags
        self.output_display.tag_config("server", foreground="green")
        self.output_display.tag_config("client", foreground="blue")
        self.output_display.tag_config("test", foreground="purple")
        self.output_display.tag_config("error", foreground="red")


    def stop_process(self, process):
        """Forcefully stop a process"""
        if process and process.poll() is None:
            os.kill(process.pid, signal.SIGTERM)
            process.wait()

    def exit_app(self):
        if self.server_process:
            self.stop_process(self.server_process)
        if self.client_process:
            self.stop_process(self.client_process)
        self.root.destroy()


if __name__ == "__main__":
    show_overview()
