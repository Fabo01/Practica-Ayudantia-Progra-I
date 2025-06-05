import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Configuración inicial
def configure_theme():
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

# Variables globales
bodega1_data = []
bodega2_data = []
diff_data = []
sum_data = []
trans1_data = []
trans2_data = []
headers = ["Producto", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

# Carga de CSV
def load_csv(bodega_name, data_list, status_label, table_frame, edit_button):
    path = filedialog.askopenfilename(filetypes=[("CSV files","*.csv"),("All files","*.*")])
    if not path:
        return
    try:
        df = pd.read_csv(path)
        if list(df.columns) != headers:
            status_label.configure(text=f"Error: CSV debe tener columnas {headers}", text_color="red")
            return
        data_list.clear()
        data_list.extend(df.values.tolist())
        status_label.configure(text=f"Cargado: {path.split('/')[-1]}", text_color="green")
        edit_button.configure(state="normal")
        update_table(table_frame, data_list)
    except Exception as e:
        status_label.configure(text=f"Error al cargar: {e}", text_color="red")

# Popup para editar stock
# Función para exportar a CSV
def export_csv(bodega_name, data_list):
    if not data_list:
        messagebox.showerror("Error", f"No hay datos en {bodega_name} para exportar.")
        return
    df = pd.DataFrame(data_list, columns=headers)
    path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files","*.csv")], title=f"Guardar {bodega_name} como...")
    if path:
        df.to_csv(path, index=False,encoding='ISO-8859-1')
        messagebox.showinfo("Éxito", f"{bodega_name} exportada en: {path}")

def open_edit_popup(bodega_name, data_list, table_frame):
    if not data_list:
        messagebox.showerror("Error", f"No hay datos en {bodega_name}")
        return
    popup = ctk.CTkToplevel(root)
    popup.title(f"Editar Stock - {bodega_name}")
    popup.geometry("400x360")
    popup.transient(root)
    popup.grab_set()

    frame = ctk.CTkFrame(popup, corner_radius=8)
    frame.pack(padx=15, pady=15, fill="both", expand=True)
    frame.grid_columnconfigure(1, weight=1)

    ctk.CTkLabel(frame, text="Producto:", font=("Arial",12)).grid(row=0, column=0, sticky="e", padx=5, pady=5)
    prod_var = tk.StringVar(value=data_list[0][0])
    product_menu = ctk.CTkOptionMenu(frame, values=[r[0] for r in data_list], variable=prod_var)
    product_menu.grid(row=0, column=1, sticky="we", padx=5, pady=5)

    entries = {}
    for idx, day in enumerate(headers[1:], start=1):
        ctk.CTkLabel(frame, text=f"{day}:", font=("Arial",12)).grid(row=idx, column=0, sticky="e", padx=5, pady=3)
        ent = ctk.CTkEntry(frame, corner_radius=5, height=28)
        ent.grid(row=idx, column=1, sticky="we", padx=5, pady=3)
        entries[day] = ent

    def update_entries(*args):
        sel = prod_var.get()
        for row in data_list:
            if row[0] == sel:
                for i, day in enumerate(headers[1:], start=1):
                    entries[day].delete(0, tk.END)
                    entries[day].insert(0, str(row[i]))
                break
    prod_var.trace_add("write", update_entries)
    update_entries()

    btn_frame = ctk.CTkFrame(frame)
    btn_frame.grid(row=len(headers), column=0, columnspan=2, pady=10)
    ctk.CTkButton(btn_frame, text="Guardar", command=lambda: save_changes(data_list, prod_var, entries, table_frame, popup)).pack(side="left", padx=8)
    ctk.CTkButton(btn_frame, text="Cancelar", command=popup.destroy).pack(side="left", padx=8)

# Guardar cambios
def save_changes(data_list, prod_var, entries, table_frame, popup):
    try:
        sel = prod_var.get()
        for day, ent in entries.items():
            val = ent.get()
            if not val.replace('.', '').isdigit():
                raise ValueError(f"La cantidad para {day} debe ser numérica.")
        for row in data_list:
            if row[0] == sel:
                for i, day in enumerate(headers[1:], start=1):
                    row[i] = float(entries[day].get())
                break
        update_table(table_frame, data_list)
        messagebox.showinfo("Éxito", f"Stock actualizado para {sel}.")
        popup.destroy()
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Función de diferencia de stock
def calculate_difference(status_label, table_frame):
    if not bodega1_data or not bodega2_data:
        status_label.configure(text="Carga ambas bodegas primero", text_color="red")
        return
    df1 = pd.DataFrame(bodega1_data, columns=headers).set_index('Producto')
    df2 = pd.DataFrame(bodega2_data, columns=headers).set_index('Producto')
    diff = df1.subtract(df2, fill_value=0).reset_index()
    diff_data.clear()
    diff_data.extend(diff.values.tolist())
    status_label.configure(text="Diferencia calculada", text_color="green")
    update_table(table_frame, diff_data)

# Función de suma de stock
def calculate_sum(status_label, table_frame):
    if not bodega1_data or not bodega2_data:
        status_label.configure(text="Carga ambas bodegas primero", text_color="red")
        return
    df1 = pd.DataFrame(bodega1_data, columns=headers).set_index('Producto')
    df2 = pd.DataFrame(bodega2_data, columns=headers).set_index('Producto')
    summed = df1.add(df2, fill_value=0).reset_index()
    sum_data.clear()
    sum_data.extend(summed.values.tolist())
    status_label.configure(text="Suma calculada", text_color="green")
    update_table(table_frame, sum_data)

# Función de transpuesta
def calculate_transpose(table_frame1, table_frame2):
    if not bodega1_data or not bodega2_data:
        messagebox.showerror("Error", "Carga ambas bodegas primero")
        return
    df1 = pd.DataFrame(bodega1_data, columns=headers)
    df2 = pd.DataFrame(bodega2_data, columns=headers)
    t1 = df1.set_index('Producto').T.reset_index()
    t2 = df2.set_index('Producto').T.reset_index()
    trans1_data.clear()
    trans2_data.clear()
    trans1_data.extend(t1.values.tolist())
    trans2_data.extend(t2.values.tolist())
    trans_headers = ['Día'] + t1.columns.tolist()[1:]
    update_table_custom(table_frame1, trans_headers, trans1_data)
    update_table_custom(table_frame2, trans_headers, trans2_data)

# Función para calcular y resaltar triángulos
def calculate_triangles(label_frame, frame1, frame2):
    if not trans1_data or not trans2_data:
        messagebox.showerror("Error", "Primero calcula la transpuesta")
        return
    def tri_sums(data):
        upper = lower = 0
        n = len(data)
        m = len(data[0]) - 1
        for i in range(n):
            for j in range(m):
                val = float(data[i][j+1])
                if i < j:
                    upper += val
                elif i > j:
                    lower += val
        return upper, lower
    u1, l1 = tri_sums(trans1_data)
    u2, l2 = tri_sums(trans2_data)
    for widget in tri_frame.winfo_children():
        widget.destroy()
    ctk.CTkLabel(tri_frame, text=f"B1 Superior: {u1:.2f}  Inferior: {l1:.2f}", font=("Arial",12)).pack(side="left", padx=20)
    ctk.CTkLabel(tri_frame, text=f"B2 Superior: {u2:.2f}  Inferior: {l2:.2f}", font=("Arial",12)).pack(side="left", padx=20)
    def highlight(frame, data, condition, colors):
        for w in frame.winfo_children():
            info = w.grid_info()
            r = info.get('row', 0)
            c = info.get('column', 0)
            if r > 0 and c > 0 and condition(r-1, c-1):
                w.configure(fg_color=colors)
    green = ("#B0E57C","#8CBF4A")
    orange = ("#F5A623","#D9822B")
    highlight(frame1, trans1_data, lambda i,j: i<j, green)
    highlight(frame2, trans2_data, lambda i,j: i<j, green)
    highlight(frame1, trans1_data, lambda i,j: i>j, orange)
    highlight(frame2, trans2_data, lambda i,j: i>j, orange)

# Función para actualizar tabla con grid
def update_table(table_frame, data):
    for w in table_frame.winfo_children(): w.destroy()
    for col, head in enumerate(headers):
        ctk.CTkLabel(table_frame, text=head, font=("Arial",12,"bold"), fg_color=("gray75","gray30"), text_color="white", corner_radius=5, width=120, height=30).grid(row=0, column=col, padx=5, pady=5, sticky="nsew")
    for r_idx, row in enumerate(data, start=1):
        for c_idx, val in enumerate(row):
            ctk.CTkLabel(table_frame, text=str(val), font=("Arial",12), width=120, height=30, corner_radius=5, fg_color=("white","gray20") if r_idx%2==0 else ("gray90","gray10")).grid(row=r_idx, column=c_idx, padx=5, pady=5, sticky="nsew")
    for i in range(len(headers)): table_frame.grid_columnconfigure(i, weight=1)

# Función para actualizar tabla personalizada
def update_table_custom(table_frame, custom_headers, data):
    for w in table_frame.winfo_children(): w.destroy()
    for col, head in enumerate(custom_headers):
        ctk.CTkLabel(table_frame, text=head, font=("Arial",12,"bold"), fg_color=("gray75","gray30"), text_color="white", corner_radius=5, width=120, height=30).grid(row=0, column=col, padx=5, pady=5, sticky="nsew")
    for r_idx, row in enumerate(data, start=1):
        for c_idx, val in enumerate(row):
            ctk.CTkLabel(table_frame, text=str(val), font=("Arial",12), width=120, height=30, corner_radius=5, fg_color=("white","gray20") if r_idx%2==0 else ("gray90","gray10")).grid(row=r_idx, column=c_idx, padx=5, pady=5, sticky="nsew")
    for i in range(len(custom_headers)): table_frame.grid_columnconfigure(i, weight=1)
# Función para calcular la suma de la diagonal principal y resaltar
# Función para resaltar celdas
def highlight(frame, data, condition, colors):
    for w in frame.winfo_children():
        info = w.grid_info()
        r = info.get('row', 0)
        c = info.get('column', 0)
        if r > 0 and c > 0 and condition(r-1, c-1):
            w.configure(fg_color=colors)
def calculate_diagonals(label_frame, frame1, frame2):
    if not trans1_data or not trans2_data:
        messagebox.showerror("Error", "Primero calcula la transpuesta")
        return
    def diag_sum(data):
        total = 0
        n = len(data)
        for i in range(n):
            if i < len(data[0]) - 1:
                val = float(data[i][i + 1])
                total += val
        return total
    diag1 = diag_sum(trans1_data)
    diag2 = diag_sum(trans2_data)
    # Limpiar el frame de resultados
    for widget in label_frame.winfo_children():
        widget.destroy()
    # Mostrar resultados de diagonales
    ctk.CTkLabel(label_frame, text=f"B1 Diagonal: {diag1:.2f}", font=("Arial", 12)).pack(side="left", padx=20)
    ctk.CTkLabel(label_frame, text=f"B2 Diagonal: {diag2:.2f}", font=("Arial", 12)).pack(side="left", padx=20)
    # Resetear colores previos en ambas tablas
    def reset_highlights(frame):
        for w in frame.winfo_children():
            info = w.grid_info()
            r = info.get('row', 0)
            c = info.get('column', 0)
            if r > 0 and c > 0:
                w.configure(fg_color=("white", "gray20") if r % 2 == 0 else ("gray90", "gray10"))
    reset_highlights(frame1)
    reset_highlights(frame2)
    # Resaltar diagonales con colores diferentes
    blue = ("#4B8BBE", "#306998")  # Azul para Bodega 1
    purple = ("#A100A1", "#800080")  # Púrpura para Bodega 2
    highlight(frame1, trans1_data, lambda i, j: i == j, blue)
    highlight(frame2, trans2_data, lambda i, j: i == j, purple)
# Función principal para crear GUI
def main():
    global root, frame1, frame2, tri_frame, diff_table_frame, sum_table_frame, trans1_frame, trans2_frame
    root = ctk.CTk()
    root.title("Gestión de Inventario de Bodegas")
    root.geometry("1000x900")
    configure_theme()

    container = ctk.CTkFrame(master=root, corner_radius=10)
    container.pack(padx=20, pady=20, fill="both", expand=True)

    ctk.CTkLabel(master=container, text="Gestión de Inventario de Bodegas", font=("Arial",20)).pack(pady=10)
    tabview = ctk.CTkTabview(master=container)
    tabview.pack(fill="both", expand=True)

    # Pestaña Bodega 1
    tabview.add("Bodega 1")
    page1 = tabview.tab("Bodega 1")
    f1 = ctk.CTkScrollableFrame(master=page1)
    f1.pack(fill="both", expand=True, padx=10, pady=10)
    b1_load = ctk.CTkButton(master=f1, text="Cargar Bodega 1", command=lambda: load_csv("Bodega 1", bodega1_data, b1_status, f1_table, b1_edit))
    b1_load.pack(pady=5)
    b1_edit = ctk.CTkButton(master=f1, text="Editar Stock", state="disabled", command=lambda: open_edit_popup("Bodega 1", bodega1_data, f1_table))
    b1_edit.pack(pady=5)
        # Botón para exportar CSV
    b1_export = ctk.CTkButton(master=f1, text="Exportar CSV", fg_color="green", text_color="white", command=lambda: export_csv("Bodega 1", bodega1_data))
    b1_export.pack(pady=5, anchor="e", padx=10)
    b1_status = ctk.CTkLabel(master=f1, text="Ninguno", font=("Arial",12), text_color="gray")
    b1_status.pack(pady=5)
    f1_table = ctk.CTkFrame(master=f1)
    f1_table.pack(fill="both", expand=True, pady=5)

    # Pestaña Bodega 2
    tabview.add("Bodega 2")
    page2 = tabview.tab("Bodega 2")
    f2 = ctk.CTkScrollableFrame(master=page2)
    f2.pack(fill="both", expand=True, padx=10, pady=10)
    b2_load = ctk.CTkButton(master=f2, text="Cargar Bodega 2", command=lambda: load_csv("Bodega 2", bodega2_data, b2_status, f2_table, b2_edit))
    b2_load.pack(pady=5)
    b2_edit = ctk.CTkButton(master=f2, text="Editar Stock", state="disabled", command=lambda: open_edit_popup("Bodega 2", bodega2_data, f2_table))
    b2_edit.pack(pady=5)
    # Botón para exportar CSV en Bodega 2
    b2_export = ctk.CTkButton(master=f2, text="Exportar CSV", fg_color="green", text_color="white", command=lambda: export_csv("Bodega 2", bodega2_data))
    b2_export.pack(pady=5, anchor="e", padx=10)
    b2_status = ctk.CTkLabel(master=f2, text="Ninguno", font=("Arial",12), text_color="gray")
    b2_status.pack(pady=5)
    f2_table = ctk.CTkFrame(master=f2)
    f2_table.pack(fill="both", expand=True, pady=5)

    # Pestaña Diferencia
    tabview.add("Diferencia")
    page_diff = tabview.tab("Diferencia")
    fd = ctk.CTkFrame(master=page_diff)
    fd.pack(fill="both", expand=True, padx=10, pady=10)
    diff_btn = ctk.CTkButton(master=fd, text="Calcular Diferencia", command=lambda: calculate_difference(diff_status, diff_table_frame))
    diff_btn.pack(pady=5)
    diff_status = ctk.CTkLabel(master=fd, text="", font=("Arial",12), text_color="gray")
    diff_status.pack(pady=5)
        # Botón para exportar CSV en Diferencia
    b_diff_export = ctk.CTkButton(master=fd, text="Exportar CSV", fg_color="green", text_color="white", command=lambda: export_csv("Diferencia", diff_data))
    b_diff_export.pack(pady=5, anchor="e", padx=10)
    diff_table_frame = ctk.CTkFrame(master=fd)
    diff_table_frame.pack(fill="both", expand=True, pady=5)

    # Pestaña Suma
    tabview.add("Suma")
    page_sum = tabview.tab("Suma")
    fs = ctk.CTkFrame(master=page_sum)
    fs.pack(fill="both", expand=True, padx=10, pady=10)
    sum_btn = ctk.CTkButton(master=fs, text="Calcular Suma", command=lambda: calculate_sum(sum_status, sum_table_frame))
    sum_btn.pack(pady=5)
    sum_status = ctk.CTkLabel(master=fs, text="", font=("Arial",12), text_color="gray")
    sum_status.pack(pady=5)
        # Botón para exportar CSV en Suma
    b_sum_export = ctk.CTkButton(master=fs, text="Exportar CSV", fg_color="green", text_color="white", command=lambda: export_csv("Suma", sum_data))
    b_sum_export.pack(pady=5, anchor="e", padx=10)
    sum_table_frame = ctk.CTkFrame(master=fs)
    sum_table_frame.pack(fill="both", expand=True, pady=5)

    # Pestaña MatrizT
    tabview.add("MatrizT")
    page_mt = tabview.tab("MatrizT")
    mt = ctk.CTkFrame(master=page_mt)
    mt.pack(fill="both", expand=True, padx=10, pady=10)

    # Frame para botones de exportación, separado de las tablas
    mt_buttons = ctk.CTkFrame(master=mt, corner_radius=5)
    mt_buttons.pack(fill="x", padx=5, pady=(0,5))
    b_t1_export = ctk.CTkButton(master=mt_buttons, text="Exportar T1 CSV", fg_color="green", text_color="white", command=lambda: export_csv("Transpuesta Bodega 1", trans1_data))
    b_t1_export.pack(side="left", padx=10, pady=5)
    b_t2_export = ctk.CTkButton(master=mt_buttons, text="Exportar T2 CSV", fg_color="green", text_color="white", command=lambda: export_csv("Transpuesta Bodega 2", trans2_data))
    b_t2_export.pack(side="right", padx=10, pady=5)

    # Frames para cada transpuesta
    trans1_frame = ctk.CTkFrame(master=mt, corner_radius=5)
    trans1_frame.place(relx=0.05, rely=0.15, relwidth=0.425, relheight=0.65)
    trans2_frame = ctk.CTkFrame(master=mt, corner_radius=5)
    trans2_frame.place(relx=0.525, rely=0.15, relwidth=0.425, relheight=0.65)

    # Etiquetas de título
    ctk.CTkLabel(master=mt, text="Transpuesta Bodega 1", font=("Arial",14)).place(relx=0.1, rely=0.08)
    ctk.CTkLabel(master=mt, text="Transpuesta Bodega 2", font=("Arial",14)).place(relx=0.6, rely=0.08)

    # Botón Calcular Transpuesta
    calc_t_btn = ctk.CTkButton(master=mt, text="Calcular Transpuesta", command=lambda: calculate_transpose(trans1_frame, trans2_frame))
    calc_t_btn.place(relx=0.4, rely=0.08)

    # Frame para los botones Calcular Triángulos y Calcular Diagonales
    tri_button_frame = ctk.CTkFrame(master=mt, corner_radius=5)
    tri_button_frame.place(relx=0.05, rely=0.82, relwidth=0.9, relheight=0.06)
    ctk.CTkButton(master=tri_button_frame, text="Calcular Triángulos", command=lambda: calculate_triangles(tri_frame, trans1_frame, trans2_frame)).pack(side="left", padx=10, pady=5)
    ctk.CTkButton(master=tri_button_frame, text="Calcular Diagonales", command=lambda: calculate_diagonals(tri_frame, trans1_frame, trans2_frame)).pack(side="left", padx=10, pady=5)

    # Frame para los resultados de triángulos y diagonales
    tri_frame = ctk.CTkFrame(master=mt, corner_radius=5)
    tri_frame.place(relx=0.05, rely=0.88, relwidth=0.9, relheight=0.06)

    root.mainloop()
if __name__ == "__main__":
    configure_theme()
    main()
