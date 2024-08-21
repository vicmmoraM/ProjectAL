import Cifrado
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import numpy as np
key_matrix = np.array([[6, 24], [1, 11]])
# Crear ventana principal
root = tk.Tk()
root.withdraw()#Ocultar ventana
frase_original = simpledialog.askstring("Ingreso de datos", "Ingrese la frase que desea citar")

    
if frase_original:
    # Cifrar el texto
    encrypted_text = Cifrado.Cifrado_Hill(frase_original, key_matrix)
        
    # Mostrar el texto cifrado
    messagebox.showinfo("Texto Cifrado", f"Texto original: {frase_original}\nTexto cifrado: {encrypted_text}")
else:
    messagebox.showwarning("Advertencia", "No se ingresó ningún texto.")