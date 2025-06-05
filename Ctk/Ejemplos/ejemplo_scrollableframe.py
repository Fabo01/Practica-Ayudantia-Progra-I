import customtkinter as ctk

# Ejemplo de ScrollableFrame CTkScrollableFrame
app = ctk.CTk()
app.geometry("350x300")

scroll_frame = ctk.CTkScrollableFrame(app, width=300, height=200)
scroll_frame.pack(padx=20, pady=20, fill="both", expand=True)

for i in range(20):
    ctk.CTkLabel(scroll_frame, text=f"Elemento {i+1}").pack(pady=2)

app.mainloop()
