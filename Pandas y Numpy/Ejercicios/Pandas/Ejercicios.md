# Ejercicios de Pandas

## Instrucciones
Resuelve los siguientes ejercicios utilizando la librería Pandas. Puedes elegir la combinación de ejercicios que prefieras para aprobar la sección, por ejemplo:
- 10 ejercicios fáciles
- 5 fáciles y 5 medios
- 3 difíciles y 1 muy difícil
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

---

### Nivel Medio

4. **Agregar una columna**  
   Agrega una columna "Aprobado" que sea True si la nota es mayor o igual a 4.0, False en caso contrario.

5. **Calcular promedio**  
   Calcula el promedio de las notas de todos los alumnos.

---

### Nivel Difícil

6. **Agrupar por carrera**  
   Agrupa los alumnos por la columna "Carrera" y muestra el promedio de notas por carrera.

7. **Ordenar por nota**  
   Ordena el DataFrame por la columna "Nota" de mayor a menor y muestra los 3 primeros.

---

### Nivel Muy Difícil

8. **Manejo de datos faltantes**  
   Supón que algunas notas están vacías (NaN). Reemplaza los valores faltantes por el promedio general de notas y muestra el DataFrame resultante.

9. **Cruzar dos DataFrames**  
   Tienes dos DataFrames: uno con alumnos y otro con inscripciones a cursos. Une ambos para mostrar qué cursos toma cada alumno.