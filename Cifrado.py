import numpy as np
import tkinter as tk
from tkinter import simpledialog

def texto_a_num(text, base = 26):
    return np.array([ord(c) - ord('A') for c in text.upper() if c.isalpha()])

def num_a_texto(numbers, base=26):
    """Convierte números (0, 1, ..., 25) en texto (A, B, ..., Z) nya"""
    return ''.join(chr(num + ord('A')) for num in numbers)

def Cifrado_Hill(text,matriz):
    key_size = matriz.shape[0]

    text = text.upper().replace(' ', '')
    if len(text) % key_size != 0:
        text += 'X' * (key_size - len(text) % key_size)
    
    # Convierte texto a números
    text_nums = texto_a_num(text).reshape(-1, key_size)

    # Cifra usando la matriz clave
    encrypted_nums = np.dot(text_nums, matriz) % 26

    # Convierte los números cifrados de vuelta a texto
    encrypted_text = num_a_texto(encrypted_nums.flatten())

    return encrypted_text