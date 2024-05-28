Prueba-DRF-B4D
===

## Instrucciones:

### Configuración Inicial:
- Crea un proyecto de Django llamado myproject.
- Crea una aplicación llamada blog.

### Modelos:
- Define un modelo Post en la aplicación blog con los siguientes campos:
  - title: CharField (máximo 200 caracteres)
  - content: TextField
  - created_at: DateTimeField (automáticamente establecido al momento de creación)

### Serializadores:
- Crea un serializador para el modelo Post llamado PostSerializer.

### Vistas y Rutas:
- Implementa las vistas para manejar las operaciones CRUD utilizando vistas basadas en clases de DRF.
- Configura las rutas en el archivo urls.py de la aplicación blog para que se puedan realizar las operaciones CRUD a través de la API.

## Recomendaciones:
> - Tomar en cuenta que es una prueba sencilla, lo que buscamos evaluar es lo que se considera production ready.
> - Toma en cuenta que buscamos ver que tecnologias manejas, por lo que te pedimos demostrar tus capacidades en todas las tecnologias que manejas.
