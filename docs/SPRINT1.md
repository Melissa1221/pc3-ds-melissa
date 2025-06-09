# Sprint 1 - Documentación del desarrollo individual

Al inicio del proyecto, nuestro equipo dividió el trabajo en tareas más pequeñas y manejables, las cuales organizamos utilizando el sistema de Kanban a través de GitHub Issues. El flujo de trabajo establecido incluye las siguientes etapas:

- **Ready**: Tareas listas para ser asignadas al sprint actual
- **In Progress**: Tareas en desarrollo activo
- **Review**: Tareas pendientes de revisión y validación
- **Done**: Tareas completadas y aprobadas

## Issue #1: Estructura Inicial del Proyecto

Me encargué de la creación de la estructura inicial del proyecto, estableciendo las bases para el desarrollo de la infraestructura como código.

La estructura del proyecto se organizó de la siguiente manera:

```
├─ iac/
│   ├─ compute/
│   │   ├─ main.tf
│   │   ├─ variables.tf
│   │   └─ outputs.tf
│   ├─ logging/
│   │   ├─ main.tf
│   │   ├─ variables.tf
│   │   └─ outputs.tf
│   ├─ monitoring/
│   │   ├─ main.tf
│   │   ├─ variables.tf
│   │   └─ outputs.tf
│   ├─ network/
│   │   ├─ main.tf
│   │   ├─ variables.tf
│   │   └─ outputs.tf
│   ├─ security/
│   │   ├─ main.tf
│   │   ├─ variables.tf
│   │   └─ outputs.tf
│   └─ storage/
│       ├─ main.tf
│       ├─ variables.tf
│       └─ outputs.tf
├─ scripts/
│   ├─ generar_diagrama.py
│   ├─ terraform_docs.py
│   ├─ update_docs.sh
│   └─ verificar_nomenclatura.py
├─ docs/
├─ README.md
├─ LICENSE
└─ .gitignore
```

La arquitectura decicida cumple con el principio de responsabilidad única el cual se especifica para cada módulo

- **compute/**: Gestión de recursos de cómputo
- **network/**: Configuración de redes 
- **security/**: Políticas de seguridad 
- **storage/**: Recursos de almacenamiento 
- **logging/**: Configuración de logs y auditoría
- **monitoring/**: Métricas y alertas del sistema

Cada módulo sigue la estructura estándar recomendada:

- **main.tf**: Contiene la lógica principal y definición de recursos
- **variables.tf**: Define las variables de entrada del módulo con tipos, descripciones y validaciones
- **outputs.tf**: Especifica los valores de salida que otros módulos pueden consumir

Para la automatización en la carpeta script se encuentran:

- **generar_diagrama.py**: Generación automática de diagramas de terraform state
- **terraform_docs.py**: Parsing y generación de documentación automática de módulos de Terraform
- **update_docs.sh**: Script para actualizar toda la documentación del proyecto
- **verificar_nomenclatura.py**: Validación de convenciones de nomenclatura

La carpeta `docs/` centraliza toda la documentación técnica, incluyendo la documentación generada y los diagramas del estado de terraform.

Los beneficios de esta estructura son principalmente la modularidad al facilitar el mantenimiento y reutilización del código, además de ser escalable ya que se pueden agregar neuvos módulos sin afectar a los existentes.

## Desarrollo de Scripts de Automatización

Como parte de el siguiente issue, también creé la estructura básica de los scripts de python que nos van a ayudar con la automatización del proyecto. Por ahora solo implementé los métodos básicos y la estructura, pero quiero explicar qué van a hacer estos scripts cuando se termine de desarrollar.

### generar_diagrama.py

Este script va a automatizar algo que normalmente haríamos a mano. La idea es que lea los archivos `terraform.tfstate` que se generan en cada módulo cuando corremos terraform, y a partir de esa información cree un diagrama visual de nuestra infraestructura.

Lo que va a hacer es revisar cada módulo (compute, network, security, etc.) y extraer las dependencias entre los recursos. Por ejemplo, si un security group depende de una VPC, o si una instancia EC2 usa cierto security group. Con toda esa información va a generar un archivo `.dot` (que es el formato que usa Graphviz) y al final vamos a tener un diagrama que muestre cómo están conectados todos nuestros recursos.

Por ahora solo tengo la estructura básica con los métodos `generate_dot()` y `main()`, pero la idea es que este script nos ahorre mucho tiempo manual creando diagramas cada vez que cambiemos la infraestructura.

### terraform_docs.py

Este otro script va a ser súper útil para mantener la documentación siempre actualizada. La idea es que recorra automáticamente cada módulo de terraform y genere documentación en Markdown de manera consistente.

Lo que va a hacer es leer los tres archivos principales de cada módulo: `variables.tf`, `outputs.tf` y `main.tf`. Del archivo de variables va a extraer qué parámetros acepta cada módulo, qué tipo de datos son, si tienen valores por defecto, y sus descripciones. De outputs va a sacar qué valores devuelve el módulo. Y de main.tf va a listar todos los recursos que crea.

Con toda esa información va a generar archivos Markdown organizados en la carpeta docs, uno por cada módulo. Así siempre vamos a tener documentación actualizada sin tener que escribirla manualmente cada vez que hagamos cambios.

Estos scripts van a hacer que el proyecto sea mucho más mantenible a largo plazo, porque la documentación y los diagramas se van a actualizar solos. Por ahora implementé solo la estructura básica con comentarios TODO donde va a ir la lógica principal, así que es un buen punto de partida para los siguientes sprints.
