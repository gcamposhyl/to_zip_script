import os
import zipfile

def zip_folder(root_folder, exclusion_file, output_zip):
    # Lista de archivos y carpetas excluidos
    exclusions = []
    
    # Leer el archivo de exclusiones
    with open(exclusion_file, 'r') as file:
        exclusions = file.read().splitlines()
    
    # Crear un archivo ZIP
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Recorrer todas las carpetas y archivos
        for root, dirs, files in os.walk(root_folder):
            # Eliminar las carpetas excluidas de la lista de directorios
            dirs[:] = [d for d in dirs if d not in exclusions]
            
            for file in files:
                if file not in exclusions:
                    # Ruta completa del archivo
                    file_path = os.path.join(root, file)
                    
                    # Ruta relativa dentro del archivo ZIP
                    zip_path = os.path.relpath(file_path, root_folder)
                    
                    # Agregar el archivo al ZIP
                    zipf.write(file_path, zip_path)


