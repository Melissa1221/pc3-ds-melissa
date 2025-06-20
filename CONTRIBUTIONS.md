## Sprint 1

- 2025-06-05: Creé la estructura inicial del proyecto con directorios `iac/`, `scripts/`, `docs/` y archivos base para los 6 módulos Terraform.  
  Commit: `feat(structure): create initial folder structure and empty files`  
  Hash: `44ed9c7`  
  Parche: `feature-melissa-estructura-inicial.patch`

- 2025-06-08: Implementé el esqueleto inicial de `scripts/terraform_docs.py` con funciones vacías para parsing y generación de Markdown.  
  Commit: `feat(scripts): add skeleton for terraform docs with parse and write markdown stubs`  
  Hash: `a05afab`  
  Parche: `feature-melissa-scripts-iniciales.patch`

- 2025-06-08: Agregué el esqueleto de `scripts/generar_diagrama.py` con función `generate_dot()` y estructura principal.  
  Commit: `feat(scripts): add skeleton for generate diagram with generate dot and main stubs`  
  Hash: `1ca4fdc`  
  Parche: `feature-melissa-scripts-iniciales.patch`

- 2025-06-09: Documenté los avances del Sprint 1 en README.md y agregué enlace al video explicativo.  
  Commit: `docs(readme): add video sprint 1`  
  Hash: `0d7a82b`  
  Issue relacionado: #1 (Estructura inicial del proyecto)

## Sprint 2

- 2025-06-10: Implementé la función `parse_resources()` en `terraform_docs.py` para extraer recursos de archivos `main.tf` usando regex.  
  Commit: `feat(py): implement parse_resources() to extract resources of main.tf`  
  Hash: `52a68f6`  
  Parche: `feature-melissa-parse-resources.patch`  
  Issue relacionado: #20 (Completar funciones de parsing)

- 2025-06-13: Completé las funciones `parse_variables()` y `parse_outputs()` con sistema de conteo de llaves para manejar bloques anidados.  
  Commit: `feat(py): implement parse_variables and parse_outputs in terraform_docs script`  
  Hash: `4a8133d`  
  Parche: `feature-melissa-parse-variables-outputs.patch`  
  Issue relacionado: #5 (Implementar parsing de variables y outputs)

- 2025-06-13: Actualicé la documentación del README.md con los logros y avances técnicos del Sprint 2.  
  Commit: `docs(readme): update sprint 2 achievements`  
  Hash: `c616927`  
  Parche: `feature-melissa-actualizar-readme.patch`

- 2025-06-14: Agregué documentación detallada de la función `create_index()` e instrucciones de uso del proyecto.  
  Commit: `update(readme): add create_index() description and instructions to run the project`  
  Hash: `accaaaf`  
  Parche: `feature-melissa-actualizar-readme.patch`

## Sprint 3

- 2025-06-17: Implementé sistema de colores por módulo y etiquetas "depends_on" en el generador de diagramas DOT.  
  Commit: `feat(diagram): add module colors and dependency labels to DOT generation`  
  Hash: `4102b68`  
  Parche: `feature-melissa-colores-diagrama.patch`  
  Issue relacionado: #21 (Agregar estilo y etiquetas a diagrama_red.dot)

- 2025-06-17: Refactoricé el sistema de asignación de colores para ser escalable y usar asignación cíclica automática.  
  Commit: `refactor(diagram): implement cyclic color assignment for module scalability`  
  Hash: `83e8f0d`  
  Parche: `feature-melissa-colores-diagrama.patch`  
  Issue relacionado: #21

- 2025-06-18: Desarrollé la función `generate_svg_from_dot()` para conversión automática de DOT a SVG usando Graphviz.  
  Commit: `feat(py): add auto generation of SVG in generar_diagrama.py`  
  Hash: `c591143`  
  Parche: `feature-melissa-generar-svg.patch`  
  Issue relacionado: #22 (Generar diagrama_red.svg usando Graphviz)

- 2025-06-18: Agregué el archivo `diagrama_red.svg` generado automáticamente al repositorio de documentación.  
  Commit: `docs(svg): add diagrama_red.svg that was generated`  
  Hash: `dec71ef`  
  Parche: `feature-melissa-generar-svg.patch`  
  Issue relacionado: #22

