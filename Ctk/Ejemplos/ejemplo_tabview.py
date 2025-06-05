import customtkinter as ctk

# Ejemplo de Tabview CTkTabview
app = ctk.CTk()
app.geometry("400x250")

tabview = ctk.CTkTabview(app)
tabview.pack(fill="both", expand=True, padx=10, pady=10)

tabview.add("Tab 1")
tabview.add("Tab 2")

ctk.CTkLabel(tabview.tab("Tab 1"), text="Contenido de la pestaña 1").pack(pady=10)
ctk.CTkLabel(tabview.tab("Tab 2"), text="Contenido de la pestaña 2").pack(pady=10)

app.mainloop()
