prendas = {
'S001': ['Polera Basica', 'polera', 'M', 'negro', 'algodon', True],
'S002': ['Jeans Slim', 'pantalon', 'L', 'azul', 'denim', False],
'S003': ['Chaqueta Urban', 'chaqueta', 'M', 'gris', 'poliester', True],
'S004': ['Vestido Sol', 'vestido', 'S', 'rojo', 'lino', False],
'S005': ['Poleron Cozy', 'poleron', 'XL', 'verde', 'algodon', True],
'S006': ['Camisa Formal', 'camisa', 'M', 'blanco', 'algodon', False],}

bodega = {
'S001': [7990, 12],
'S002': [19990, 0],
'S003': [29990, 3],
'S004': [24990, 6],
'S005': [17990, 8],
'S006': [14990, 2],
}


def busqueda_de_precio(p_min,p_max):
    contador=1
    contador_total_prendas=0
    for codigo, datos in bodega.items():
        if p_min<=datos[0]<=p_max:
            print(f"{contador}. Nombre: {prendas[codigo][0]} | Precio: {bodega[codigo][0]}")
            contador+=1
            contador_total_prendas+=1
    if contador_total_prendas==0:
        print("No hay prendas en ese rango de precios.")
def leer_opcion():
        try:
            valor=int(input("Ingrese opcion: "))
            if valor<1 or valor>6:
                return 0
            return valor
        except ValueError:
            return 0
def unidades_categoria(categoria):
    acumulador_categoria=0
    for codigo,datos in prendas.items():
        if categoria.lower() == prendas[codigo][1].lower():
            acumulador_categoria+=bodega[codigo][1]
    print(f"El total de unidades disponibles es:{acumulador_categoria}")
def buscar_codigo(codigo):
    return codigo.upper() != "" and codigo.upper() in prendas
def actualizar_precio(nuevo_precio,codigo):
    bodega[codigo][0]=nuevo_precio
def eliminar_prenda(codigo):
    buscar_codigo(codigo)
    del prendas[codigo]
    del bodega[codigo]
    print("Prenda eliminada")


def validacion_codigo(codigo):
    if len(codigo) !=0 and codigo not in prendas:
        return codigo
def validacion_nombre(nombre):
    if len(nombre) !=0:
        return nombre
def validacion_categoria(categoria):
    if len(categoria) !=0:
        return categoria
def validacion_talla(talla):
    if len(talla) !=0:
        return talla
def validacion_color(color):
    if len(color) !=0:
        return color
def validacion_material(material):
    if len(material)!=0:
        return material
def validacion_unisex(es_unisex):
    if len(es_unisex) !=0 and es_unisex in ("s","n"):
        return es_unisex
def validacion_precio(precio):
    try:
        precio=int(precio)
        if precio<0:
            return False
        return precio
    except ValueError:
        return False
def validacion_unidades(unidades):
    try:
        unidades=int(unidades)
        if unidades<0:
            return False
        return unidades
    except ValueError:
        return False


def agregar_prenda(codigo,nombre,categoria,talla,color,material,es_unisex,precio,unidades):
    if es_unisex=="s":
        es_unisex=True
        prendas[codigo]
    else:
        es_unisex=False
        prendas[codigo][nombre,categoria,talla,color,material,es_unisex]
        bodega[codigo][precio,unidades]
def main():
    while True:
        print('''========== MENÚ PRINCIPAL ==========
                1. Unidades por categoría
                2. Búsqueda de prendas por rango de precio
                3. Actualizar precio de prenda
                4. Agregar prenda
                5. Eliminar prenda
                6. Salir
                =====================================''')
        op_menu=leer_opcion()
        if op_menu==0:
            print("Debe seleccionar una opción válida")
        elif op_menu==1:
            categoria=input("Ingrese la categoria a consultar: ")
            unidades_categoria(categoria)
        elif op_menu==2:
            while True:
                try:
                    p_min=int(input("Ingrese precio minimo: "))
                    p_max=int(input("Ingrese precio maximo: "))
                    if p_min<0 or p_max<0:
                        print("Debe ingresar valores enteros")
                    elif p_min>p_max:
                        print("El precio minimo debe ser menor o igual al precio maximo")
                    else:
                        busqueda_de_precio(p_min,p_max)
                        break
                except ValueError:
                    print("Debe ingresar valores enteros")
        elif op_menu==3:
            while True:
                codigo=input("Ingrese codigo de la prenda: ").upper()
                if buscar_codigo(codigo):
                    print(f"Nombre: {prendas[codigo][0]} | Precio actual: {bodega[codigo][0]}")
                    try:
                        nuevo_precio=int(input("Ingrese nuevo precio: "))
                        actualizar_precio(nuevo_precio,codigo)
                        print("Precio actualizado")
                    except ValueError:
                        print("Error al actualizar precio")
                else:
                    print("El codigo no existe")
                pregunta=input("Desea actualizar otro precio (s/n)?: ")
                if pregunta=="n":
                    break
        elif op_menu==4:
            codigo=input("Ingrese un codigo: ").upper()
            if not validacion_codigo(codigo):
                print("Codigo ya existente o esta en blanco")
                continue
            nombre=input("Ingrese un nombre: ")
            if not validacion_nombre(nombre):
                print("No puede quedar en blanco el nombre")
                continue
            categoria=input("Ingrese una categoria: ")
            if not validacion_categoria(categoria):
                print("No puede quedar en blanco la categoria")
                continue
            talla=input("Ingrese una talla: ")
            if not validacion_talla(talla):
                print("No puede quedar en blanco la talla")
                continue
            color=input("Ingrese un color: ")
            if not validacion_color(color):
                print("No puede quedar en blanco el color")
                continue
            material=input("Ingrese el material: ")
            if not validacion_material(material):
                print("No puede quedar en blanco el material")
                continue
            es_unisex=input("La prenda es unisex (s/n)?: ").lower()
            if not validacion_unisex(es_unisex):
                print("Ingrese s o n para esta opcion")
                continue
            precio=input("Ingrese el precio: ")
            if not validacion_precio(precio):
                print("Ingrese un numero mayor que 0")
                continue
            unidades=input("Ingrese las unidades: ")
            if not validacion_unidades(unidades):
                print("Ingrese un numero positivo")
                continue
            agregar_prenda(codigo,nombre,categoria,talla,color,material,es_unisex,precio,unidades)
            print(prendas)

        elif op_menu==5:
            codigo=input("Ingrese un codigo: ").upper()
            if buscar_codigo(codigo):
                eliminar_prenda(codigo)
            else:
                print("El codigo no existe")
        elif op_menu==6:
            print("Programa finalizado.")
            break
main()


































