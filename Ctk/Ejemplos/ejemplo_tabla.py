import customtkinter as ctk

# Ejemplo de tabla simple usando CTkFrame y CTkLabel
app = ctk.CTk()
app.geometry("500x250")

frame = ctk.CTkFrame(app)
frame.pack(padx=20, pady=20, fill="both", expand=True)

# Encabezados
headers = ["Producto", "Lunes", "Martes", "Miércoles"]
for col, head in enumerate(headers):
    ctk.CTkLabel(frame, text=head, font=("Arial",12,"bold"), fg_color=("gray75","gray30"), text_color="white", corner_radius=5, width=100, height=30).grid(row=0, column=col, padx=5, pady=5)

# Datos de ejemplo
filas = [
    ["Manzanas", 10, 12, 8],
    ["Peras", 7, 9, 11],
    ["Plátanos", 5, 6, 7]
]
for r_idx, fila in enumerate(filas, start=1):
    for c_idx, val in enumerate(fila):
        ctk.CTkLabel(frame, text=str(val), font=("Arial",12), width=100, height=30, corner_radius=5, fg_color=("white","gray20") if r_idx%2==0 else ("gray90","gray10")).grid(row=r_idx, column=c_idx, padx=5, pady=5)

app.mainloop()
