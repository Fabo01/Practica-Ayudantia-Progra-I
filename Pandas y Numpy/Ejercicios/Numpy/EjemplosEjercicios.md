# Explicaciones Detalladas – Sección NumPy

Este documento explica en detalle la lógica y la secuencia de cada ejercicio propuesto para practicar con NumPy. Lee detenidamente antes de revisar el código de ejemplo.

---

## Ejercicios Nivel Fácil

### NumPy-Fácil-1

1. **Objetivo:** Crear un arreglo NumPy que represente la tabla de inventarios y revisar su forma y tipo.  
2. **Pasos:**
   - Importar NumPy: `import numpy as np`.  
   - Construir la lista de listas (5 filas × 6 columnas) con los datos numéricos.  
   - Convertirla a arreglo: `A = np.array(lista)`; el tipo (`dtype`) será `int64` si todos son enteros.  
   - Llamar `A.shape` para verificar que la forma sea `(5, 6)`.  
   - Llamar `A.dtype` para ver que sea un tipo numérico (entero).  
   - Para “primera fila completa”: `A[0, :]`.  
   - Para “última columna completa”: `A[:, -1]`.  
3. **Por qué funciona:**  
   - NumPy representa matrices en memoria contigua; `shape` e `dtype` son atributos.  
   - `A[i, :]` selecciona toda la fila en la posición `i`.  
   - `A[:, -1]` selecciona la última columna.

---

### NumPy-Fácil-2

1. **Objetivo:** Extraer columnas con índices específicos (martes, viernes).  
2. **Pasos:**
   - Asumir que `A` ya está definido.  
   - Día “Lunes” → columna índice 0: `v_lunes = A[:, 0]`.  
   - Día “Viernes” → columna índice 4 (contando desde 0): `v_viernes = A[:, 4]`.  
   - Sumar con `np.sum(v_lunes)` y `np.sum(v_viernes)`.  
3. **Por qué funciona:**  
   - En NumPy, `A[:, j]` toma todas las filas (`:`) en la columna `j`.  
   - `np.sum` suma todos los elementos del arreglo dado.

---

### NumPy-Fácil-3

1. **Objetivo:** Calcular la suma por fila (total semanal) y encontrar fila con mayor suma.  
2. **Pasos:**
   - Dado `A` de tamaño `(5, 6)`, pero **ojo**: la primera columna (índice 0) correspondería a “Producto” si fuera numérico. Si estamos usando solo valores numéricos (sin “Producto”), entonces `A` debe ser `(5,5)` con sólo los días.  
   - Supongamos que ya tienes `A5` de tamaño `(5,5)` (días). Entonces:  
     ```python
     prod_total = np.sum(A5, axis=1)
     ```
     donde `axis=1` suma por fila.  
   - Para encontrar índice de mayor suma: `indice_max = np.argmax(prod_total)`.  
   - Imprimir `prod_total` y `indice_max`.  
3. **Por qué funciona:**  
   - `np.sum(..., axis=1)` suma horizontalmente (cada fila).  
   - `np.argmax` devuelve la posición del máximo en una dimensión.

---

### NumPy-Fácil-4

1. **Objetivo:** Generar un arreglo aleatorio y aplicar máscara booleana para reemplazar valores bajos.  
2. **Pasos:**
   - Importar NumPy: `import numpy as np`.  
   - Generar arreglo: `M = np.random.randint(0, 51, size=(5,5))`.  
   - Crear máscara: `mascara = M < 10`.  
   - Aplicar: `M[mascara] = 0`.  
   - Imprimir `M`.  
3. **Por qué funciona:**  
   - `np.random.randint(a, b, size=(m,n))` produce números enteros entre `a` y `b-1`.  
   - La comparación `M < 10` genera una matriz booleana.  
   - Asignar `M[mascara] = 0` sustituye en todos los lugares donde la máscara es `True`.

---

## Ejercicios Nivel Medio

### NumPy-Medio-1

1. **Objetivo:** Practicar suma y resta de arreglos de igual tamaño.  
2. **Pasos:**
   - Crear arreglos `A` y `B` de tamaño `(5,5)`, por ejemplo:  
     ```python
     import numpy as np
     A = np.array([[1,2,3,4,5],
                   [5,4,3,2,1],
                   [2,2,2,2,2],
                   [0,1,0,1,0],
                   [7,8,9,8,7]])
     B = np.random.randint(0, 50, size=(5,5))
     ```
   - Calcular `D = A - B` (resta elemento a elemento) y `S = A + B` (suma elemento a elemento).  
   - Imprimir usando `print("A =\n", A)`, etc.  
3. **Por qué funciona:**  
   - NumPy sobrecarga operadores `+` y `-` para hacer operaciones elemento a elemento cuando los arreglos tienen la misma forma.

---

### NumPy-Medio-2

1. **Objetivo:** Obtener transpuesta, diagonal y suma de diagonal.  
2. **Pasos:**
   - Asumir un arreglo `M` de tamaño `(5,5)`.  
   - Transpuesta: `M_T = M.T` o `np.transpose(M)`.  
   - Vector diagonal: `diag = np.diag(M)`.  
   - Suma diagonal: `suma_diag = np.sum(diag)`.  
   - Imprimir resultados por separado.  
3. **Por qué funciona:**  
   - `M.T` invierte filas ↔ columnas.  
   - `np.diag(M)` extrae diagonal principal.  
   - `np.sum` sobre un vector suma todos sus elementos.

---

### NumPy-Medio-3

1. **Objetivo:** Calcular sumas de triángulo superior e inferior de una matriz rectangular.  
2. **Pasos:**
   - Dado `M` de tamaño `(5,7)`.  
   - Para índices del triángulo superior:  
     ```python
     tri_sup_idx = np.triu_indices(n=M.shape[0], k=1, m=M.shape[1])
     suma_superior = np.sum(M[tri_sup_idx])
     ```
     - `k=1` indica “estrictamente superior” (i<j).  
   - Para triángulo inferior:  
     ```python
     tri_inf_idx = np.tril_indices(n=M.shape[0], k=-1, m=M.shape[1])
     suma_inferior = np.sum(M[tri_inf_idx])
     ```
   - Imprimir ambas sumas.  
3. **Por qué funciona:**  
   - `np.triu_indices(n, k, m)` devuelve tuplas de índices `(filas, columnas)` donde `fila + k <= columna < m`.  
   - Similar `np.tril_indices` con `k=-1` para “estrictamente inferior”.  
   - Luego `M[filas, columnas]` selecciona todos esos elementos y `np.sum` los suma.

---

## Ejercicios Nivel Difícil

### NumPy-Difícil-1

1. **Objetivo:** Implementar función que “resalte” (duplica) valores por encima de un umbral en una matriz.  
2. **Pasos:**
   - Definir función:
     ```python
     import numpy as np

     def resaltar_mayores(A, umbral):
         # 1. Crear copia para no modificar A original
         B = A.copy()
         # 2. Máscara booleana
         mascara = B > umbral
         # 3. Multiplicar sólo donde la máscara es True
         B[mascara] = B[mascara] * 2
         return B
     ```
   - Probar con:
     ```python
     A = np.arange(1, 26).reshape((5,5))  # crea matriz 5×5 con números 1 a 25
     umbral = 10
     B = resaltar_mayores(A, umbral)
     print("A original:\n", A)
     print("A modificado (valores > 10 duplicados):\n", B)
     ```
3. **Por qué funciona:**
   - `A.copy()` evita cambiar el arreglo original.  
   - `B > umbral` genera un arreglo booleano del mismo tamaño que `B`.  
   - `B[mascara]` selecciona todos los valores que cumplen la condición y los multiplica por 2.

---

### NumPy-Difícil-2

1. **Objetivo:** Cargar datos de CSV de bodegas como arreglos NumPy y calcular diferencia por producto.  
2. **Pasos:**
   - Importar NumPy y leer archivos:
     ```python
     import numpy as np

     # Leer sólo los valores numéricos (sin la columna “Producto”)
     A_B1 = np.loadtxt("bodega1.csv", delimiter=",", skiprows=1, usecols=range(1,6))
     A_B2 = np.loadtxt("bodega2.csv", delimiter=",", skiprows=1, usecols=range(1,6))
     ```
   - Si los arreglos no tienen la misma forma (por ejemplo, diferente número de filas), rellenar con ceros:
     ```python
     filas1, cols1 = A_B1.shape
     filas2, cols2 = A_B2.shape
     filas_max = max(filas1, filas2)
     # Crear nuevos arreglos de ceros con forma (filas_max, 5)
     temp1 = np.zeros((filas_max, cols1))
     temp2 = np.zeros((filas_max, cols2))
     # Copiar datos originales al principio
     temp1[:filas1, :] = A_B1
     temp2[:filas2, :] = A_B2
     A_B1 = temp1
     A_B2 = temp2
     ```
   - Calcular `D = A_B1 - A_B2`.  
   - Calcular suma por fila:
     ```python
     diferencia_total_por_producto = np.sum(D, axis=1)
     ```
   - Encontrar índice con mayor diferencia:
     ```python
     idx_max = np.argmax(diferencia_total_por_producto)
     ```
   - Imprimir vector y `idx_max`.  
3. **Por qué funciona:**  
   - `np.loadtxt` carga directamente valores numéricos (columnas 1–5).  
   - Al tener que “igualar” dimensiones, crear un arreglo nuevo lleno de ceros y copiar las filas originales al principio es la forma más sencilla.  
   - Sumar por fila con `axis=1` y luego usar `argmax`.

---

## Ejercicios Nivel Muy Difícil

### NumPy-MuyDifícil-1

1. **Objetivo:** Implementar funciones para sumar triángulos y diagonal, y graficar resultados.  
2. **Pasos:**
   - Definir la matriz `A` (Bodega1) y matriz `B` (Bodega2) de tamaño `(5,5)`, ya sea manualmente o usando `np.random`.  
   - Calcular `D = A - B`.  
   - **Función `sumas_triangular(D)`:**
     ```python
     import numpy as np

     def sumas_triangular(D):
         # Triangular superior (i < j)
         tri_sup_idx = np.triu_indices(n=D.shape[0], k=1)
         suma_superior = np.sum(D[tri_sup_idx])

         # Triangular inferior (i > j)
         tri_inf_idx = np.tril_indices(n=D.shape[0], k=-1)
         suma_inferior = np.sum(D[tri_inf_idx])

         return suma_superior, suma_inferior
     ```
   - **Función `suma_diagonal(D)`:**
     ```python
     def suma_diagonal(D):
         # np.diag(D) extrae la diagonal principal
         return np.sum(np.diag(D))
     ```
   - Probar ambas funciones:
     ```python
     s_sup, s_inf = sumas_triangular(D)
     s_diag = suma_diagonal(D)
     print(f"Suma Triangular Superior: {s_sup}")
     print(f"Suma Triangular Inferior: {s_inf}")
     print(f"Suma Diagonal Principal: {s_diag}")
     ```
   - **Gráfico de barras con Matplotlib:**
     ```python
     import matplotlib.pyplot as plt

     categorias = ["Superior", "Inferior", "Diagonal"]
     valores = [s_sup, s_inf, s_diag]

     plt.figure(figsize=(6, 4))
     plt.bar(categorias, valores)
     plt.title("Sumas de Triángulos y Diagonal de D = A - B")
     plt.xlabel("Categoría")
     plt.ylabel("Suma de Valores")
     for i, val in enumerate(valores):
         plt.text(i, val + 0.02 * max(valores), str(val), ha="center")
     plt.tight_layout()
     plt.savefig("barras_sumas.png", dpi=300)
     plt.show()
     ```
   - Con esto, generas la figura `barras_sumas.png`.
3. **Puntos clave:**
   - `np.triu_indices(n, k)` asume cuadrada; si fuera rectangular, usar `np.triu_indices(n, k, m)`.  
   - `np.diag(D)` devuelve un vector de tamaño `n` (elementos `(0,0), (1,1), …`).  
   - En el gráfico, usamos `plt.bar` y luego `plt.text` para anotar cada barra con su valor.

---

> **Fin de las explicaciones de NumPy**  
> Ahora que tienes la lógica completa, revisa cada bloque en el código de ejemplos. Si algo falla, imprime valores intermedios (`print(sup_idx, inf_idx, diag)`) para verificar índices.

