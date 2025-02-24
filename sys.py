import tkinter as tk
from tkinter import messagebox

class Module:
    def __init__(self, name, coefficient, note_distribution):
        self.name = name
        self.coefficient = coefficient
        self.note_distribution = note_distribution
        self.exam_note = 0
        self.test_note = 0
        self.practice_note = 0

def calculate_moyen(modules):
    total_weighted_sum = 0
    total_coefficients = 0
    module_moyens = []
    for module in modules:
        module_average = (module.exam_note * module.note_distribution['exam']) + \
                         (module.test_note * module.note_distribution['test']) + \
                         (module.practice_note * module.note_distribution['practice'])
        module_moyens.append((module.name, module_average))
        weighted_average = module_average * module.coefficient
        total_weighted_sum += weighted_average
        total_coefficients += module.coefficient
    general_moyen = total_weighted_sum / total_coefficients if total_coefficients != 0 else 0
    return module_moyens, general_moyen

def on_calculate():
    try:
        for i, module in enumerate(modules):
            module.exam_note = float(exam_note_entries[i].get())
            module.test_note = float(test_note_entries[i].get())
            if practice_note_entries[i] is not None:
                module.practice_note = float(practice_note_entries[i].get())
            else:
                module.practice_note = 0
            if not (0 <= module.exam_note <= 20 and 0 <= module.test_note <= 20 and 0 <= module.practice_note <= 20):
                raise ValueError("Notes must be between 0 and 20")
        module_moyens, general_moyen = calculate_moyen(modules)
        result_message = ""
        for name, moyen in module_moyens:
            result_message += f"{name}: {moyen:.2f}\n"
        result_message += f"\nGeneral Moyen: {general_moyen:.2f}"
        messagebox.showinfo("Result", result_message)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for all notes within the range [0, 20].")

app = tk.Tk()
app.title("Moyen Calculator")

modules = [
    Module("analyse", 4, {'exam': 0.6, 'test': 0.4, 'practice': 0}),
    Module("ana num", 2, {'exam': 0.5, 'test': 0.2, 'practice': 0.3}),
    Module("Mécanique Rationnelle 1", 3, {'exam': 0.6, 'test': 0.4, 'practice': 0}),
    Module("Mécanique des Fluides", 3, {'exam': 0.5, 'test': 0.2, 'practice': 0.3}),
    Module("anglais", 1, {'exam': 0.6, 'test': 0.4, 'practice': 0}),
    Module("Electricité générale", 3, {'exam': 0.5, 'test': 0.2, 'practice': 0.3}),
    Module("Technique d'expression 1", 1, {'exam': 0.6, 'test': 0.4, 'practice': 0}),
    Module("informatique 3", 3, {'exam': 0.5, 'test': 0.2, 'practice': 0.3}),
    Module("Physique 3", 4, {'exam': 0.5, 'test': 0.2, 'practice': 0.3}),
    Module("Ingénierie 1", 3, {'exam': 0.5, 'test': 0.2, 'practice': 0.3}),
    Module("Chimie 3", 3, {'exam': 0.5, 'test': 0.2, 'practice': 0.3}),
]

tk.Label(app, text="Module").grid(row=0, column=0)
tk.Label(app, text="Coefficient").grid(row=0, column=1)
tk.Label(app, text="Exam Note").grid(row=0, column=2)
tk.Label(app, text="Test Note").grid(row=0, column=3)
tk.Label(app, text="Practice Note").grid(row=0, column=4)

exam_note_entries = []
test_note_entries = []
practice_note_entries = []

for i, module in enumerate(modules):
    tk.Label(app, text=module.name).grid(row=i+1, column=0)
    tk.Label(app, text=module.coefficient).grid(row=i+1, column=1)
    
    exam_note_entry = tk.Entry(app)
    exam_note_entry.grid(row=i+1, column=2)
    exam_note_entries.append(exam_note_entry)
    
    test_note_entry = tk.Entry(app)
    test_note_entry.grid(row=i+1, column=3)
    test_note_entries.append(test_note_entry)
    
    if module.note_distribution['practice'] > 0:
        practice_note_entry = tk.Entry(app)
        practice_note_entry.grid(row=i+1, column=4)
        practice_note_entries.append(practice_note_entry)
    else:
        practice_note_entries.append(None)

calculate_button = tk.Button(app, text="Calculate Moyen", command=on_calculate)
calculate_button.grid(row=len(modules)+1, columnspan=5)

app.mainloop()
