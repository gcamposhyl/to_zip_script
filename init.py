import main
import deploy
import re

if __name__ == "__main__":

    print('''
        -----------------------Script deploy proyectos python------------------------------
    ''')

    input_option = input('''
Opciones:
                         
    - Desplegar archivo en Python Anywhere -> Digite 1
                         
    - Comprimir archivo o carpeta a .zip en local -> Digite 2
                         
''')
    print('''
        -----------------------------------------------------------------------------
        ''')

    if input_option == "1":

        print(r"Ejemplo -> escritura path en local: c:\..\archivo.txt")
        print("")
        file_to_upload = input("Ingresa la ruta del archivo a subir: ")
        name_file = re.search(r'\\([^\\]+)$', file_to_upload).group(1)
        print('''
        -----------------------------------------------------------------------------
        ''')
        print(r"Ejemplo -> escritura path en nube (escribir directorio al que se desea subir): carpeta/subcarpeta")
        print("")
        file_on_cloud = "/home/gcamposhyl/" + input("Ingresa ubicación deseada para archivo: ") + "/" + name_file
        print('''
        -----------------------------------------------------------------------------
        ''')
        deploy.deploy_to_pa(file_to_upload, file_on_cloud)

    elif input_option == "2":

        print(r"Ejemplo -> escritura path en local: c:\..")
        print("")
        root_folder = input("Ingresa la ruta de la carpeta a comprimir: ")
        print('''
        -----------------------------------------------------------------------------
        ''')
        exclusion_file = input("Ingresa la ruta del archivo .txt para exclusiones: ")
        print('''
        -----------------------------------------------------------------------------
        ''')
        print(r"Ejemplo -> escritura path en local: c:\..")
        print("")
        output_zip = input("Ingresa la ruta de la carpeta destino para archivo .zip: ")
        print('''
        -----------------------------------------------------------------------------
        ''')
        zip_name = input("Ingresa el nombre del archivo: ") + ".zip"
        print('''
        -----------------------------------------------------------------------------
        ''')
        
        #root_folder = r"c:\Users\dev-h\OneDrive\Escritorio\proyectos_python\test_input"
        #exclusion_file = r"c:\Users\dev-h\OneDrive\Escritorio\proyectos_python\test_input\exclusiones.txt"
        #output_zip = r"c:\Users\dev-h\OneDrive\Escritorio\proyectos_python\test_output"
        #zip_name = r"nuevo"

        main.zip_folder(root_folder, exclusion_file, output_zip, zip_name)
    
    