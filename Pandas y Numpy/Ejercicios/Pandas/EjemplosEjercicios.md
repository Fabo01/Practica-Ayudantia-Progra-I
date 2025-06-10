# Explicaciones Detalladas – Sección Pandas

Este documento explica en detalle la lógica y la secuencia de cada ejercicio propuesto para practicar con Pandas. Lee detenidamente antes de revisar el código de ejemplo.

---

## Ejercicios Nivel Fácil

### 1. Leer un archivo CSV
- Objetivo: Aprender a leer un archivo CSV y entender qué es un DataFrame.
- Pasos: Importar pandas, leer el archivo, mostrar las primeras filas.
- Código:
```python
import pandas as pd
df = pd.read_csv('alumnos.csv')
print(df.head())
```
- Reflexión: Leer datos externos es el primer paso para cualquier análisis real.

### 2. Seleccionar columnas
- Objetivo: Seleccionar columnas específicas de un DataFrame.
- Código:
```python
df[['Nombre', 'Edad']]
```
- Reflexión: Permite enfocarse en la información relevante y reduce errores.

### 3. Filtrar filas
- Objetivo: Filtrar filas usando condiciones lógicas.
- Código:
```python
df[df['Edad'] > 20]
```
- Reflexión: El filtrado es esencial para análisis exploratorio y limpieza de datos.

### 4. Contar valores únicos en una columna
- Objetivo: Contar valores únicos en una columna.
- Código:
```python
df['Carrera'].nunique()
```
- Reflexión: Ayuda a entender la diversidad de los datos.

### 5. Obtener estadísticas descriptivas
- Objetivo: Obtener estadísticas básicas del DataFrame.
- Código:
```python
df.describe()
```
- Reflexión: Es el primer paso para entender la distribución de los datos.

### 6. Sumar columnas para crear una nueva columna
- Objetivo: Sumar varias columnas para obtener un total semanal.
- Código:
```python
df['TotalSemanal'] = df['Lunes'] + df['Martes'] + df['Miércoles'] + df['Jueves'] + df['Viernes']
```
- Reflexión: Ayuda a analizar tendencias y totales.

### 7. Ordenar un DataFrame por una columna
- Objetivo: Ordenar por una columna específica.
- Código:
```python
df.sort_values(by='TotalSemanal', ascending=False)
```
- Reflexión: Permite identificar valores máximos y mínimos rápidamente.

### 8. Guardar un DataFrame en un archivo CSV
- Objetivo: Exportar datos procesados.
- Código:
```python
df.to_csv('salida.csv', index=False)
```
- Reflexión: Es esencial para compartir o reutilizar análisis.

### 9. Seleccionar filas por índice
- Objetivo: Seleccionar filas por posición.
- Código:
```python
df.iloc[0:3]
```
- Reflexión: Útil para muestras rápidas o depuración.

### 10. Cambiar el nombre de columnas
- Objetivo: Hacer el DataFrame más legible.
- Código:
```python
df.rename(columns={'Nota':'Calificación'}, inplace=True)
```
- Reflexión: Nombres claros facilitan el trabajo en equipo.

---

## Ejercicios Nivel Medio

### 11. Agregar una columna basada en condición
- Objetivo: Crear una columna booleana según condición.
- Código:
```python
df['Aprobado'] = df['Nota'] >= 4.0
```
- Reflexión: Permite análisis más profundos y segmentados.

### 12. Calcular promedio de una columna
- Objetivo: Calcular el promedio de una columna.
- Código:
```python
df['Nota'].mean()
```
- Reflexión: Fundamental para comparar grupos y tomar decisiones.

### 13. Eliminar filas duplicadas
- Objetivo: Limpiar duplicados.
- Código:
```python
df.drop_duplicates()
```
- Reflexión: Mejora la calidad del análisis y evita sesgos.

### 14. Filtrar por múltiples condiciones
- Objetivo: Filtrar usando varias condiciones.
- Código:
```python
df[(df['Aprobado']) & (df['Edad'] > 20)]
```
- Reflexión: Permite análisis más específicos y útiles.

### 15. Pivotar datos
- Objetivo: Reorganizar datos con tabla dinámica.
- Código:
```python
df.pivot_table(index='Carrera', columns='Año', values='Nota', aggfunc='mean')
```
- Reflexión: Útil para reportes y visualización de datos complejos.

### 16. Agrupar por carrera y calcular estadísticas
- Objetivo: Agrupar y calcular promedios por grupo.
- Código:
```python
df.groupby('Carrera')['Nota'].mean()
```
- Reflexión: Permite comparar grupos y detectar patrones.

---

## Ejercicios Nivel Difícil

### 17. Ordenar por nota y mostrar los mejores
- Objetivo: Ordenar y mostrar los mejores alumnos.
- Código:
```python
df.sort_values(by='Nota', ascending=False).head(3)
```
- Reflexión: Ayuda a identificar los mejores, peores o casos extremos.

### 18. Cruzar dos DataFrames
- Objetivo: Unir dos DataFrames usando una columna común.
- Código:
```python
pd.merge(df1, df2, on='ID')
```
- Reflexión: Clave para análisis integrados y responder preguntas complejas.

### 19. Aplicar funciones personalizadas a columnas
- Objetivo: Adaptar el análisis a necesidades específicas.
- Código:
```python
df['Categoria'] = df['Nota'].apply(lambda x: 'Aprobado' if x >= 4.0 else 'Reprobado')
```
- Reflexión: Permite personalizar el análisis.

### 20. Manejo de datos faltantes
- Objetivo: Tratar valores NaN.
- Código:
```python
df['Nota'].fillna(df['Nota'].mean(), inplace=True)
```
- Reflexión: Esencial para evitar errores y obtener resultados confiables.

---

## Ejercicios Nivel Muy Difícil

### 21. Crear un reporte de diferencias entre bodegas
- Objetivo: Calcular la diferencia por producto entre dos bodegas y mostrar el resultado ordenado.
- Código:
```python
df_diff = df_b1.set_index('Producto') - df_b2.set_index('Producto')
df_diff = df_diff.reset_index()
print(df_diff)
print(df_diff.sort_values(by='Lunes', ascending=False).head(1))
```
- Reflexión: Permite identificar rápidamente productos con mayor o menor stock entre bodegas.

### 22. Reporte avanzado de diferencias y análisis
- Objetivo: Calcular la diferencia por producto y día, y mostrar el producto con mayor diferencia para cada día.
- Código:
```python
# Para cada día, ordenar y mostrar el producto con mayor diferencia
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
for dia in dias:
    print(df_diff.sort_values(by=dia, ascending=False).head(1))
```
- Reflexión: Permite un análisis detallado sin necesidad de gráficos.
