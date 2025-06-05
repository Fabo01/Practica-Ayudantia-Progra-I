# Explicaciones de Ejercicios de Pandas

## Nivel Fácil

1. **Leer un archivo CSV**  
   Para leer un archivo CSV en Pandas se utiliza `pd.read_csv('archivo.csv')`. Esto carga los datos en un DataFrame, que es una estructura tabular similar a una hoja de cálculo. Es importante explicar qué es un DataFrame y cómo acceder a sus filas y columnas. Mostrar cómo ver las primeras filas con `.head()` y cómo asegurarse de que el archivo está en la ruta correcta. Reflexión: Leer datos externos es el primer paso para cualquier análisis de datos real.

2. **Seleccionar columnas**  
   Para seleccionar columnas específicas de un DataFrame, se usan corchetes: `df[['Nombre', 'Edad']]`. Esto devuelve un nuevo DataFrame solo con esas columnas. Es útil para trabajar solo con los datos relevantes y evitar errores al manipular columnas que no se necesitan. Reflexión: Seleccionar columnas permite enfocarse en la información relevante y reduce errores.

3. **Filtrar filas**  
   Filtrar filas se hace usando condiciones lógicas, por ejemplo: `df[df['Edad'] > 20]`. Esto devuelve solo las filas donde la condición se cumple. Es importante explicar la diferencia entre el filtrado con listas y con DataFrames, y cómo Pandas permite hacerlo de forma eficiente y legible. Reflexión: El filtrado es esencial para análisis exploratorio y limpieza de datos.

4. **Contar valores únicos en una columna**  
   Para contar cuántos valores únicos hay en una columna, se usa `df['Columna'].nunique()`. Esto es útil para entender la diversidad de datos, por ejemplo, cuántas carreras distintas hay. Reflexión: Saber la cantidad de categorías ayuda a planificar análisis posteriores.

5. **Obtener estadísticas descriptivas**  
   Pandas permite obtener estadísticas básicas con `df.describe()`, que muestra media, desviación estándar, mínimo, máximo, etc. Reflexión: Las estadísticas descriptivas son el primer paso para entender la distribución de los datos.

6. **Sumar columnas para crear una nueva columna**  
   Puedes sumar varias columnas de un DataFrame para obtener un total semanal, por ejemplo: `df['Total'] = df['Lunes'] + df['Martes'] + ...`. Esto es útil para obtener métricas agregadas. Reflexión: Crear columnas derivadas ayuda a analizar tendencias y totales.

7. **Ordenar un DataFrame por una columna**  
   Usar `df.sort_values(by='Total', ascending=False)` permite ordenar los datos por una columna específica. Reflexión: Ordenar ayuda a identificar los valores máximos y mínimos rápidamente.

8. **Guardar un DataFrame en un archivo CSV**  
   Con `df.to_csv('archivo_salida.csv', index=False)` puedes exportar tus datos procesados. Reflexión: Guardar resultados es esencial para compartir o reutilizar análisis.

9. **Seleccionar filas por índice**  
   Usar `df.iloc[0:3]` selecciona las primeras tres filas. Reflexión: Acceder por posición es útil para muestras rápidas o depuración.

10. **Cambiar el nombre de columnas**  
    Con `df.rename(columns={'Viejo':'Nuevo'}, inplace=True)` puedes hacer tu DataFrame más legible. Reflexión: Nombres claros facilitan el trabajo en equipo y la comprensión del código.

---

## Nivel Medio

11. **Agregar una columna basada en condición**  
    Puedes crear una columna booleana, por ejemplo: `df['Aprobado'] = df['Nota'] >= 4.0`. Reflexión: Clasificar datos permite análisis más profundos y segmentados.

12. **Calcular promedio de una columna**  
    El promedio de una columna se calcula con `df['Nota'].mean()`. Reflexión: Calcular promedios es fundamental para comparar grupos y tomar decisiones.

13. **Eliminar filas duplicadas**  
    Para eliminar filas duplicadas se usa `df.drop_duplicates()`. Reflexión: Limpiar duplicados mejora la calidad del análisis y evita sesgos.

14. **Filtrar por múltiples condiciones**  
    Se pueden combinar condiciones usando `&` (y) o `|` (o): `df[(df['Aprobado']) & (df['Edad'] > 20)]`. Reflexión: Filtrar por varias condiciones permite análisis más específicos y útiles.

15. **Pivotar datos**  
    Para reorganizar datos se usa `df.pivot_table()`. Por ejemplo, para ver el promedio de notas por carrera y año. Reflexión: Pivotar es útil para reportes y visualización de datos complejos.

16. **Agrupar por carrera y calcular estadísticas**  
    Usar `df.groupby('Carrera')['Nota'].mean()` permite obtener promedios por grupo. Reflexión: Agrupar permite comparar grupos y detectar patrones o diferencias.

---

## Nivel Difícil

17. **Ordenar por nota y mostrar los mejores**  
    Ordenar un DataFrame por la columna 'Nota' de mayor a menor y mostrar los 3 primeros con `.head(3)`. Reflexión: Ordenar datos ayuda a identificar los mejores, peores o casos extremos.

18. **Cruzar dos DataFrames**  
    Para unir dos DataFrames, se usa `pd.merge(df1, df2, on='ID')` o una columna común. Reflexión: Cruzar datos es clave para análisis integrados y para responder preguntas complejas.

19. **Aplicar funciones personalizadas a columnas**  
    Se pueden aplicar funciones propias a columnas usando `.apply()`. Por ejemplo, para categorizar notas. Reflexión: Aplicar funciones personalizadas permite adaptar el análisis a necesidades específicas.

20. **Manejo de datos faltantes**  
    Los valores faltantes (NaN) son comunes en datos reales. Para reemplazarlos por el promedio, se usa `df['Nota'].fillna(df['Nota'].mean(), inplace=True)`. Reflexión: Tratar los datos faltantes es esencial para evitar errores y obtener resultados confiables.

---

## Nivel Muy Difícil

21. **Crear un reporte de diferencias entre bodegas**  
    Combina datos de dos bodegas, calcula la diferencia por producto y muestra el resultado en un DataFrame. Reflexión: Comparar diferencias ayuda a detectar rápidamente anomalías o patrones. Puedes mostrar el DataFrame ordenado por la mayor diferencia, pero no se debe graficar ni usar librerías externas. Ejemplo de código:
    ```python
    # Supón que tienes dos DataFrames: df_b1 y df_b2, ambos con columna 'Producto' y columnas de días
    df_diff = df_b1.set_index('Producto') - df_b2.set_index('Producto')
    df_diff = df_diff.reset_index()
    print(df_diff)
    # Para ver el producto con mayor diferencia en un día específico:
    print(df_diff.sort_values(by='Lunes', ascending=False).head(1))
    ```
    Reflexión: Visualizar diferencias en tablas permite identificar rápidamente productos con mayor o menor stock entre bodegas, sin necesidad de gráficos.

---

**Nota:** Cada explicación debe ir acompañada de ejemplos de código y de una reflexión sobre cómo se relaciona con el manejo de datos, la programación y el análisis real. Se recomienda que el docente refuerce la importancia de entender la lógica detrás de cada operación y su utilidad en problemas reales.