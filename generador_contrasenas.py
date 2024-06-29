import random
import string
import tkinter as tk
from tkinter import messagebox

def generar_contrasena():
    longitud = int(entry_longitud.get())
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    entry_contrasena.delete(0, tk.END)
    entry_contrasena.insert(0, contrasena)

def copiar_contrasena():
    root.clipboard_clear()
    root.clipboard_append(entry_contrasena.get())
    messagebox.showinfo("Éxito", "Contraseña copiada al portapapeles")

# Interfaz gráfica
root = tk.Tk()
root.title("Generador de Contraseñas")

label_longitud = tk.Label(root, text="Longitud de la contraseña:")
label_longitud.pack(pady=5)
entry_longitud = tk.Entry(root)
entry_longitud.pack(pady=5)
entry_longitud.insert(0, "12")

button_generar = tk.Button(root, text="Generar", command=generar_contrasena)
button_generar.pack(pady=5)

label_contrasena = tk.Label(root, text="Contraseña generada:")
label_contrasena.pack(pady=5)
entry_contrasena = tk.Entry(root, width=50)
entry_contrasena.pack(pady=5)

button_copiar = tk.Button(root, text="Copiar", command=copiar_contrasena)
button_copiar.pack(pady=5)

root.mainloop()
