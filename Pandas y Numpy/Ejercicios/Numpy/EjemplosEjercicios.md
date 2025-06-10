# Explicaciones Detalladas – Sección NumPy

Este documento explica en detalle la lógica y la secuencia de cada ejercicio propuesto para practicar con NumPy. Lee detenidamente antes de revisar el código de ejemplo.

---

## Ejercicios Nivel Fácil

### 1. Crear un arreglo secuencial
- **Objetivo:** Crear un arreglo con los números del 1 al 10.
- **Código:**
```python
import numpy as np
arreglo = np.arange(1, 11)
print(arreglo)
print(type(arreglo), arreglo.shape)
```
- **Reflexión:** Los arreglos de Numpy permiten operaciones vectorizadas y son más eficientes que las listas de Python.

---

### 2. Sumar 5 a todos los elementos de un arreglo
- **Objetivo:** Sumar un valor escalar a todos los elementos.
- **Código:**
```python
arreglo = np.arange(1, 11)
resultado = arreglo + 5
print(resultado)
```
- **Reflexión:** Las operaciones vectorizadas son más rápidas y legibles que los bucles for.

---

### 3. Crear una matriz aleatoria 4x4
- **Objetivo:** Generar una matriz 4x4 con valores enteros aleatorios entre 0 y 10.
- **Código:**
```python
matriz = np.random.randint(0, 11, (4,4))
print(matriz)
```
- **Reflexión:** Cada ejecución puede dar resultados distintos a menos que se fije la semilla.

---

### 4. Obtener el máximo y mínimo de un arreglo
- **Objetivo:** Encontrar el valor máximo y mínimo y sus posiciones.
- **Código:**
```python
arreglo = np.random.randint(0, 100, 10)
print('Max:', np.max(arreglo), 'en', np.argmax(arreglo))
print('Min:', np.min(arreglo), 'en', np.argmin(arreglo))
```
- **Reflexión:** Útil para análisis rápidos de datos.

---

### 5. Sumar todos los elementos de un arreglo
- **Objetivo:** Calcular la suma total de los elementos.
- **Código:**
```python
arreglo = np.arange(1, 11)
print(np.sum(arreglo))
```
- **Reflexión:** Numpy realiza sumas de manera eficiente en cualquier dimensión.

---

### 6. Extraer una columna o fila de una matriz
- **Objetivo:** Seleccionar una columna o fila específica.
- **Código:**
```python
matriz = np.random.randint(0, 10, (4,4))
print('Columna 2:', matriz[:,1])
print('Fila 0:', matriz[0,:])
```
- **Reflexión:** Muy útil para análisis por día o producto.

---

### 7. Filtrar valores mayores a un umbral
- **Objetivo:** Usar máscaras booleanas para filtrar.
- **Código:**
```python
arreglo = np.random.randint(0, 20, 10)
print(arreglo[arreglo > 5])
```
- **Reflexión:** Permite análisis rápidos y segmentados.

---

### 8. Reemplazar valores según condición
- **Objetivo:** Asignar un valor a los elementos que cumplen una condición.
- **Código:**
```python
arreglo = np.random.randint(0, 10, 10)
arreglo[arreglo < 3] = 0
print(arreglo)
```
- **Reflexión:** Útil para limpiar o transformar datos.

---

### 9. Contar cuántos elementos cumplen una condición
- **Objetivo:** Contar elementos que cumplen una condición.
- **Código:**
```python
arreglo = np.random.randint(0, 10, 20)
print(np.sum(arreglo > 5))
```
- **Reflexión:** Útil para reportes rápidos.

---

### 10. Crear un arreglo de ceros o unos
- **Objetivo:** Inicializar arreglos de ceros o unos.
- **Código:**
```python
ceros = np.zeros((3,4))
unos = np.ones((2,5))
print(ceros)
print(unos)
```
- **Reflexión:** Útil para preparar estructuras antes de cargar datos reales.

---

## Ejercicios Nivel Medio

### 11. Suma y resta de matrices
- **Objetivo:** Sumar y restar matrices del mismo tamaño.
- **Código:**
```python
A = np.random.randint(0, 10, (3,3))
B = np.random.randint(0, 10, (3,3))
print('Suma:\n', A+B)
print('Resta:\n', A-B)
```
- **Reflexión:** Ambas matrices deben tener la misma forma.

---

### 12. Obtener la diagonal principal
- **Objetivo:** Extraer la diagonal principal de una matriz cuadrada.
- **Código:**
```python
M = np.random.randint(0, 10, (4,4))
diag = np.diag(M)
print(diag)
```
- **Reflexión:** Útil para análisis matemáticos y subconjuntos de datos.

---

### 13. Transponer una matriz
- **Objetivo:** Intercambiar filas por columnas.
- **Código:**
```python
M = np.random.randint(0, 10, (3,4))
print(M.T)
```
- **Reflexión:** Fundamental en álgebra lineal y manejo de datos.

---

### 14. Sumar por filas y columnas
- **Objetivo:** Sumar elementos por filas o columnas.
- **Código:**
```python
M = np.random.randint(0, 10, (3,4))
print('Suma por columnas:', np.sum(M, axis=0))
print('Suma por filas:', np.sum(M, axis=1))
```
- **Reflexión:** El parámetro axis es clave para controlar la dirección de la suma.

---

### 15. Aplicar una función a todos los elementos
- **Objetivo:** Elevar al cuadrado todos los elementos.
- **Código:**
```python
arreglo = np.arange(1, 6)
print(arreglo ** 2)
```
- **Reflexión:** Las operaciones vectorizadas son muy potentes en Numpy.

---

### 16. Concatenar arreglos
- **Objetivo:** Unir dos arreglos por filas o columnas.
- **Código:**
```python
a = np.ones((2,3))
b = np.zeros((2,3))
print(np.concatenate([a, b], axis=0))
print(np.concatenate([a, b], axis=1))
```
- **Reflexión:** Útil para juntar datos de diferentes fuentes.

---

## Ejercicios Nivel Difícil

### 17. Producto de matrices
- **Objetivo:** Calcular el producto matricial de dos matrices compatibles.
- **Código:**
```python
A = np.random.randint(0, 10, (3,4))
B = np.random.randint(0, 10, (4,2))
print(np.dot(A, B))
# o
print(A @ B)
```
- **Reflexión:** El producto matricial requiere dimensiones compatibles.

---

### 18. Normalización de un arreglo
- **Objetivo:** Restar la media y dividir por la desviación estándar.
- **Código:**
```python
arreglo = np.random.randint(0, 100, 10)
norm = (arreglo - arreglo.mean()) / arreglo.std()
print(norm)
```
- **Reflexión:** Fundamental en análisis de datos y machine learning.

---

### 19. Sumar triángulo superior e inferior de una matriz
- **Objetivo:** Sumar los valores del triángulo superior e inferior de una matriz cuadrada.
- **Código:**
```python
M = np.random.randint(0, 10, (4,4))
sup = np.sum(np.triu(M, 1))
inf = np.sum(np.tril(M, -1))
print('Superior:', sup, 'Inferior:', inf)
```
- **Reflexión:** Útil para análisis de matrices de correlación o inventarios.

---

### 20. Cargar datos desde un CSV y operar
- **Objetivo:** Leer datos numéricos desde un archivo CSV y operar.
- **Código:**
```python
A = np.loadtxt('matriz1.csv', delimiter=',')
B = np.loadtxt('matriz2.csv', delimiter=',')
print('Suma por filas:', np.sum(A, axis=1))
print('Diferencia:', A - B)
```
- **Reflexión:** Importante para análisis de datos reales.

---

## Ejercicios Nivel Muy Difícil

### 21. Encontrar valores únicos y sus frecuencias
- **Objetivo:** Encontrar los valores únicos y cuántas veces aparece cada uno en un arreglo.
- **Código:**
```python
arreglo = np.random.randint(0, 11, 100)
valores, cuentas = np.unique(arreglo, return_counts=True)
print('Valores:', valores)
print('Frecuencias:', cuentas)
```
- **Reflexión:** Útil para análisis estadístico y distribución de datos.

---

### 22. Resolver un sistema de ecuaciones lineales
- **Objetivo:** Resolver Ax = b con A cuadrada y b compatible.
- **Código:**
```python
A = np.random.randint(1, 10, (3,3))
b = np.random.randint(1, 10, 3)
x = np.linalg.solve(A, b)
print('Solución:', x)
```
- **Reflexión:** Numpy permite resolver sistemas lineales de forma eficiente.

---

> **Fin de las explicaciones de NumPy**  
> Ahora que tienes la lógica completa, revisa cada bloque en el código de ejemplos. Si algo falla, imprime valores intermedios (`print(sup_idx, inf_idx, diag)`) para verificar índices.

