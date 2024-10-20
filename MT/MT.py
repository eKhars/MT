import tkinter as tk
from tkinter import messagebox, font

class TuringMachine:
    def __init__(self):
        self.state = 'q0'
        self.head = 0
        self.tape = []

    def run(self, input_string):
        self.tape = list(input_string) + ['_']  
        self.head = 0
        self.state = 'q0'

        while self.state != 'qf':
            if self.state == 'q0':
                if self.read() == 'a':
                    self.write('a')
                    self.move_right()
                    self.state = 'q1'
                else:
                    return False
            elif self.state == 'q1':
                if self.read() == 'b':
                    self.write('b')
                    self.move_right()
                    self.state = 'q2'
                else:
                    return False
            elif self.state == 'q2':
                if self.read() == 'b':
                    self.write('b')
                    self.move_right()
                    self.state = 'q3'
                else:
                    return False
            elif self.state == 'q3':
                if self.read() == 'a':
                    self.write('a')
                    self.move_right()
                    self.state = 'q4'
                elif self.read() == '_':
                    self.move_left()
                    self.state = 'qf'
                else:
                    return False
            elif self.state == 'q4':
                if self.read() == 'b':
                    self.write('b')
                    self.move_right()
                    self.state = 'q2'
                else:
                    return False
            else:
                return False

        return True

    def read(self):
        return self.tape[self.head]

    def write(self, symbol):
        self.tape[self.head] = symbol

    def move_right(self):
        self.head += 1
        if self.head == len(self.tape):
            self.tape.append('_')

    def move_left(self):
        if self.head > 0:
            self.head -= 1

class TuringMachineGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Máquina de Turing (ab^2)^n")
        self.master.geometry("500x300") 
        self.master.configure(bg='#f0f0f0') 
        
        self.tm = TuringMachine()

        title_font = font.Font(family="Helvetica", size=16, weight="bold")
        normal_font = font.Font(family="Helvetica", size=12)

        self.title_label = tk.Label(master, text="Máquina de Turing para (ab^2)^n", font=title_font, bg='#f0f0f0')
        self.title_label.pack(pady=20)

        input_frame = tk.Frame(master, bg='#f0f0f0')
        input_frame.pack(pady=10)

        self.input_label = tk.Label(input_frame, text="Ingrese la cadena:", font=normal_font, bg='#f0f0f0')
        self.input_label.pack(side=tk.LEFT, padx=5)

        self.input_entry = tk.Entry(input_frame, font=normal_font, width=20)
        self.input_entry.pack(side=tk.LEFT, padx=5)

        self.run_button = tk.Button(input_frame, text="Ejecutar", command=self.run_tm, font=normal_font, bg='#4CAF50', fg='white')
        self.run_button.pack(side=tk.LEFT, padx=5)

        self.result_label = tk.Label(master, text="", font=normal_font, bg='#f0f0f0')
        self.result_label.pack(pady=20)

    def run_tm(self):
        input_string = self.input_entry.get()
        if self.tm.run(input_string):
            self.result_label.config(text="Cadena aceptada", fg="green")
        else:
            self.result_label.config(text="Cadena rechazada", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    gui = TuringMachineGUI(root)
    root.mainloop()