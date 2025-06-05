# Explicaciones Detalladas – Sección Pandas

Este documento desglosa en detalle cada uno de los ejercicios propuestos en la sección Pandas. Lee cada explicación antes de revisar el código de ejemplo.  

---

## Ejercicios Nivel Fácil

### Pandas-Fácil-1  
1. **Objetivo:** Aprender a leer un CSV con Pandas y examinar dimensiones del DataFrame.  
2. **Pasos:**
   - Importar `pandas` con `import pandas as pd`.
   - Usar `pd.read_csv("bodega1.csv")` para cargar el CSV en un DataFrame llamado, por ejemplo, `df`.
   - Llamar `df.head()` para mostrar las primeras 5 filas.
   - Llamar `df.shape` para obtener una tupla `(n_filas, n_columnas)`.
3. **Por qué funciona:**  
   - `read_csv` detecta automáticamente el separador (coma) y los nombres de columnas en la primera fila del CSV.  
   - `head()` es útil para verificar que la lectura sea correcta.  
   - `shape` sirve para validar si se cargaron todos los registros.  

---

### Pandas-Fácil-2  
1. **Objetivo:** Practicar filtrado de filas según condiciones en Pandas.  
2. **Pasos:**
   - Partir del DataFrame `df` del ejercicio anterior.
   - Escribir `df[df["Lunes"] > 50]` para filtrar.  
   - Guardar el resultado en `df_lunes_mayor50` y usar `print(df_lunes_mayor50)`.
3. **Por qué funciona:**  
   - En Pandas, `df[condición]` devuelve un DataFrame con las filas que cumplen `condición`.  
   - La comparación `df["Lunes"] > 50` produce una Serie de valores booleanos.  

---

### Pandas-Fácil-3  
1. **Objetivo:** Aprender a sumar columnas de un DataFrame para crear una nueva columna.  
2. **Pasos:**
   - Dado `df` con columnas `["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]`.
   - Crear la nueva columna con:  
     ```python
     df["TotalSemanal"] = df["Lunes"] + df["Martes"] + df["Miércoles"] + df["Jueves"] + df["Viernes"]
     ```
   - Mostrar `df.head()` para verificar.  
3. **Pistas:**
   - Pandas se encarga de hacer la suma fila a fila.  
   - Si alguna celda estuviera vacía o no numérica, habría que convertir o imputar valores, pero suponemos datos limpios.

---

### Pandas-Fácil-4  
1. **Objetivo:** Ordenar un DataFrame por una columna y guardar en CSV.  
2. **Pasos:**
   - Usar `df.sort_values(by="TotalSemanal", ascending=False)` para ordenar de mayor a menor.
   - Guardar el resultado en `df_ordenado`.
   - Luego llamar `df_ordenado.to_csv("bodega1_ordenado.csv", index=False)` para exportar sin índice.
3. **Por qué funciona:**  
   - `sort_values` reordena las filas según la columna indicada.  
   - `to_csv(..., index=False)` guarda el CSV sin la columna de índice, tal como se pide.

---

## Ejercicios Nivel Medio

### Pandas-Medio-1  
1. **Objetivo:** Aprender a combinar (merge) dos DataFrames según una clave.  
2. **Pasos:**
   - Cargar `df1 = pd.read_csv("bodega1.csv")` y `df2 = pd.read_csv("bodega2.csv")`.
   - Para no confundir columnas, primero renombra cada conjunto:  
     ```python
     df1 = df1.rename(columns={"Lunes": "Lunes_B1", "Martes": "Martes_B1", "Miércoles": "Miércoles_B1", "Jueves": "Jueves_B1", "Viernes": "Viernes_B1"})
     df2 = df2.rename(columns={"Lunes": "Lunes_B2", "Martes": "Martes_B2", "Miércoles": "Miércoles_B2", "Jueves": "Jueves_B2", "Viernes": "Viernes_B2"})
     ```
   - Unir usando:  
     ```python
     df_combinado = pd.merge(df1, df2, on="Producto", how="outer")
     ```
     (el parámetro `how="outer"` garantiza que aparezcan todos los productos, incluso si sólo están en una bodega).
   - Mostrar `df_combinado.head()`.
3. **Por qué funciona:**  
   - `rename` es útil para agregar sufijos que distingan columnas idénticas antes de la unión.  
   - `pd.merge` toma dos DataFrames y los combina donde la columna `"Producto"` coincida.  

---

### Pandas-Medio-2  
1. **Objetivo:** Aplicar operaciones aritméticas entre columnas de un mismo DataFrame.  
2. **Pasos:**
   - A partir de `df_combinado`, crea por ejemplo:  
     ```python
     df_combinado["Diferencia_Lunes"] = df_combinado["Lunes_B1"] - df_combinado["Lunes_B2"]
     df_combinado["Diferencia_Martes"] = df_combinado["Martes_B1"] - df_combinado["Martes_B2"]
     # ... y así sucesivamente para Miércoles, Jueves, Viernes
     ```
   - Para mostrar únicamente las columnas pedidas:  
     ```python
     columnas_mostrar = ["Producto", "Diferencia_Lunes", "Diferencia_Viernes"]
     print(df_combinado[columnas_mostrar])
     ```
3. **Por qué funciona:**  
   - Restar dos columnas de un DataFrame produce otra Serie, que se asigna directamente a una nueva columna.  
   - Al final, `df_combinado[columnas_mostrar]` devuelve un DataFrame sólo con esas tres columnas.

---

### Pandas-Medio-3  
1. **Objetivo:** Practicar lectura de CSV diferente y agrupar datos.  
2. **Pasos:**
   - Leer `df_ventas = pd.read_csv("ventas.csv")`.
   - Crear `df_ventas["Ingreso"] = df_ventas["CantidadVta"] * df_ventas["PrecioUnitario"]`.
   - Aplicar agrupación:  
     ```python
     df_agrupado = df_ventas.groupby("Producto").agg({
         "CantidadVta": "sum",
         "Ingreso": "sum"
     }).reset_index()
     ```
   - Mostrar `print(df_agrupado)`.
3. **Por qué funciona:**  
   - `groupby("Producto")` agrupa filas por cada producto.  
   - `agg({"CantidadVta": "sum", "Ingreso": "sum"})` calcula sumas por grupo.  
   - `reset_index()` convierte el índice agrupado en columna normal.

---

## Ejercicios Nivel Difícil

### Pandas-Difícil-1  
1. **Objetivo:** Combinar datos de ambas bodegas y filtrar según una suma condicionada.  
2. **Pasos:**
   - Partir de `df1` y `df2` ya renombrados (ver Medio-1).
   - Hacer el `merge` para obtener `df_combinado`.
   - Crear dos columnas temporales:  
     ```python
     df_combinado["Total_B1"] = (
         df_combinado["Lunes_B1"] + df_combinado["Martes_B1"] +
         df_combinado["Miércoles_B1"] + df_combinado["Jueves_B1"] +
         df_combinado["Viernes_B1"]
     )
     df_combinado["Total_B2"] = (
         df_combinado["Lunes_B2"] + df_combinado["Martes_B2"] +
         df_combinado["Miércoles_B2"] + df_combinado["Jueves_B2"] +
         df_combinado["Viernes_B2"]
     )
     ```
   - Luego crear una columna `"SumaTotal"` = `Total_B1 + Total_B2`.
   - Filtrar:  
     ```python
     df_filtrado = df_combinado[df_combinado["SumaTotal"] > 500]
     ```
   - Ordenar:  
     ```python
     df_filtrado = df_filtrado.sort_values(by="SumaTotal", ascending=False)
     ```
   - Finalmente, exportar:  
     ```python
     df_filtrado.to_csv("productos_mas_500.csv", index=False)
     ```
3. **Pistas y recomendaciones:**
   - Si alguna bodega tiene NaN (producto no existe en la otra), convertir con `.fillna(0)` antes de sumar.  
   - Siempre verificar con `print(df_filtrado.head())` antes de exportar.

---

### Pandas-Difícil-2  
1. **Objetivo:** Generar la transpuesta de un DataFrame (filas ↔ columnas).  
2. **Pasos:**
   - Leer `df = pd.read_csv("bodega1.csv")`.
   - Hacer que la columna `"Producto"` sea índice:  
     ```python
     df_index = df.set_index("Producto")
     ```
   - Calcular la transpuesta con:  
     ```python
     df_transpuesta = df_index.transpose()
     ```
     o, equivalente,  
     ```python
     df_transpuesta = df_index.T
     ```
   - Ahora el índice de `df_transpuesta` son los días `["Lunes", "Martes", ...]` y las columnas son los productos.
   - Para que el índice aparezca como columna normal, hacer:  
     ```python
     df_transpuesta = df_transpuesta.reset_index()
     df_transpuesta = df_transpuesta.rename(columns={"index": "Día"})
     ```
   - Exportar:  
     ```python
     df_transpuesta.to_csv("bodega_transpuesta.csv", index=False)
     ```
3. **Por qué funciona:**  
   - `set_index("Producto")` hace que Pandas use “Producto” como índice, de modo que `transpose()` mueva ese índice a columnas.  
   - `reset_index()` pasa el índice a columna normal para guardar un CSV legible.

---

## Ejercicios Nivel Muy Difícil

### Pandas-MuyDifícil-1  
1. **Objetivo general:**  
   - Crear una tabla de diferencias entre las dos bodegas y visualizarla como un heatmap.  
   - Entender el uso conjunto de Pandas y Matplotlib (o Seaborn) para gráfico matricial.

2. **Pasos detallados:**

   1. **Cargar bodega1 y bodega2:**
      ```python
      import pandas as pd
      df1 = pd.read_csv("bodega1.csv")
      df2 = pd.read_csv("bodega2.csv")
      ```
      - Si tienen nombres de columnas idénticos, renómbralos con `_B1` y `_B2` como en ejercicios anteriores.

   2. **Merge por “Producto”:**
      ```python
      df1 = df1.rename(columns={"Lunes": "Lunes_B1", ... , "Viernes": "Viernes_B1"})
      df2 = df2.rename(columns={"Lunes": "Lunes_B2", ... , "Viernes": "Viernes_B2"})
      df_combinado = pd.merge(df1, df2, on="Producto", how="inner")
      ```
      - Aquí se usa `how="inner"` asumiendo que sólo analizaremos productos comunes, pero podrías usar `outer` y rellenar NaN con 0.

   3. **Calcular tabla de diferencias (B1 - B2):**
      ```python
      df_diferencias = pd.DataFrame()
      df_diferencias["Producto"] = df_combinado["Producto"]
      for dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]:
          df_diferencias[dia] = (
              df_combinado[f"{dia}_B1"].fillna(0) - df_combinado[f"{dia}_B2"].fillna(0)
          )
      ```
      - Así obtendrás un DataFrame con columnas `["Producto", "Lunes", "Martes", ..., "Viernes"]` para las diferencias.

   4. **Exportar tabla de diferencias:**
      ```python
      df_diferencias.to_csv("diferencia_bodegas.csv", index=False)
      ```

   5. **Preparar matriz para el heatmap:**
      - Primero, convertir `df_diferencias` a una tabla donde cada fila sea un día y cada columna un producto.  
        ```python
        df_index = df_diferencias.set_index("Producto")
        df_transpuesta = df_index.T  # filas = días, columnas = productos
        ```
      - Obtener la matriz NumPy:
        ```python
        matriz = df_transpuesta.values  # forma: (5 días) × (n productos)
        etiquetas_x = list(df_index.index)  # nombres de productos
        etiquetas_y = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
        ```

   6. **Generar el heatmap con Matplotlib (sin Seaborn, para practicar “desde cero”):**
      ```python
      import matplotlib.pyplot as plt

      plt.figure(figsize=(10, 6))
      im = plt.imshow(matriz, aspect="auto", cmap="coolwarm")  # 'coolwarm' es un mapa de colores
      plt.colorbar(im, label="Diferencia (B1 - B2)")
      plt.xticks(ticks=range(len(etiquetas_x)), labels=etiquetas_x, rotation=90)
      plt.yticks(ticks=range(len(etiquetas_y)), labels=etiquetas_y)
      plt.title("Mapa de calor: Diferencia de stock Bodega1 - Bodega2")
      plt.xlabel("Producto")
      plt.ylabel("Día de la semana")
      plt.tight_layout()
      plt.savefig("heatmap_diferencia.png", dpi=300)
      plt.show()
      ```
      - `imshow` dibuja la matriz de valores; `cmap="coolwarm"` es un gradiente rojo-azul.
      - `plt.colorbar` añade una barra de color con label explicativo.
      - `xticks` y `yticks` para etiquetar ejes con rotación en el eje x.

3. **Puntos clave:**
   - Asegúrate de rellenar NaN con 0 antes de restar, para evitar errores.  
   - El DataFrame final `df_diferencias` debe tener exactamente las mismas columnas que el CSV original salvo que “Producto” va primero.  
   - Verifica que `matriz.shape` sea `(5, número_de_productos)` antes de graficar.  
   - El archivo `heatmap_diferencia.png` debe guardarse en la carpeta de trabajo.

---

> **Fin de las explicaciones de Pandas**  
> Con esto, tienes la lógica paso a paso y las líneas clave de código. Si algo no funciona, revisa cada paso e imprime valores parciales (por ejemplo, `print(df_index.head())`) para debugear.
