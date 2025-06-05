# Explicaciones detalladas de los ejemplos de CustomTkinter (CTk)

A continuación se explican todos los ejemplos incluidos en la carpeta de ejemplos. Cada explicación detalla el objetivo, el uso de los componentes y cómo puedes adaptar el código para tu propio proyecto de inventario.

## ejemplo_ventana.py
Crea una ventana principal usando CTk. Se configura el modo de apariencia y el tema de color. Es la base para cualquier aplicación con CTk. Incluye el método `set_appearance_mode` para definir el modo (claro, oscuro o sistema) y `set_default_color_theme` para el tema de color. El ejemplo muestra cómo iniciar la ventana y es fundamental para cualquier proyecto.

## ejemplo_boton.py
Muestra cómo crear un botón (`CTkButton`) y asociar una función a su evento de clic usando el parámetro `command`. Es fundamental para ejecutar acciones en la interfaz. El ejemplo imprime un mensaje en consola al presionar el botón y muestra cómo conectar lógica a la interfaz.

## ejemplo_entrada.py
Ejemplo de campo de entrada de texto (`CTkEntry`) con un placeholder. Permite al usuario ingresar datos y recuperarlos con `.get()`. Incluye un botón que muestra el texto ingresado en consola. Es útil para formularios y entradas de usuario.

## ejemplo_optionmenu.py
Demuestra el uso de un menú desplegable (`CTkOptionMenu`) para seleccionar entre varias opciones. Incluye un botón que muestra la opción seleccionada en consola. Útil para elegir productos, días, etc. El ejemplo enseña cómo obtener la opción elegida y reaccionar a la selección.

## ejemplo_frame.py
Muestra cómo agrupar widgets dentro de un `CTkFrame`, útil para organizar la interfaz en secciones. Dentro del frame se pueden colocar etiquetas, botones u otros widgets. El ejemplo enseña cómo estructurar la interfaz y separar funcionalidades.

## ejemplo_tabview.py
Explica cómo crear pestañas (`CTkTabview`) para separar distintas vistas o funcionalidades, como en el proyecto final (bodegas, suma, diferencia, etc). Cada pestaña puede contener widgets independientes. El ejemplo muestra cómo agregar y acceder a pestañas.

## ejemplo_scrollableframe.py
Ejemplo de un frame desplazable (`CTkScrollableFrame`), ideal para mostrar listas largas de elementos o tablas. Permite agregar muchos widgets y desplazarse verticalmente. El ejemplo enseña cómo manejar grandes volúmenes de información en la interfaz.

## ejemplo_tabla.py
Simula una tabla usando `CTkFrame` y `CTkLabel`, mostrando cómo organizar datos en filas y columnas, como en la gestión de inventario. Se usan bucles para crear la cuadrícula de etiquetas. Puedes personalizar los colores y el formato de las celdas. El ejemplo explica el uso de `.grid()` y cómo simular tablas.

## ejemplo_treeview.py
Muestra cómo integrar un widget `Treeview` de Tkinter (TK) dentro de una ventana de CustomTkinter (CTk). El `Treeview` permite mostrar datos en forma de tabla, útil para visualizar inventarios o listas de productos. En el ejemplo, se crea una ventana CTk, se añade un frame de Tkinter y dentro de este se coloca el Treeview con columnas para "Producto" y "Cantidad". Se insertan datos de ejemplo y se explica cómo se puede adaptar para mostrar información dinámica del inventario. Se recomienda usarlo cuando se requiere funcionalidad avanzada de tablas.

## ejemplo_app.py
Ejemplo mínimo de una aplicación CTk con solo la ventana principal. Es útil como plantilla base para comenzar cualquier proyecto. Permite experimentar agregando nuevos widgets y funcionalidades.

---
Todos los ejemplos están pensados para ser la base de los componentes usados en el proyecto final de gestión de inventario de bodegas. Revisa cada uno para entender cómo se implementan y cómo puedes adaptarlos a tu proyecto.
