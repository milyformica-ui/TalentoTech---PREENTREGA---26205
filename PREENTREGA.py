listaProductos = []
opcion = 0

while opcion != '5':
    print("\n\tMENÚ5\n1. Agregar producto.\n2. Mostrar productos.\n3. Buscar producto.\n4. Eliminar producto.\n5. Salir.")
    opcion = input("\nIngrese acción: ").strip()

    while opcion not in ('1','2','3','4','5'): 
        opcion = input("Error. Ingrese opción válida: ").strip()

    if opcion == '1':
        nombreProducto = input("Nombre del producto: ").strip().capitalize()
        while nombreProducto == '':
            nombreProducto = input("Error. Ingrese nombre del producto: ").strip().capitalize()

        categoriaProducto = input("Categoría del producto: ").strip().capitalize()
        while categoriaProducto == '':
            categoriaProducto = input("Error. Ingrese categoría del producto: ").strip().capitalize()

        precioProducto = input("Precio del producto: ").strip()
        while not precioProducto.isnumeric():
            precioProducto = input("Error. Ingrese un precio válido: ").strip()
        precioProducto = int(precioProducto)

        listaProductos.append([nombreProducto,categoriaProducto,precioProducto])

    elif opcion == '2':
        if len(listaProductos) == 0:
            print("No hay productos cargados.")
            continue
        print("\n----- LISTA DE PRODUCTOS -----\n")
        for i in range(len(listaProductos)):
            print(f"Producto #{i+1}:")
            print(f"\tNombre: {listaProductos[i][0]}\n\tCategoría: {listaProductos[i][1]}\n\tPrecio: ${listaProductos[i][2]}\n")

    elif opcion == '3':
        if len(listaProductos) == 0:
                    print("No hay productos cargados.")
                    continue
        print("\n----- BÚSQUEDA DE PRODUCTOS -----\n")
        productoBuscar = input("Producto a buscar (nombre): ").strip().capitalize()
        encontrado = False
        for i in range(len(listaProductos)):
            if listaProductos[i][0] == productoBuscar:
                print(f"Producto #{i+1}:")
                print(f"\tNombre: {listaProductos[i][0]}\n\tCategoría: {listaProductos[i][1]}\n\tPrecio: ${listaProductos[i][2]}\n")
                encontrado = True
        if not encontrado:
            print("No se encontraron productos con ese nombre.")

    elif opcion == '4':
        productoEliminar = input("Producto a eliminar (numero en la lista): ").strip()
        while not productoEliminar.isnumeric():
            productoEliminar = input("Error. Ingrese el numero del producto a eliminar: ").strip()
        productoEliminar=int(productoEliminar)
        if(productoEliminar < 1 or productoEliminar > len(listaProductos)):
            print("Este producto no existe.")
        else:
            eliminado = listaProductos.pop(productoEliminar-1)
            print(f"Producto #{productoEliminar}: '{eliminado[0]}' fue eliminado exitosamente.")

print("¡Gracias por usar nuestro servicio! Programa finalizado.")