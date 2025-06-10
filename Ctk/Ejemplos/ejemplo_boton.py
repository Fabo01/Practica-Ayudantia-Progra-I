import customtkinter as ctk

# Ejemplo de botón CTkButton
app = ctk.CTk()
app.geometry("300x150")
# Temas: blue, dark-blue, green


# Función que se ejecuta al presionar el botón
def hola():
    print("¡Botón presionado!")
    print("¡Hola, mundo!")
    

boton = ctk.CTkButton(app, text="Cargar csv", command=hola, fg_color="green", hover_color="darkgreen")
boton.pack(pady=30)

app.mainloop()
