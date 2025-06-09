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

