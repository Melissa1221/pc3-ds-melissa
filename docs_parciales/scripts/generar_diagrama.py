#!/usr/bin/env python3
"""
scripts/generar_diagrama.py
- Genera docs/diagrama_red.dot a partir de los .tfstate en cada módulo
"""
import os
import json


def get_available_colors():
    """
    Retorna lista de colores disponibles para asignación a módulos.

    """
    return ['blue', 'green', 'orange', 'red', 'purple', 'yellow', 
            'cyan', 'magenta', 'brown', 'pink', 'gray', 'darkgreen']

def assign_module_colors(modulos):
    """
    Asigna colores de manera cíclica a una lista de módulos.
    
    """
    colores_disponibles = get_available_colors()
    mapeo_colores = {}
    
    for index, modulo in enumerate(sorted(modulos)):
        color_index = index % len(colores_disponibles)
        mapeo_colores[modulo] = colores_disponibles[color_index]
    
    return mapeo_colores

def generate_dot():
    """
    Lee terraform.tfstate de cada módulo (iac/<módulo>/terraform.tfstate)
    y extrae dependencies para formar un grafo DOT.
    """
    # TODO: implementar lectura de JSON y generar líneas DOT
    
    root = os.path.join(os.path.dirname(__file__), "../iac")
    # Identificar módulos disponibles
    modulos_disponibles = []
    for item in os.listdir(root):
        modulo_dir = os.path.join(root, item)
        tfstate = os.path.join(modulo_dir, "terraform.tfstate")
        if os.path.isfile(tfstate):
            modulos_disponibles.append(item)
    # Asignar colores
    mapeo_colores = assign_module_colors(modulos_disponibles)
    recurso_a_modulo = {}
    return


def generate_svg_from_dot(dot_file_path, svg_file_path):
    """
    Convierte un archivo DOT a SVG usando el comando dot de Graphviz.
    
    Args:
        dot_file_path (str): Ruta al archivo DOT de entrada
        svg_file_path (str): Ruta al archivo SVG de salida
    
    Returns:
        bool: True si la conversión fue exitosa, False en caso contrario
    """
    try:
        # Verificar que el archivo DOT existe
        if not os.path.isfile(dot_file_path):
            print(f"Error: El archivo DOT {dot_file_path} no existe")
            return False
        
        # Ejecutar comando dot para generar SVG
        cmd = ["dot", "-Tsvg", dot_file_path, "-o", svg_file_path]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        # Verificar que el archivo SVG se creó correctamente
        if os.path.isfile(svg_file_path):
            print(f"Diagrama SVG generado exitosamente en {svg_file_path}")
            return True
        else:
            print(f"Error: No se pudo crear el archivo SVG {svg_file_path}")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"Error ejecutando comando dot: {e}")
        print(f"stderr: {e.stderr}")
        return False
    except FileNotFoundError:
        print("Error: comando 'dot' no encontrado. Asegúrese de que Graphviz esté instalado")
        print("En sistemas Ubuntu/Debian: sudo apt-get install graphviz")
        return False
    except Exception as e:
        print(f"Error inesperado al generar SVG: {e}")
        return False

def main():
    # TODO: invocar generate_dot() y escribir docs/diagrama_red.dot
    pass

if __name__ == "__main__":
    main() 