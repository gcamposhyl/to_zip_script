import os
import zipfile

def zip_folder(root_folder, exclusion_file, output_zip, zip_name):
    try:
        # Construyo ruta completa al zip
        output_zip = output_zip + f"\{zip_name}"

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
                #dirs[:] = [d for d in dirs if os.path.join(root, d) not in exclusions]
                dirs[:] = [d for d in dirs if d not in exclusions]
                                
                for file in files:
                    file_path = os.path.join(root, file)
                    
                    # Ruta relativa dentro del archivo ZIP
                    zip_path = os.path.relpath(file_path, root_folder)
                    
                    # Verificar si el archivo completo (incluyendo la ruta) está excluido
                    excluded = False
                    for exclusion in exclusions:
                        if (file_path.endswith(exclusion) or os.path.join(root, exclusion) == file_path) and exclusion.startswith("\\"):
                            excluded = True
                            break
                    
                    if not excluded:
                        # Agregar el archivo al ZIP
                        zipf.write(file_path, zip_path)
    except Exception as e:
        print(f'Error: {str(e)}')     

                        
