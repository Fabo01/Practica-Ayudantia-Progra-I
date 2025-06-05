import customtkinter as ctk

# Ejemplo de tabla usando .grid() sin bucles, colocando los elementos manualmente
app = ctk.CTk()
app.geometry("500x250")

frame = ctk.CTkFrame(app)
frame.pack(padx=20, pady=20, fill="both", expand=True)

# Encabezados
ctk.CTkLabel(frame, text="Producto", font=("Arial",12,"bold"), fg_color=("gray75","gray30"), text_color="white", corner_radius=5, width=100, height=30).grid(row=0, column=0, padx=5, pady=5)
ctk.CTkLabel(frame, text="Lunes", font=("Arial",12,"bold"), fg_color=("gray75","gray30"), text_color="white", corner_radius=5, width=100, height=30).grid(row=0, column=1, padx=5, pady=5)
ctk.CTkLabel(frame, text="Martes", font=("Arial",12,"bold"), fg_color=("gray75","gray30"), text_color="white", corner_radius=5, width=100, height=30).grid(row=0, column=2, padx=5, pady=5)
ctk.CTkLabel(frame, text="Miércoles", font=("Arial",12,"bold"), fg_color=("gray75","gray30"), text_color="white", corner_radius=5, width=100, height=30).grid(row=0, column=3, padx=5, pady=5)

# Fila 1
ctk.CTkLabel(frame, text="Manzanas", font=("Arial",12), width=100, height=30, corner_radius=5, fg_color=("white","gray20")).grid(row=1, column=0, padx=5, pady=5)
ctk.CTkLabel(frame, text="10", font=("Arial",12), width=100, height=30, corner_radius=5, fg_color=("white","gray20")).grid(row=1, column=1, padx=5, pady=5)
ctk.CTkLabel(frame, text="12", font=("Arial",12), width=100, height=30, corner_radius=5, fg_color=("white","gray20")).grid(row=1, column=2, padx=5, pady=5)
ctk.CTkLabel(frame, text="8", font=("Arial",12), width=100, height=30, corner_radius=5, fg_color=("white","gray20")).grid(row=1, column=3, padx=5, pady=5)

# Fila 2
ctk.CTkLabel(frame, text="Peras", font=("Arial",12), width=100, height=30, corner_radius=5, fg_color=("gray90","gray10")).grid(row=2, column=0, padx=5, pady=5)
ctk.CTkLabel(frame, text="7", font=("Arial",12), width=100, height=30, corner_radius=5, fg_color=("gray90","gray10")).grid(row=2, column=1, padx=5, pady=5)
ctk.CTkLabel(frame, text="9", font=("Arial",12), width=100, height=30, corner_radius=5, fg_color=("gray90","gray10")).grid(row=2, column=2, padx=5, pady=5)
ctk.CTkLabel(frame, text="11", font=("Arial",12), width=100, height=30, corner_radius=5, fg_color=("gray90","gray10")).grid(row=2, column=3, padx=5, pady=5)

# Fila 3
ctk.CTkLabel(frame, text="Plátanos", font=("Arial",12), width=100, height=30, corner_radius=5, fg_color=("white","gray20")).grid(row=3, column=0, padx=5, pady=5)
ctk.CTkLabel(frame, text="5", font=("Arial",12), width=100, height=30, corner_radius=5, fg_color=("white","gray20")).grid(row=3, column=1, padx=5, pady=5)
ctk.CTkLabel(frame, text="6", font=("Arial",12), width=100, height=30, corner_radius=5, fg_color=("white","gray20")).grid(row=3, column=2, padx=5, pady=5)
ctk.CTkLabel(frame, text="7", font=("Arial",12), width=100, height=30, corner_radius=5, fg_color=("white","gray20")).grid(row=3, column=3, padx=5, pady=5)

app.mainloop()
