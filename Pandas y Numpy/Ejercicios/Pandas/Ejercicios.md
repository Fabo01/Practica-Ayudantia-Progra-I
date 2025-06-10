# Ejercicios de Pandas

## Instrucciones
Resuelve los siguientes ejercicios utilizando la librería Pandas. Puedes elegir la combinación de ejercicios que prefieras para aprobar la sección, por ejemplo:
- 10 ejercicios fáciles
- 6 fáciles y 6 medios
- 4 difíciles
- 2 muy difíciles
El objetivo es completar aproximadamente 40-60 minutos de trabajo efectivo.

---

### Nivel Fácil

1. **Leer un archivo CSV**  
   Descarga el archivo `alumnos.csv` (simulado) y cárgalo en un DataFrame. Muestra las primeras 5 filas.

2. **Seleccionar columnas**  
   Del DataFrame anterior, muestra solo las columnas "Nombre" y "Edad".

3. **Filtrar filas**  
   Muestra solo los alumnos cuya edad sea mayor a 20 años.

4. **Contar valores únicos**  
   Cuenta cuántos valores únicos hay en la columna "Carrera".

5. **Estadísticas descriptivas**  
   Obtén estadísticas descriptivas (como media, mediana, desviación estándar) de la columna "Nota".

6. **Sumar columnas**  
   Crea una nueva columna llamada "Total Semanal" que sea la suma de las columnas "Nota1" y "Nota2".

7. **Ordenar DataFrame**  
   Ordena el DataFrame por la columna "Edad" de menor a mayor.

8. **Guardar DataFrame**  
   Guarda el DataFrame resultante en un nuevo archivo CSV llamado `alumnos_modificado.csv`.

9. **Seleccionar por índice**  
   Muestra las filas con índice 0, 2 y 4.

10. **Renombrar columnas**  
    Cambia el nombre de la columna "Nombre" a "NombreCompleto".

---

### Nivel Medio

11. **Agregar una columna**  
    Agrega una columna "Aprobado" que sea True si la nota es mayor o igual a 4.0, False en caso contrario.

12. **Calcular promedio**  
    Calcula el promedio de las notas de todos los alumnos.

13. **Eliminar duplicados**  
    Elimina las filas duplicadas del DataFrame.

14. **Filtrar múltiples condiciones**  
    Muestra solo los alumnos que están en la carrera de "Ingeniería" y tienen una nota mayor a 3.5.

15. **Pivotar datos**  
    Crea una tabla dinámica que muestre el promedio de notas por carrera y por año.

16. **Agrupar por carrera**  
    Agrupa los alumnos por la columna "Carrera" y muestra el promedio de notas por carrera.

---

### Nivel Difícil

17. **Ordenar por nota**  
    Ordena el DataFrame por la columna "Nota" de mayor a menor y muestra los 3 primeros.

18. **Cruzar dos DataFrames**  
    Tienes dos DataFrames: uno con alumnos y otro con inscripciones a cursos. Une ambos para mostrar qué cursos toma cada alumno.

19. **Aplicar funciones personalizadas**  
    Crea una función que clasifique a los alumnos como "Sobresaliente", "Bien", "Suficiente" o "Insuficiente" según su nota y aplícala a la columna de notas.

20. **Manejo de datos faltantes**  
    Supón que algunas notas están vacías (NaN). Reemplaza los valores faltantes por el promedio general de notas y muestra el DataFrame resultante.

---

### Nivel Muy Difícil

21. **Reporte de diferencias entre bodegas**  
    Tienes datos de ventas de productos en dos bodegas diferentes. Crea un reporte que muestre la diferencia de ventas por producto y por día.

22. **Reporte avanzado**  
    Del reporte anterior, muestra solo el producto con mayor diferencia de ventas para cada día entre las dos bodegas.