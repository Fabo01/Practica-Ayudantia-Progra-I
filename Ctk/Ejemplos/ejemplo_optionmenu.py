import customtkinter as ctk

# Ejemplo de OptionMenu CTkOptionMenu
app = ctk.CTk()
app.geometry("350x150")

opciones = ["Opción 1", "Opción 2", "Opción 3"]
menu = ctk.CTkOptionMenu(app, values=opciones)
menu.pack(pady=20)

# Botón para mostrar la opción seleccionada
def mostrar():
    print("Seleccionado:", menu.get())

boton = ctk.CTkButton(app, text="Mostrar selección", command=mostrar)
boton.pack()

app.mainloop()
