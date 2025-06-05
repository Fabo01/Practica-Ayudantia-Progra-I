# Ejercicios prácticos de CustomTkinter (CTk)

A continuación encontrarás ejercicios detallados para practicar cada componente de CTk. Lee atentamente las instrucciones y completa cada ejercicio, recuerda probar las funcionalidades, experimentar y comprender la lógica para utilizar la interfaz.

Consideren comentar cada codigo, sus funciones principales y lógica más compleja para que luego cuando hagan su proyecto puedan volver y utilizar los ejercicios para su proyecto.

## Ejercicio 1: Ventana y etiqueta
Crea una ventana principal usando CTk (`CTk()`) y agrega una etiqueta (`CTkLabel`) que muestre algún texto, por ejemplo "Interfaz bakana de Ctk". La ventana debe tener un tamaño de 777x333 píxeles.


## Ejercicio 2: Botón contador
Crea una ventana con un botón (`CTkButton`) y una etiqueta (`CTkLabel`). Cada vez que presiones el botón, la etiqueta debe actualizarse mostrando cuántas veces se ha presionado el botón. Usa una variable para llevar la cuenta y el método `.configure()` para actualizar el texto de la etiqueta.

## Ejercicio 3: Entrada y saludo
Haz una ventana con un campo de entrada de texto (`CTkEntry`) y un botón. Al presionar el botón, muestra en una etiqueta el texto "Hola, <nombre>!" usando el nombre ingresado en el campo de entrada. Utiliza el método `.get()` para obtener el texto.

## Ejercicio 4: OptionMenu de productos
Crea un `CTkOptionMenu` con al menos 3 productos diferentes. Al seleccionar uno y presionar un botón, muestra el producto seleccionado en una etiqueta. Usa el método `.get()` del OptionMenu para obtener la opción elegida.

## Ejercicio 5: Frame de datos
Crea un `CTkFrame` que contenga dos etiquetas y dos campos de entrada para ingresar el nombre y la cantidad de un producto. Añade un botón que, al presionarlo, muestre los datos ingresados en una etiqueta fuera del frame.

## Ejercicio 6: Tabview de bodegas
Crea una ventana con un `CTkTabview` que tenga dos pestañas: "Bodega 1" y "Bodega 2". En cada pestaña, coloca una etiqueta diferente que indique el nombre de la bodega.

## Ejercicio 7: ScrollableFrame de lista
Crea un `CTkScrollableFrame` y agrega dentro de él 10 o 20 etiquetas numeradas (por ejemplo, "Producto 1", "Producto 2", ...). La idea es que el ScrollableFrame debe permitir desplazarse si no caben todas las etiquetas en pantalla.

## Ejercicio 8: Tabla simple
Simula una tabla de inventario con 3 productos y 3 días usando `CTkFrame` y `CTkLabel`, organizando los datos en filas y columnas. Cada fila debe mostrar el nombre del producto y las cantidades para cada día. Para esto deben usar `.grid()` o `.pack()`

## Ejercicio 9: Tabla avanzada con Treeview
Crea una ventana CTk que integre un widget `Treeview` de Tkinter para mostrar una tabla de productos y cantidades. Inserta al menos 3 filas de ejemplo.

## Ejercicio 10: App integradora de inventario
Desarrolla una aplicación sencilla que integre los componentes anteriores:
- Una ventana principal con título y tamaño personalizado.
- Un `CTkTabview` con dos pestañas: "Agregar producto" y "Ver inventario".
- En "Agregar producto": un frame con campos para nombre y cantidad, y un botón para agregar productos a una lista interna.
- En "Ver inventario": muestra la lista de productos agregados en una tabla simulada usando `CTkFrame` y `CTkLabel`.
- Opcional: Agrega un botón para limpiar la lista de productos y un tabview adicional para mostrar los productos con un treeview.
- Ten en cuenta que esto es para practicar Ctk, no tomes en cuenta validaciones o operaciones complejas.

---

Todos los ejercicios deben resolverse solo con CustomTkinter (CTk) y, si es necesario, Tkinter para componentes avanzados como Treeview. Explica tu código con comentarios y prueba cada funcionalidad. Tengan en cuenta que estos ejercicios simples les servirán para la creación de la interfaz de la bodega.