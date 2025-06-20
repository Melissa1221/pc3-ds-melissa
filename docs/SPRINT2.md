# Sprint 2 - Desarrollo del parseo y automatización

Durante este sprint me tocó encargarme de hacer que el código lea automáticamente los archivos de Terraform y genere la documentación. Después de tener toda la estructura lista del Sprint 1, ahora había que hacer que todo funcione de verdad.

## Issues #5 y 20: Completar las funciones de parsing en terraform_docs.py

Lo primero que hice fue terminar las funciones que habían quedado como esqueletos en el sprint anterior. Había tres funciones principales que necesitaba completar y cada una tenía sus propios retos.

### parse_variables() 

Esta función me costó más trabajo del que esperaba. La idea era sencilla: leer el archivo `variables.tf` y extraer toda la información de cada variable. Pero cuando empecé a trabajar con los archivos reales me di cuenta de que las variables en Terraform pueden tener bloques anidados, validaciones, y toda clase de cosas que complicaban el parsing.

Al principio intenté con regex simples, pero me fallaban cuando había llaves dentro de los bloques de variables. Entonces tuve que implementar un sistema de conteo de llaves para saber dónde terminaba realmente cada bloque variable. Básicamente, cuando encuentro `variable "nombre" {`, empiezo a contar llaves abiertas y cerradas hasta que el contador llegue a cero.

```python
# Encontrar el final del bloque contando llaves
brace_count = 1
end_pos = start_pos

while end_pos < len(content) and brace_count > 0:
    if content[end_pos] == '{':
        brace_count += 1
    elif content[end_pos] == '}':
        brace_count -= 1
    end_pos += 1
```

Una vez que tenía el bloque completo, usé regex más específicos para extraer la descripción, el tipo y el valor por defecto.

### parse_outputs()

Para los outputs usé la misma técnica de conteo de llaves, pero fue más sencillo porque los outputs tienen menos variaciones que las variables. Solo necesitaba extraer el nombre y la descripción. El truco estaba en el mismo sistema de conteo de llaves para manejar bloques anidados.

### parse_resources()

Esta función resultó ser la más simple de todas. Solo necesitaba encontrar patrones como `resource "tipo" "nombre"` en el main.tf. Usé un regex básico y funcionó perfecto:

```python
pattern = r'resource\s+"([^"]+)"\s+"([^"]+)"'
matches = re.findall(pattern, content)
```

Lo que me gusta de esta función es que es súper robusta - si no encuentra el archivo o hay algún error, simplemente retorna una lista vacía sin tronar el programa.
