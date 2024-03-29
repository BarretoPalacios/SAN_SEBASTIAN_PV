from django.db import models

class Categoria(models.Model):
    codigo = models.AutoField(primary_key=True)
    codigo_categoria = models.CharField(max_length=20, unique=True)
    nombre_categoria = models.CharField(max_length=100)
    
    def __str__(self):
            return self.nombre_categoria

class Marca(models.Model):
    codigo = models.AutoField(primary_key=True)
    codigo_marca = models.CharField(max_length=20, unique=True)
    nombre_marca = models.CharField(max_length=100)
    
    def __str__(self):
            return self.nombre_marca

class Proveedor(models.Model):
    codigo = models.AutoField(primary_key=True)
    codigo_proveedor = models.CharField(max_length=20, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    ruc_dni = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    correo_electronico = models.EmailField()
    numero_telefono = models.CharField(max_length=20)
    
    def __str__(self):
            return self.nombres

class Producto(models.Model):
    codigo = models.AutoField(primary_key=True)
    codigo_producto = models.CharField(max_length=20, unique=True)
    codigo_barras = models.CharField(max_length=20)
    nombre = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
  
    def __str__(self):
            return self.nombre

class Factura(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre_factura = models.CharField(max_length=50)
    fecha_factura = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
            return self.nombre_factura
        
class MetodoPago(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
      
    def __str__(self):
            return self.nombre  
      
class Lista_Productos_Factura(models.Model):
    codigo = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_vendida = models.PositiveIntegerField()
    codigo_factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    
    def __str__(self):
            return f' se vendio {self.producto} {self.cantidad_vendida}'
    
class Venta_Productos_Factura(models.Model):
    codigo = models.AutoField(primary_key=True)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE,null=True)
    metodo = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    comentario = models.CharField(max_length=200, null=True, blank=True,default='Venta Añadida')
    total = models.PositiveIntegerField()
    
    def __str__(self):
            return f'total {self.total} de la venta  {self.codigo}'

      
class Inventario(models.Model):
    codigo = models.AutoField(primary_key=True)
    stock_inicial = models.PositiveIntegerField(default=0)  
    stock_actual = models.PositiveIntegerField(default=0) 
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    


    
        
    
    
    
    

    

        
        
        # --- tiket ---
        
        # 2 agusas = 2 
        # 4 galletas = 4.50 
        # 1/2 arroz = 3.00
        
        
        
        # impot= 9.50 
        # metodo de pago = yape
        
        
        
        # total 
        # vendieron 
        # quedaan
        
        
        
        
        
    
    