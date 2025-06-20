
# Sprint 3 - Visualización y diagramas automáticos

Para este sprint me tocó trabajar en la parte visual del proyecto, que era hacer que los diagramas no solo se generaran automáticamente, sino que se vieran bien y fueran fáciles de entender. Aquí es donde entra Graphviz y todo el tema de convertir datos de Terraform en algo visual.

## Issue #21: Agregar colores y estilo al diagrama

Lo primero que necesitaba resolver era cómo hacer que el diagrama fuera más legible. Un diagrama donde todos los nodos se ven iguales no dice mucho, así que necesitaba un sistema de colores que ayudara a distinguir los diferentes tipos de módulos.

### Sistema de asignación de colores

Implementé dos funciones para manejar esto de manera ordenada:

```python
def get_available_colors():
    return ['blue', 'green', 'orange', 'red', 'purple', 'yellow', 
            'cyan', 'magenta', 'brown', 'pink', 'gray', 'darkgreen']

def assign_module_colors(modulos):
    colores_disponibles = get_available_colors()
    mapeo_colores = {}
    
    for index, modulo in enumerate(sorted(modulos)):
        color_index = index % len(colores_disponibles)
        mapeo_colores[modulo] = colores_disponibles[color_index]
    
    return mapeo_colores
```

Lo que me gustó de esta solución es que es escalable. Si mañana agregamos más módulos, el sistema automáticamente les asigna colores de manera cíclica. También ordeno los módulos alfabéticamente antes de asignar colores, para que siempre queden consistentes.

El resultado es que cada tipo de módulo tiene su color distintivo:
- Network en rojo
- Compute en azul  
- Storage en amarillo
- Security en púrpura
- Y así sucesivamente...


## Issue #22: Conversión a SVG con Graphviz

El segundo fue hacer que el archivo DOT se convirtiera automáticamente en SVG. Esto requería integrar Graphviz en el flujo de trabajo y manejar todos los posibles errores que pudieran ocurrir.

### Implementación de generate_svg_from_dot()

Esta función fue interesante porque tuve que manejar muchos casos edge:

```python
def generate_svg_from_dot(dot_file_path, svg_file_path):
    try:
        # Verificar que el archivo DOT existe
        if not os.path.isfile(dot_file_path):
            print(f"Error: El archivo DOT {dot_file_path} no existe")
            return False
        
        # Ejecutar comando dot para generar SVG
        cmd = ["dot", "-Tsvg", dot_file_path, "-o", svg_file_path]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
```

Se debe manejar todos los errores posibles

1. **Archivo DOT inexistente**: Verifico que existe antes de intentar procesarlo
2. **Graphviz no instalado**: Capturo `FileNotFoundError` y doy instrucciones específicas de instalación
3. **Errores de sintaxis en DOT**: Capturo `CalledProcessError` y muestro el stderr para debugging
4. **Archivo SVG no generado**: Verifico que el archivo de salida realmente se creó


El SVG resultante muestra claramente:
- Cada módulo con su color distintivo
- Las dependencias marcadas con "depends_on"
- Una estructura jerárquica que hace sentido visualmente

## Integración con el flujo completo

Ahora el flujo completo es:

1. Los scripts de parsing extraen la información de Terraform
2. `generate_dot()` crea el archivo DOT con colores y etiquetas
3. `generate_svg_from_dot()` convierte automáticamente a SVG
4. El resultado se puede abrir directamente en cualquier navegador
