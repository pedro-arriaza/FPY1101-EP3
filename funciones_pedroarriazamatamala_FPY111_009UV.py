import os

#Registrar libros
#Definir listas y variables globales
libros = []
def registro():
    try:
        titulo = input("Ingrese el titulo del libro: ")
        autor = input("Ingrese el nombre del autor: ")
        año_autor=input   ("Ingrese el año del autor")
        año_publicacion=input("Ingrese el año de publicacion")
        SKU=input("ingrese la SKU")
        SKU = float(input("Ingrese el nombre del libro: "))

        if libros == "" or autor == "" or titulo == "" or SKU == año_autor =="" or año_publicacion:
            print("Faltaron datos por ingresar")
        
            libros = {
                'titulo' : titulo,
                'autor' : autor,
                'año_autor' : año_autor,
                'año_publicacion':año_publicacion
                
            }
            libros.append(libros)
            print("Registro se realizo exitosamente")
    except ValueError:
        print("Dato erroneo. Intente nuevamente")
        #Esta función recoge los datos de los libros, 
        
        
#Listar los todos los libros
def listar():
    print("libros\t\tTitulo\t\tAutor\t\taño_autor\t\tsku\t\taño_publicacion\n")
    for libros in libros:
        print(f"{libros['nombre']}\t\t{libros['titulo']}\t\t{libros['año_autor']}\t\t{libros['año_publicacion']}\t\t{libros['SKU']}\n")
        #Esta función imprime la lista de todos los libros



def imprimir():
    try:
        op = int(input("¿Cómo desea imprimir la reporte de prestamos de los libros ?\n1. Todos\n2.Opción: "))

        if op == 1:
            with open('planilla_prestamo.txt','w') as archivo:
                archivo.write("titulo\t\tautor\t\t\t\taño_autor\t\tsku\t\taño_publicacion\n")

                for libros in libros:
                    archivo.write(f"{libros['titulo']}\t\t{libros['autor']}\t\t{libros['año_autor']}\t\t{libros['sku']}\t\taño_publicacion")

            print("Planilla de prestamo de libros generada exitosamente en: ", os.getcwd())
        elif op == 2:
            cargo = input("ingrese el libro: ").lower()
            if not libros in libros:
                print("libro no existe")
            else:
                with open(f'planilla_{libros}.txt','w') as archivo:
                    archivo.write("libros\t\ttitulo\t\tautor\t\taño_autor\t\tsku\t\taño_publicacion\n")

                    for libros in libros:
                        if libros['libros'].lower() == libros:
                            archivo.write(f"{libros['titulo']}\t\t{libros['autor']}\t\t{libros['año_autor']}\t\t{libros['sku']}\t\t{libros['año_publicacion']}")
                print("Planilla generada exitosamente en: ", os.getcwd())
    except ValueError:
        print("Dato erroneo.libro emprestado Intente nuevamente")
        
        
        #Función del menú principal
def menu():
    while True:
        try:
            print("* * *  REGISTRO  * * *")
            print("1. Registrar libros\n2. Listar libros\n3. Imprimir libros emprestados\n4. Salir")
            op = int(input("Ingrese una opción: "))
        except ValueError:
            print("Dato erroneo. Intente nuevamente")
        if op == 1:
            registro()
        elif op == 2:
            listar()
        elif op == 3:
            imprimir()
        elif op == 4:
            print("Finalizando el programa")
            break
        else:
            print("La opción ingresada esta fuera de rango, por favor intente nuevamente")
            


