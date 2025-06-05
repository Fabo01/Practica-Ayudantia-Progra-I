# Explicaciones de Ejercicios de Numpy

## Nivel Fácil

1. **Crear un arreglo secuencial**  
   Para crear un arreglo con los números del 1 al 10 en Numpy, se utiliza `np.arange(1, 11)`. Esto genera un arreglo de tipo `numpy.ndarray` que permite operaciones vectorizadas. Es importante explicar la diferencia entre listas de Python y arreglos de Numpy: los arreglos permiten operaciones matemáticas directas sobre todos sus elementos. Se puede mostrar cómo imprimir el tipo de dato y la forma del arreglo con `type()` y `.shape`.

2. **Operaciones básicas sobre arreglos**  
   Sumar 5 a todos los elementos de un arreglo en Numpy se hace con `arreglo + 5`. Esto es una operación vectorizada, mucho más eficiente que usar ciclos for. Se puede comparar con la forma tradicional usando un ciclo for para reforzar la diferencia.

3. **Crear una matriz aleatoria 4x4**  
   Para generar una matriz 4x4 con valores enteros aleatorios entre 0 y 10, se usa `np.random.randint(0, 11, (4,4))`. Es importante recalcar que los valores pueden repetirse y que cada ejecución puede dar resultados diferentes a menos que se fije la semilla con `np.random.seed`.

4. **Obtener el máximo y mínimo de un arreglo**  
   Para encontrar el valor máximo y mínimo de un arreglo, se usan las funciones `np.max(arreglo)` y `np.min(arreglo)`. También se puede obtener la posición con `np.argmax()` y `np.argmin()`.

5. **Sumar todos los elementos de un arreglo**  
   La suma total de los elementos de un arreglo se obtiene con `np.sum(arreglo)`. Numpy realiza esta operación de manera eficiente y se puede usar para arreglos de cualquier dimensión.

6. **Extraer una columna o fila de una matriz**  
   Para extraer una columna, se usa `matriz[:, indice]`. Para una fila, `matriz[indice, :]`. Esto es útil para analizar datos por día o por producto en el contexto de inventarios.

7. **Filtrar valores mayores a un umbral**  
   Se puede usar una máscara booleana: `arreglo[arreglo > 5]` devuelve solo los valores mayores a 5. Es útil para análisis de inventarios o ventas.

8. **Reemplazar valores según condición**  
   Usando máscaras booleanas, se puede asignar un valor a los elementos que cumplen una condición: `arreglo[arreglo < 3] = 0`.

9. **Contar cuántos elementos cumplen una condición**  
   Se puede usar `np.sum(arreglo > 5)` para contar cuántos elementos son mayores a 5. Esto es útil para reportes rápidos.

10. **Crear un arreglo de ceros o unos**  
    Para inicializar arreglos, se usan `np.zeros((filas, columnas))` o `np.ones((filas, columnas))`. Es útil para preparar estructuras antes de cargar datos reales.

---

## Nivel Medio

11. **Suma y resta de matrices**  
    Para sumar y restar matrices en Numpy, basta con usar los operadores `+` y `-` entre dos arreglos del mismo tamaño. Es fundamental que ambas matrices tengan la misma forma, de lo contrario Numpy lanzará un error de broadcasting. Se recomienda mostrar cómo imprimir las matrices y sus dimensiones usando `shape`.

12. **Obtener la diagonal principal**  
    La función `np.diag(matriz)` extrae la diagonal principal de una matriz cuadrada. Esto es útil para análisis matemáticos y para entender cómo acceder a subconjuntos de datos en Numpy.

13. **Transponer una matriz**  
    Transponer una matriz significa intercambiar sus filas por columnas. En Numpy se hace con `.T` o `np.transpose(matriz)`. Es importante explicar el concepto de transposición y cómo se usa en álgebra lineal y en el manejo de datos.

14. **Sumar por filas y columnas**  
    Para sumar los elementos por filas o columnas se usa `np.sum(matriz, axis=0)` (columnas) y `np.sum(matriz, axis=1)` (filas). Es importante explicar el parámetro `axis` y cómo afecta el resultado.

15. **Aplicar una función a todos los elementos**  
    Se puede usar `np.vectorize` o simplemente operaciones directas: por ejemplo, elevar al cuadrado todos los elementos con `arreglo ** 2`.

16. **Concatenar arreglos**  
    Para unir dos arreglos, se usa `np.concatenate([a, b], axis=0)` para filas o `axis=1` para columnas. Es útil para juntar datos de diferentes fuentes.

---

## Nivel Difícil

17. **Producto de matrices**  
    El producto matricial (multiplicación de matrices) se realiza con `np.dot(A, B)` o el operador `@`. Es importante diferenciar entre el producto elemento a elemento (`*`) y el producto matricial. El producto matricial requiere que el número de columnas de la primera matriz sea igual al número de filas de la segunda.

18. **Normalización de un arreglo**  
    Normalizar un arreglo significa restar la media y dividir por la desviación estándar: `(arreglo - arreglo.mean()) / arreglo.std()`. Esto es común en análisis de datos y machine learning para que los datos tengan media 0 y desviación estándar 1.

19. **Sumar triángulo superior e inferior de una matriz**  
    Usando `np.triu` y `np.tril`, se pueden obtener las sumas de los triángulos superior e inferior de una matriz cuadrada. Es útil para análisis de matrices de correlación o inventarios.

20. **Cargar datos desde un CSV y operar**  
    Usando `np.loadtxt` o `np.genfromtxt`, se pueden cargar datos numéricos desde un archivo CSV y realizar operaciones como suma por filas, diferencia entre matrices, etc. Es importante explicar el manejo de archivos y la conversión de datos.

---

## Nivel Muy Difícil

21. **Encontrar valores únicos y sus frecuencias**  
    Para encontrar los valores únicos y cuántas veces aparece cada uno en un arreglo, se usa `np.unique(arreglo, return_counts=True)`. Esto devuelve dos arreglos: uno con los valores únicos y otro con la cantidad de veces que aparece cada uno. Es útil para análisis estadístico y para entender la distribución de los datos.

22. **Resolver un sistema de ecuaciones lineales**  
    Para resolver un sistema Ax = b, se usa `np.linalg.solve(A, b)`. Aquí, `A` debe ser una matriz cuadrada (por ejemplo, 3x3) y `b` un vector de tamaño compatible. Numpy calcula la solución exacta si existe. Es importante explicar que si el sistema no tiene solución o es indeterminado, Numpy lanzará un error.

---

**Nota:** Cada explicación debe ir acompañada de ejemplos de código y de una reflexión sobre cómo se relaciona con el manejo de datos, la programación y el análisis numérico. Se recomienda que el docente refuerce la importancia de entender la lógica detrás de cada operación y su utilidad en problemas reales.