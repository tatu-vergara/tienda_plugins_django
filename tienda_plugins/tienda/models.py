from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="productos",
    )
    etiquetas = models.ManyToManyField(
        Etiqueta,
        blank=True,
        related_name="productos",
    )

    def __str__(self):
        return f"{self.nombre} (${self.precio})"


class DetalleProducto(models.Model):
    producto = models.OneToOneField(
        Producto,
        on_delete=models.CASCADE,
        related_name="detalles",
    )
    dimensiones = models.CharField(
        max_length=100,
        blank=True,
        help_text="Por ejemplo: 1200x800 px para la interfaz.",
    )
    peso_mb = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Tamaño aproximado de la descarga en MB.",
    )

    def __str__(self):
        return f"Detalles de {self.producto.nombre}"

class DetalleProducto(models.Model):
    producto = models.OneToOneField(
        Producto,
        on_delete=models.CASCADE,
        related_name="detalles",
    )
    dimensiones = models.CharField(
        max_length=100,
        blank=True,
        help_text="Resolución de la interfaz del plugin, ej: 1200x800 px.",
    )
    peso_mb = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Tamaño aproximado de la descarga en MB.",
    )