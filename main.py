from persona import Persona
from producto import Producto
from factura import Factura
from factura_detalle import FacturaDetalle
from factura_final import Facturafinal
from fecha import Fechas
from montos import Montos
from generarpdf import Generarpdf
import csv
import os
import shutil
from datetime import datetime

personas: Persona = []
productos: Producto = []
factutas: Factura = []
facturasf: Facturafinal = []
fechas: Fechas = []
monto: Montos = []
lista: list = [["DNI", "NOMBRES", "APELLIDOS", "DIRECCION", "TELEFONO"]]
listap: list = [["CODIGO", "NOMBRE", "PRECIO", "MARCA"]]
listaf: list = [["SERIE", "NUMERO", "DNI DEL CLIENTE",
                 "NOMBRE DEL CLIENTE", "BASE IMPONIBLE", "IGV", "TOTAL"]]
listafd:list=[["CODIGO","NOMBRE","CANTIDAD","PRECIO"]]
listafecha:list=[["FACTURA","DIA","MES","AÑO","HORA","FECHA"]]
facturastt = open("facturas.txt", "w")
clientes = open("clientes.txt", "w")
productot = open("productos.txt", "w")
facturasdt = open("facturadetalle.txt", "w")
fechastt=open("fechas.txt","w")

# Gestión de archivos
def iniciarsesion():
    user_="espacial1"
    pwd_="1234"
    print("Inicio de sesión")
    user=(str(input("Ingrese Usuario: ")))
    pwd=(str(input("Ingrese contraseña: ")))
    while user!=user_ and pwd!=pwd_:
        print("Usuario o contraseña inválido")
        user=(str(input("Ingrese Usuario: ")))
        pwd=(str(input("Ingrese contraseña: ")))
    print("Bienvenido(a)")

def generadorfactura(numero,cliente):
    facturaresultante=open("facturaresultante.txt","w")

    for factura in factutas:
        base_imponible=0.0
        igv=0.0
        total=0.0
        if factura.numero == numero:
            facturaresultante.write("---------------------------              -------------------\n")
            facturaresultante.write("                                         |R.U.C: 20448844456\n")
            facturaresultante.write("| LA TIENDITA DE DON PEPE |              |      FACTURA     \n")
            facturaresultante.write("| Ubicados en: Piura 156  |              |    ELECTRONICA   \n")
            facturaresultante.write(f"                                         F00{numero}\n")
            facturaresultante.write("---------------------------              --------------------\n")
            facturaresultante.write("\n")
            facturaresultante.write("DATOS DEL CLIENTE:\n")
            facturaresultante.write(f"DNI: {cliente.dni}\n")
            facturaresultante.write(f"{cliente.apellidos}, {cliente.nombres}\n")
            facturaresultante.write(f"{cliente.direccion}\n")
            facturaresultante.write("\n")
            facturaresultante.write("| CÓDIGO | CANTIDAD | DESCRIPCIÓN | PRECIO UNITARIO | TOTAL |\n")
            facturaresultante.write("-------------------------------------------------------------\n")
            for detalle in factura.detalle:
                facturaresultante.write("| {} | {} | {} - {} | {} | {} |\n".format(detalle.codigo, detalle.cantidad, detalle.nombre, detalle.marca, detalle.precio, detalle.base_imponible))
                base_imponible=base_imponible+detalle.base_imponible
                igv=igv+detalle.igv
                total=total+detalle.total
            facturaresultante.write(f"                                     Subtotal: {base_imponible}\n")
            facturaresultante.write(f"                                     IGV: {igv}\n")
            facturaresultante.write(f"                                     Total: {total}\n")
            for montonum in monto:
                if montonum.numero == numero:
                    facturaresultante.write(f"                                     Monto a pagar: {montonum.monto}\n")
                    facturaresultante.write(f"                                     Vuelto: {montonum.monto-total}\n")
            #montoapagar=float(input("Monto a pagar: "))
            #montonum: Montos=Montos(len(factutas),montoapagar)
            #monto.append(montonum)
    for fecha in fechas:
        if fecha.numero == numero:
            facturaresultante.write(f"Fecha: {fecha.dia}-{fecha.mes}-{fecha.año}  {fecha.hora}:{fecha.minuto}\n")
    facturaresultante.close()

def guardardatos():
    clientes.write(format(lista))
    with open('clientes.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL, delimiter=';')
        writer.writerows(lista)
    productot.write(format(listap))
    with open('productos.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL, delimiter=';')
        writer.writerows(listap)
    facturastt.write(format(listaf))
    with open('facturas.csv', 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL, delimiter=";")
        writer.writerows(listaf)
    facturasdt.write(format(listafd))
    with open('facturadetalle.csv','w',newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL, delimiter=";")
        writer.writerows(listafd)
    fechastt.write(format(listafecha))
    with open('fechas.csv','w',newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL, delimiter=";")
        writer.writerows(listafecha)



def cargardatospersona():
    x = input("¿Quieres cargar los datos de los clientes? (SI/si para cargar) ")
    if x == "SI" or x == "si":
        separador = ";"
        with open("clientes.csv", encoding="utf-8") as archivo:
            next(archivo)
            listac = []
            for linea in archivo:
                linea = linea.rstrip("\n")
                columnas = linea.split(separador)
                dni: str = columnas[0]
                dni = dni.strip('\"')
                nombres: str = columnas[1]
                nombres = nombres.strip('\"')
                apellidos: str = columnas[2]
                apellidos = apellidos.strip('\"')
                direccion: str = columnas[3]
                direccion = direccion.strip('\"')
                telefono: str = columnas[4]
                telefono = telefono.strip('\"')
                listac.append([
                    dni, nombres, apellidos, direccion, telefono
                ])
                lista.append([
                    dni, nombres, apellidos, direccion, telefono
                ])
                persona: Persona = Persona(
                    dni, nombres, apellidos, direccion, telefono)
                personas.append(persona)
            return listac


def cargardatosproducto():
    x = input("¿Quieres cargar los datos de los productos? (SI/si para cargar) ")
    if x == "SI" or x == "si":
        separador = ";"
        with open("productos.csv", encoding="utf-8") as archivo:
            next(archivo)
            listac = []
            for linea in archivo:
                linea = linea.rstrip("\n")
                columnas = linea.split(separador)
                codigo: str = columnas[0]
                codigo = codigo.strip('\"')
                nombre: str = columnas[1]
                nombre = nombre.strip('\"')
                precio: float = columnas[2]
                precio = precio.strip('\"')               
                precio = float(precio)
                marca: str = columnas[3]
                marca = marca.strip('\"')
                listac.append([
                    codigo, nombre, precio, marca
                ])
                listap.append([
                    codigo, nombre, precio, marca
                ])
                producto: Producto = Producto(codigo, nombre, precio, marca)
                productos.append(producto)
            return listac


def cargardatosfactura():
    """[["SERIE","NUMERO","DNI DEL CLIENTE","NOMBRE DEL CLIENTE","BASE IMPONIBLE","IGV","TOTAL"]]"""
    x = input("¿Quieres cargar los datos de las facturas? (SI para cargar) ")
    if x == "SI":
        separador = ";"
        with open("facturas.csv", encoding="utf-8") as archivo:
            next(archivo)
            listac = []
            cargardatosfacturadetalle()
            for linea in archivo:
                    linea = linea.rstrip("\n")
                    columnas = linea.split(separador)
                    serie: str = columnas[0]
                    serie=serie.strip('\"')
                    numero: str = columnas[1]
                    numero = numero.strip('\"')
                    dni: str = columnas[2]
                    dni = dni.strip('\"')
                    nombre: str = columnas[3]
                    nombre = nombre.strip('\"')
                    base_imponible: float = columnas[4]
                    base_imponible = base_imponible.strip('\"')
                    base_imponible = float(base_imponible)
                    igv: float = columnas[5]
                    igv = igv.strip('\"')
                    igv=float(igv)
                    total: float = columnas[6]
                    total = total.strip('\"')
                    total = float(total)
                    listac.append([
                        serie, numero, dni, nombre, base_imponible, igv, total
                    ])
                    listaf.append([
                        serie, numero, dni, nombre, base_imponible, igv, total])
                        
                    factura: Factura = Factura(numero, dni, nombre)
                    factutas.append(factura)
            return listac

def cargardatosfacturadetalle():
    """| CÓDIGO | CANTIDAD | DESCRIPCIÓN | PRECIO UNITARIO | TOTAL |"""
    separador = ";"
    with open("facturas.csv", encoding="utf-8") as archivo:
            next(archivo)
            listac = []
            for linea in archivo:
                    linea = linea.rstrip("\n")
                    columnas = linea.split(separador)
                    codigo: str = columnas[0]
                    nombre: float =columnas[1]
                    cantidad: str=columnas[2]
                    precio: float =columnas[3]
                    listac.append([codigo,nombre,cantidad,precio])
                    listafd.append([codigo, nombre, cantidad, precio])
                    facturadetalle: FacturaDetalle = FacturaDetalle(
                        codigo, nombre, cantidad, precio)
            return facturadetalle
def persona():
    dni: str = str(input("Ingrese DNI: "))
    nombres: str = str(input("Ingrese Nombres: "))
    apellidos: str = str(input("Ingrese Apellidos: "))
    direccion: str = str(input("Ingrese Direccion: "))
    telefono: str = str(input("Ingrese Telefono: "))
    persona: Persona = Persona(dni, nombres, apellidos, direccion, telefono)
    personas.append(persona)
    lista.append([dni, nombres, apellidos, direccion, telefono])


def listar_personas():
    print("| DNI | NOMBRES | APELLIDOS | DIRECCION | TELEFONO |")
    for persona in personas:
        Persona.convertir_a_string(persona)


def buscar_persona():
    dni: str = str(input("Ingrese DNI para buscar persona: "))
    for persona in personas:
        if persona.dni == dni:
            print("| DNI | NOMBRES | APELLIDOS | DIRECCION | TELEFONO |")
            Persona.convertir_a_string(persona)
            return persona


def editar_persona():
    dni: str = str(input("Ingrese DNI para buscar persona: "))
    for persona in personas:
        if persona.dni == dni:
            Persona.convertir_a_string(persona)
            persona.nombres = str(input("Ingrese nuevo nombre: "))
            Persona.convertir_a_string(persona)


def eliminar_persona():
    dni: str = str(input("Ingrese DNI para buscar persona: "))
    for indice, persona in enumerate(personas):
        if persona.dni == dni:
            personas.pop(indice)
            lista.pop(indice+1)


def producto():
    codigo: str = str(input("Ingrese código del producto: "))
    nombre: str = str(input("Ingrese nombre del producto: "))
    precio: float = float(input("Ingrese precio del producto: "))
    marca: str = str(input("Ingrese marca del producto: "))
    producto: Producto = Producto(codigo, nombre, precio, marca)
    productos.append(producto)
    listap.append([codigo, nombre, "{:.2f}".format(precio), marca])


def listar_producto():
    print("| CODIGO | NOMBRE | PRECIO | MARCA |")
    for producto in productos:
        Producto.convertir_a_string(producto)


def buscar_producto():
    codigo: str = str(input("Ingrese Código para buscar el producto: "))
    for producto in productos:
        if producto.codigo == codigo:
            print("| CODIGO | NOMBRE | PRECIO | MARCA |")
            Producto.convertir_a_string(producto)
            return producto


def editar_producto():
    codigo: str = str(input("Ingrese código para cambiar: "))
    for producto in productos:
        if producto.codigo == codigo:
            Producto.convertir_a_string(producto)
            producto.nombre = str(input("Ingrese nuevo nombre: "))
            Producto.convertir_a_string(producto)


def eliminar_producto():
    codigo: str = str(input("Ingrese código a eliminar: "))
    for indice, producto in enumerate(productos):
        if producto.codigo == codigo:
            productos.pop(indice)
            listap.pop(indice+1)


def nueva_factura():
    print("para generar una factura busca un cliente")
    cliente: Persona = buscar_persona()
    producto: Producto = buscar_producto()
    factura: Factura = Factura(len(factutas)+1, cliente)
    continuar: bool = True

    while continuar:

        cantidad: int = int(input("Ingrese la cantidad: "))
        now = datetime.now()
        dia=now.day
        mes=now.month
        año=now.year
        hora=now.hour
        minuto=now.minute
        factura.detalle.append(FacturaDetalle(
            producto.codigo, producto.nombre, producto.marca, cantidad, producto.precio))
        
        listafd.append([producto.codigo, producto.nombre, cantidad, producto.precio])
        facturaf: Facturafinal = Facturafinal(len(factutas), cliente)
        facturasf.append(facturaf)
        
        condicion: str = str(input("SI/si para agregar productos: "))

        if condicion == "SI" or condicion == "si":
            continuar = True
            producto: Producto = buscar_producto()
        else:
            continuar = False
            factura.calcular_igv()
            factutas.append(factura)
            listaf.append([factura.serie, factura.numero, cliente.dni, cliente.nombres, "{:.2f}".format(factura.base_imponible),
            "{:.2f}".format(factura.igv),"{:.2f}".format(factura.total)])
            print(listaf)
            fecha: Fechas=Fechas(len(factutas),dia,mes,año,hora,minuto)
            fechas.append(fecha)
            listafecha.append([len(factutas),dia,mes,año,hora,minuto])
            facturaf: Facturafinal = Facturafinal(len(factutas), cliente)
            facturasf.append(facturaf)
            generadorfactura(len(factutas),cliente)
            Generarpdf()
            print(format(factura.total))
            montoapagar=float(input("Monto a pagar: "))
            montonum: Montos=Montos(len(factutas),montoapagar)
            monto.append(montonum)
            
def listar_factura():
    for factura in factutas:
        print("| SERIE | NUMERO | DNI DEL CLIENTE | NOMBRE DEL CLIENTE | BASE IMPONIBLE | IGV | TOTAL |")
        Factura.convertir_a_string(factura)


def buscar_factura():
    numero: int = int(input("Ingrese el numero de la factura: "))
    for factura in factutas:
        if factura.numero == numero:
            Facturafinal.convertir_a_string(factura)
            print(
                "----------------------------------------------------------------------")
            for detalle in factura.detalle:
                FacturaDetalle.convertir_a_string(detalle)
            Facturafinal.convertir_a_string_final(factura)
            for montonum in monto:
                if montonum.numero == numero:
                    print(f"                                     Monto a pagar: {montonum.monto}")
                    print(f"                                     Vuelto: {montonum.monto-factura.total}")
    for fecha in fechas:
        if fecha.numero == numero:
            Fechas.convertir_a_string(fecha)


def ver_factura():
    for factura in factutas:
        Facturafinal.convertir_a_string(factura)
        for detalle in factura.detalle:
            FacturaDetalle.convertir_a_string(detalle)
        Facturafinal.convertir_a_string_final(factura)
        for fecha in fechas:
            if fecha.numero==factura.numero:
                Fechas.convertir_a_string(fecha)


def main():
    continuar: bool = True
    iniciarsesion()
    cargardatospersona()
    cargardatosproducto()
    cargardatosfactura()
    
    while continuar:
        print("*************************************************************")
        print("************************SISTEMA DE VENTAS********************")
        print("                                         ")
        print("=============================MENÚ============================")
        print("*************************INGRESE OPCIONES********************")
        print("       CLIENTE  ")
        print("       1: PARA AGREGAR PERSONA       2: PARA LISTAR PERSONAS")
        print("       3: PARA BUSCAR PERSONA        4: PARA EDITAR PERSONA")
        print("       5: PARA ELIMINAR PERSONA")
        print("       ")
        print("       PRODUCTO")
        print("       6: para ingresar producto     7: para listar productos")
        print("       8: para buscar producto       9: para editar producto")
        print("       10 para eliminar producto")
        print("       ")
        print("       FACTURA")
        print("       15: PARA CREAR FACTURA        16: PARA LISTAR  FACTURA")
        print("       17: PARA BUSCAR FACTURA       18: PARA LISTAR FACTURAS")
        print("                                         CON DETALLE")
        print("============================================================")
        print("       20: PARA SALIR                21: PARA GUARDAR EL PDF")
        print("                                         RESULTANTE")

        caso: str = str(input("INGRESE OPCIÓN: "))
        match caso:
            case "1":
                persona()
            case "2":
                listar_personas()
            case "3":
                buscar_persona()
            case "4":
                editar_persona()
            case "5":
                eliminar_persona()
            case "6":
                producto()
            case "7":
                listar_producto()
            case "8":
                buscar_producto()
            case "9":
                editar_producto()
            case "10":
                eliminar_producto()
            case "15":
                nueva_factura()
            case "16":
                listar_factura()
            case "17":
                buscar_factura()
            case "18":
                ver_factura()

            case "20":
                continuar = False
                x = input("¿Quieres guardar los datos? (SI/si para guardar) ")
                if x == "SI" or x == "si":
                    guardardatos()
                clientes.close()
                productot.close()
                facturastt.close()
                facturasdt.close()
                fechastt.close()
            case "21":
                print("Si el pdf asegura que es el correcto se procederá con el guardado")
                x=str(input("Si está seguro diga |si|: "))
                if x=="si":
                    contenido = os.listdir('PDFs/')
                    shutil.move("Factura resultante.pdf","PDFs/Factura resultante.pdf")
                    os.rename("PDFs/Factura resultante.pdf",f"PDFs/Factura resultante {len(contenido)}.pdf")
                    
                    
if __name__ == '__main__':
    main()
