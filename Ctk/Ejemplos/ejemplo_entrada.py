import customtkinter as ctk

# Ejemplo de entrada de texto CTkEntry
app = ctk.CTk()
app.geometry("350x150")

entrada = ctk.CTkEntry(app, placeholder_text="Escribe tu nombre...")
entrada.pack(pady=20)

# Botón para mostrar el texto ingresado
def mostrar():
    print("Texto ingresado:", entrada.get())

boton = ctk.CTkButton(app, text="Mostrar", command=mostrar)
boton.pack()

app.mainloop()
