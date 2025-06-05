"""
Ejemplo de uso de TK.Treeview en una ventana CTk

Este ejemplo muestra cómo integrar un widget Treeview de Tkinter (TK) dentro de una ventana de CustomTkinter (CTk).
El Treeview es útil para mostrar tablas o listas de datos de manera estructurada.
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

# Crear la ventana principal CTk
ctk.set_appearance_mode("light")
ventana = ctk.CTk()
ventana.title("Ejemplo de TK.Treeview en CTk")
ventana.geometry("400x250")

# Crear un frame de Tkinter dentro de la ventana CTk
frame_tk = tk.Frame(master=ventana)
frame_tk.pack(padx=20, pady=20, fill="both", expand=True)

# Crear el Treeview
columnas = ("Producto", "Cantidad")
tree = ttk.Treeview(frame_tk, columns=columnas, show="headings")
tree.heading("Producto", text="Producto")
tree.heading("Cantidad", text="Cantidad")

# Insertar algunos datos de ejemplo
productos = [
    ("Manzanas", 10),
    ("Naranjas", 5),
    ("Peras", 8)
]
for producto, cantidad in productos:
    tree.insert("", tk.END, values=(producto, cantidad))

# Mostrar el Treeview
tree.pack(fill="both", expand=True)

ventana.mainloop()
