from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Categoria, Etiqueta, DetalleProducto
from .forms import (
    ProductoForm,
    CategoriaForm,
    EtiquetaForm,
    DetalleProductoForm,  
)
from decimal import Decimal
from django.db.models import Count, Avg

def index(request):
    return render(request, "index.html")


def lista_productos(request):
    productos = (
        Producto.objects
        .select_related("categoria")
        .prefetch_related("etiquetas")
        .all()
    )
    context = {
        "productos": productos,
    }
    return render(request, "productos/lista.html", context)

def crear_producto(request):
    if request.method == "POST":
        form_producto = ProductoForm(request.POST)
        form_detalle = DetalleProductoForm(request.POST)

        if form_producto.is_valid() and form_detalle.is_valid():
            # Primero se guarda el producto
            producto = form_producto.save()

            # Luego se asocian los detalles a ese producto
            detalle = form_detalle.save(commit=False)
            detalle.producto = producto
            detalle.save()

            return redirect("lista_productos")
    else:
        form_producto = ProductoForm()
        form_detalle = DetalleProductoForm()

    context = {
        "form_producto": form_producto,
        "form_detalle": form_detalle,
    }
    return render(request, "productos/crear.html", context)


def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)

    try:
        detalle = producto.detalles   
    except DetalleProducto.DoesNotExist:
        detalle = None

    context = {
        "producto": producto,
        "detalle": detalle,
    }
    return render(request, "productos/detalle.html", context)

def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    detalle, _ = DetalleProducto.objects.get_or_create(producto=producto)

    if request.method == "POST":
        form_producto = ProductoForm(request.POST, instance=producto)
        form_detalle = DetalleProductoForm(request.POST, instance=detalle)

        if form_producto.is_valid() and form_detalle.is_valid():
            form_producto.save()
            form_detalle.save()
            return redirect("lista_productos")
    else:
        form_producto = ProductoForm(instance=producto)
        form_detalle = DetalleProductoForm(instance=detalle)

    context = {
        "form_producto": form_producto,
        "form_detalle": form_detalle,
        "producto": producto,
    }
    return render(request, "productos/editar.html", context)


def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == "POST":
        producto.delete()
        return redirect("lista_productos")

    context = {"producto": producto}
    return render(request, "productos/eliminar.html", context)

def lista_categorias(request):
    categorias = Categoria.objects.all()
    context = {"categorias": categorias}
    return render(request, "categorias/lista.html", context)

def crear_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_categorias")
    else:
        form = CategoriaForm()

    context = {"form": form, "categoria": None}
    return render(request, "categorias/formulario.html", context)

def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect("lista_categorias")
    else:
        form = CategoriaForm(instance=categoria)

    context = {"form": form, "categoria": categoria}
    return render(request, "categorias/formulario.html", context)

def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)

    if request.method == "POST":
        try:
            categoria.delete()
            return redirect("lista_categorias")
        except Exception:
            pass

    context = {"categoria": categoria}
    return render(request, "categorias/eliminar.html", context)

def lista_etiquetas(request):
    etiquetas = Etiqueta.objects.all()
    context = {"etiquetas": etiquetas}
    return render(request, "etiquetas/lista.html", context)

def crear_etiqueta(request):
    if request.method == "POST":
        form = EtiquetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_etiquetas")
    else:
        form = EtiquetaForm()

    context = {"form": form, "etiqueta": None}
    return render(request, "etiquetas/formulario.html", context)

def editar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, id=id)

    if request.method == "POST":
        form = EtiquetaForm(request.POST, instance=etiqueta)
        if form.is_valid():
            form.save()
            return redirect("lista_etiquetas")
    else:
        form = EtiquetaForm(instance=etiqueta)

    context = {"form": form, "etiqueta": etiqueta}
    return render(request, "etiquetas/formulario.html", context)

def eliminar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, id=id)

    if request.method == "POST":
        etiqueta.delete()
        return redirect("lista_etiquetas")

    context = {"etiqueta": etiqueta}
    return render(request, "etiquetas/eliminar.html", context)

def analitica_productos(request):
    """
    Vista de ejemplo para mostrar consultas avanzadas con el ORM:
        -  filter()
        - exclude()
        - annotate()
        - raw()
    """
    productos_caros = Producto.objects.filter(precio__gt=Decimal("10.00"))

    productos_no_dinamica = Producto.objects.exclude(
        categoria__nombre="Dinámica"
    )

    categorias_stats = Categoria.objects.annotate(
        num_productos=Count("productos"),
        precio_promedio=Avg("productos__precio"),
    )

    productos_raw = Producto.objects.raw(
        """
        SELECT id, nombre, precio, categoria_id
        FROM tienda_producto
        WHERE precio > %s
        """,
        [Decimal("10.00")],
    )

    context = {
        "productos_caros": productos_caros,
        "productos_no_dinamica": productos_no_dinamica,
        "categorias_stats": categorias_stats,
        "productos_raw": productos_raw,
    }
    return render(request, "productos/analitica.html", context)