from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import datetime
import qrcode

ruta = "C:/Users/Aula 25/Desktop/Examen/"

# Get user input
nombre = input("Nombre del usuario: ")
direccion = input("Dirección: ")
correo_electronico = input("Correo electrónico: ")

# Productos
productos = []
cantidades = []
precios_unitarios = []
precios_totales = []

num_productos = int(input("Número de productos: "))
for i in range(num_productos):
    producto = input(f"Nombre del producto {i + 1}: ")
    cantidad = int(input(f"Cantidad del producto {i + 1}: "))
    precio_unitario = float(input(f"Precio unitario del producto {i + 1}: "))
    precio_total = cantidad * precio_unitario

    productos.append(producto)
    cantidades.append(cantidad)
    precios_unitarios.append(precio_unitario)
    precios_totales.append(precio_total)

codigo_rastreo = input("Código de rastreo: ")

# QR
informacion = f"Nombre: {nombre}\nDirección: {direccion}\nCorreo: {correo_electronico}"
img = qrcode.make(informacion)
nombreImagen = ruta + "miQR.png"
img.save(nombreImagen)

# Current date and time
now = datetime.now()
fecha = now.strftime("%Y-%m-%d %H:%M:%S")

# Create PDF
c = canvas.Canvas(ruta + "TicketExamen.pdf", pagesize=A4)
c.setFont('Helvetica', 25)
c.drawString(200, 780, "Walmar")
logo= ruta+"logo.png"
c.drawImage(logo,300,780,50,50,mask="auto")


c.setFont('Helvetica-Bold', 16)
c.drawString(40, 750, "Comprador:")
c.drawString(180, 750, nombre)
c.drawString(40, 730, "Fecha:")
c.drawString(180, 730, fecha)
c.drawString(40, 710, "Dirección:")
c.drawString(180, 710, direccion)
c.drawString(40, 690, "Correo electrónico:")
c.drawString(190, 690, correo_electronico)

c.drawString(250, 660, "Productos")

x = 0
y = A4[1] - 190
c.line(x, y, x + 800, y)

c.drawString(50,630, "Producto")
c.drawString(180,630, "Cantidad")
c.drawString(310,630, "Precio")
c.drawString(490,630, "Total")

x = 0
y = A4[1] - 220
c.line(x, y, x + 800, y)

c.setFont('Helvetica', 16)
y -=40
for i in range(num_productos):
    c.drawString(50, y, productos[i])
    c.drawString(180, y, f"{cantidades[i]}")
    c.drawString(310,y, f"${precios_unitarios[i]:.2f}")
    c.drawString(490,y, f"${precios_totales[i]:.2f}")
    y-=25
c.drawString(200, 50, "Código de rastreo:")
c.drawString(350,50, codigo_rastreo)

c.drawImage(nombreImagen, 220, 100, 150, 150)

c.save()
