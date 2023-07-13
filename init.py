import main
import deploy

if __name__ == "__main__":
    input_option = input('''
Desplegar archivo en Python Anywhere => Digite 1
Comprimir archivo en local => Digite 2
                         
''')

    if input_option == "1":
        file_to_upload = input("Ingresa la ruta del archivo a subir: ")
        deploy.deploy_to_pa(file_to_upload)
    elif input_option == "2":
        root_folder = input("Ingresa la ruta de la carpeta a comprimir: ")
        exclusion_file = input("Ingresa la ruta del archivo .txt para exclusiones: ")
        output_zip = input("Ingresa la ruta de la carpeta destino para archivo .zip: ")
        zip_name = input("Ingresa el nombre del archivo: ") + ".zip"
        
        #root_folder = r"C:\Users\DevHyL\Desktop\proyectos_python\test_input"
        #exclusion_file = r"C:\Users\DevHyL\Desktop\proyectos_python\test_input\exclusiones.txt"
        #output_zip = r"C:\Users\DevHyL\Desktop\proyectos_python\test_output"
        #zip_name = r"nuevo"

        main.zip_folder(root_folder, exclusion_file, output_zip, zip_name)
    
    