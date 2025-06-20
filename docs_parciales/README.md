
## 2. Avances desarrollados en Sprint 2:

Durante este segundo sprint hemos completado la funcionalidad principal del sistema de documentación automática, implementando las funciones de parsing y automatización que constituyen el núcleo operativo del proyecto.

### Implementación completa de funciones de parsing en terraform_docs.py

Se completaron las funciones fundamentales que permiten la extracción automática de información desde los archivos Terraform:

**parse_resources(modulo_path)**:
- Analiza archivos `main.tf` utilizando expresiones regulares para identificar declaraciones de recursos
- Extrae patrones `resource "<tipo>" "<nombre>"` y los estructura en diccionarios con claves "type" y "name"
- Implementa manejo robusto de errores, retornando lista vacía cuando no existe el archivo main.tf
- Probado exitosamente en todos los módulos, identificando recursos tipo `null_resource` en cada uno

**parse_variables(modulo_path)**:
- Lee archivos `variables.tf` implementando parsing avanzado con regex y conteo de llaves para manejar bloques anidados
- Extrae información completa de variables: nombre, tipo, valor por defecto y descripción
- Maneja bloques de validación anidados sin interferir con la extracción principal
- Retorna estructura de diccionarios con claves "name", "type", "default", "description"
- Procesamiento exitoso de 18 variables distribuidas entre los 6 módulos

**parse_outputs(modulo_path)**:
- Procesa archivos `outputs.tf` utilizando técnicas similares de parsing con conteo de llaves
- Extrae nombre y descripción de cada output definido
- Estructura los datos en diccionarios con claves "name" y "description"
- Manejo graceful de archivos inexistentes mediante retorno de listas vacías
- Procesamiento exitoso de 18 outputs distribuidos entre los 6 módulos

### Validación de nomenclatura con verificar_nomenclatura.py

Se implementó el sistema de validación de convenciones de nomenclatura:
- Escaneo automático del directorio `iac/` aplicando regex
- Reporte estructurado con mensajes "OK: <módulo>" para nombres válidos
- Identificación de violaciones con "ERROR: <módulo> no cumple convención"
- Terminación con código de error apropiado usando `sys.exit(1)` cuando detecta fallos
- Validación exitosa de los 6 módulos existentes: compute, logging, monitoring, network, security, storage

### Generación automatizada de documentación Markdown

La función `write_markdown()` produce documentación estructurada para cada módulo:
- Encabezados consistentes con formato `# Módulo <nombre>`
- Secciones organizadas: descripción placeholder, tablas de variables, tablas de outputs, lista de recursos
- Integración completa con las funciones de parsing implementadas
- Generación de 6 archivos de documentación correspondientes a cada módulo
- Formato de tablas Markdown estándar con encabezados apropiados

### Automatización completa con update_docs.sh

Script de automatización que ejecuta el flujo completo:
- Iteración sobre cada módulo en `iac/` ejecutando `terraform init` y `terraform apply -auto-approve`
- Manejo de errores con terminación apropiada en caso de fallos de Terraform
- Ejecución secuencial de `terraform_docs.py` y `generar_diagrama.py`
- Retorno al directorio raíz para mantener consistencia de rutas
- Preparación del entorno para la generación automatizada de documentación

### Implementación de create_index() para generación automática del índice

Desarrollo de la función `create_index()` que automatiza la creación del archivo índice principal:
- Utiliza plantilla `template_index.md` para estructura consistente
- Escaneo automático del directorio `iac/` para detectar módulos disponibles
- Generación dinámica de enlaces Markdown a cada archivo de documentación
- Integración con el flujo de trabajo de automatización
- Creación de `docs/index.md` con navegación centralizada y referencia al diagrama de red

### Punto de entrada unificado con docs/index.md

El archivo índice generado automáticamente proporciona:
- Encabezado estándar "Documentación de Módulos IaC"
- Enlaces dinámicos a cada archivo de documentación individual
- Referencia al diagrama de red (diagrama_red.svg)
- Estructura de navegación centralizada para acceso directo a cualquier módulo




## 4. Instrucciones básicas de reproducibilidad:

Aunque no haya aún una funcionalidad establecida, es posible acceder a este proyecto mediante los siguientes pasos:
```bash
# 1. Clonar el repositorio
git clone https://github.com/bxcowo/PracticaCalificada3_Grupo5.git
cd PracticaCalificada3_Grupo5

# 2. Verificar nomenclatura de módulos (opcional)
python3 scripts/verificar_nomenclatura.py