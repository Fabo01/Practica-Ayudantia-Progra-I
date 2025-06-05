import customtkinter as ctk

# Ejemplo de botón CTkButton
app = ctk.CTk()
app.geometry("300x150")

# Función que se ejecuta al presionar el botón
def accion():
    print("¡Botón presionado!")

boton = ctk.CTkButton(app, text="Presióname", command=accion)
boton.pack(pady=30)

app.mainloop()
