import customtkinter as ctk

# Ejemplo básico de ventana principal CTk
ctk.set_appearance_mode("light")  # Modo: system, light, dark
ctk.set_default_color_theme("green")  # Temas: blue, dark-blue, green

app = ctk.CTk()  # Crear ventana principal
app.title("Ejemplo Ventana CTk")
app.geometry("500x300")

app.mainloop()
