import customtkinter as ctk

# Ejemplo de Frame CTkFrame
app = ctk.CTk()
app.geometry("400x200")

frame = ctk.CTkFrame(app, corner_radius=10)
frame.pack(padx=20, pady=20, fill="both", expand=True)

ctk.CTkLabel(frame, text="Contenido dentro del Frame").pack(pady=10)
ctk.CTkButton(frame, text="Botón en Frame").pack()

app.mainloop()
