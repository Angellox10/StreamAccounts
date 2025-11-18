from .forms import CheckoutForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Order, OrderItem
from .forms import ProductoForm
from django.contrib import messages #para mensajes de alerta
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Sum, Count, Q
from datetime import datetime, timedelta

# ============================================
# PANEL DE ADMINISTRACIÓN
# ============================================

@staff_member_required(login_url='login')
def admin_dashboard(request):
    """Panel de control para administradores"""
    # Estadísticas generales
    total_productos = Producto.objects.count()
    productos_activos = Producto.objects.filter(activo=True).count()
    productos_sin_stock = Producto.objects.filter(stock=0).count()
    
    total_ordenes = Order.objects.count()
    ordenes_pendientes = Order.objects.filter(estado='pendiente').count()
    ordenes_completadas = Order.objects.filter(estado='completada').count()
    
    # Ingresos totales
    ingresos_totales = Order.objects.filter(estado='completada').aggregate(total=Sum('total'))['total'] or 0
    
    # Órdenes recientes (últimas 10)
    ordenes_recientes = Order.objects.all().order_by('-creado_el')[:10]
    
    # Productos más vendidos
    productos_vendidos = OrderItem.objects.values(
        'producto__id', 'producto__nombre', 'producto__servicio'
    ).annotate(
        total_vendido=Sum('cantidad')
    ).order_by('-total_vendido')[:5]
    
    # Obtener objetos de producto completos para acceder a get_logo()
    productos_vendidos_list = []
    for item in productos_vendidos:
        producto = Producto.objects.get(id=item['producto__id'])
        productos_vendidos_list.append({
            'producto': producto,
            'total_vendido': item['total_vendido']
        })
    
    # Productos con bajo stock (menos de 5)
    productos_bajo_stock = Producto.objects.filter(stock__lt=5, activo=True).order_by('stock')
    
    # Usuarios registrados
    total_usuarios = User.objects.count()
    usuarios_con_ordenes = User.objects.filter(order__isnull=False).distinct().count()
    
    # Estadísticas por categoría
    stats_categorias = Producto.objects.values('categoria').annotate(
        total=Count('id'),
        activos=Count('id', filter=Q(activo=True))
    )
    
    context = {
        'total_productos': total_productos,
        'productos_activos': productos_activos,
        'productos_sin_stock': productos_sin_stock,
        'total_ordenes': total_ordenes,
        'ordenes_pendientes': ordenes_pendientes,
        'ordenes_completadas': ordenes_completadas,
        'ingresos_totales': ingresos_totales,
        'ordenes_recientes': ordenes_recientes,
        'productos_vendidos': productos_vendidos_list,
        'productos_bajo_stock': productos_bajo_stock,
        'total_usuarios': total_usuarios,
        'usuarios_con_ordenes': usuarios_con_ordenes,
        'stats_categorias': stats_categorias,
    }
    
    return render(request, 'crud_app/admin_dashboard.html', context)

@staff_member_required(login_url='login')
def admin_orders(request):
    """Vista de todas las órdenes para administradores"""
    estado_filter = request.GET.get('estado', '')
    
    ordenes = Order.objects.all().order_by('-creado_el')
    
    if estado_filter:
        ordenes = ordenes.filter(estado=estado_filter)
    
    context = {
        'ordenes': ordenes,
        'estado_filter': estado_filter,
    }
    
    return render(request, 'crud_app/admin_orders.html', context)

@staff_member_required(login_url='login')
def admin_order_update(request, pk):
    """Actualizar estado de una orden"""
    orden = get_object_or_404(Order, pk=pk)
    
    if request.method == 'POST':
        nuevo_estado = request.POST.get('estado')
        if nuevo_estado in dict(Order.STATUS_CHOICES):
            orden.estado = nuevo_estado
            orden.save()
            messages.success(request, f'Estado de la orden #{orden.id} actualizado a {orden.get_estado_display()}')
            return redirect('admin_orders')
    
    return redirect('admin_orders')

@login_required(login_url='login')
def checkout(request):
    carrito = request.session.get('carrito', {})
    productos = []
    total = 0
    for pk, cantidad in carrito.items():
        producto = Producto.objects.filter(pk=pk).first()
        if producto:
            subtotal = producto.precio * cantidad
            productos.append({
                'producto': producto,
                'cantidad': cantidad,
                'subtotal': subtotal
            })
            total += subtotal

    if not productos:
        messages.error(request, 'El carrito está vacío.')
        return redirect('ver_carrito')

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Validar stock
            for item in productos:
                if item['cantidad'] > item['producto'].stock:
                    messages.error(request, f"No hay suficiente stock para {item['producto'].nombre}.")
                    return redirect('ver_carrito')
            # Crear orden
            order = Order.objects.create(
                usuario=request.user,
                total=total,
                estado='pendiente'
            )
            for item in productos:
                OrderItem.objects.create(
                    order=order,
                    producto=item['producto'],
                    cantidad=item['cantidad'],
                    precio_unitario=item['producto'].precio
                )
                # Descontar stock
                item['producto'].stock -= item['cantidad']
                item['producto'].save()
            # Limpiar carrito
            request.session['carrito'] = {}
            messages.success(request, '¡Compra realizada con éxito!')
            return redirect('orders')
    else:
        form = CheckoutForm()
    return render(request, 'crud_app/checkout.html', {'productos': productos, 'total': total, 'form': form})
# --- Historial de órdenes ---
@login_required(login_url='login')
def orders(request):
    ordenes = Order.objects.filter(usuario=request.user).order_by('-creado_el')
    return render(request, 'crud_app/orders.html', {'ordenes': ordenes})
# --- Carrito ---
from django.http import HttpResponseRedirect

def agregar_al_carrito(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    carrito = request.session.get('carrito', {})
    carrito[str(pk)] = carrito.get(str(pk), 0) + 1
    request.session['carrito'] = carrito
    messages.success(request, f"{producto.nombre} agregado al carrito.")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    productos = []
    total = 0
    for pk, cantidad in carrito.items():
        producto = Producto.objects.filter(pk=pk).first()
        if producto:
            subtotal = producto.precio * cantidad
            productos.append({
                'producto': producto,
                'cantidad': cantidad,
                'subtotal': subtotal
            })
            total += subtotal
    return render(request, 'crud_app/carrito.html', {'productos': productos, 'total': total})

def aumentar_cantidad(request, pk):
    carrito = request.session.get('carrito', {})
    if str(pk) in carrito:
        carrito[str(pk)] += 1
        request.session['carrito'] = carrito
        # No mostrar notif. emergente al aumentar cantidad (UX in-place)
    return redirect('ver_carrito')

def disminuir_cantidad(request, pk):
    carrito = request.session.get('carrito', {})
    if str(pk) in carrito:
        if carrito[str(pk)] > 1:
            carrito[str(pk)] -= 1
            request.session['carrito'] = carrito
            # No mostrar notif. emergente al disminuir cantidad (UX in-place)
        else:
            del carrito[str(pk)]
            request.session['carrito'] = carrito
            # No mostrar notif. emergente al eliminar (UX in-place)
    return redirect('ver_carrito')
#crud_app/views.py


# Visitar para listar todos los productos (SOLO ADMINISTRADORES)
@staff_member_required(login_url='login')
def listar_productos(request):
    # Mostrar solo productos con stock disponible
    productos = Producto.objects.filter(stock__gt=0).order_by('-creado_el')
    return render(request, 'crud_app/lista_productos.html', {'productos': productos})

# Visitar para crear un nuevo producto
@staff_member_required(login_url='login')
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado exitosamente.')
            return redirect('lista_productos')
        else:
            # Mostrar errores de validación al usuario, sin redirigir
            messages.error(request, 'Error al crear el producto. Por favor, revisar los datos.')
    else:
        form = ProductoForm()
    return render(request, 'crud_app/crear_producto.html', {'form': form})

# Visitar para actualizar un producto existente
@staff_member_required(login_url='login')
def actualizar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado exitosamente.')
            return redirect('lista_productos')
        else:
            # Mostrar errores de validación al usuario, sin redirigir
            messages.error(request, 'Error al actualizar el producto. Por favor, revisar los datos.')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'crud_app/actualizar_producto.html', {'form': form})

# Visitar para eliminar un producto
@staff_member_required(login_url='login')
def eliminar_producto(request, pk): 
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado exitosamente.')
        return redirect('lista_productos')
    return render(request, 'crud_app/eliminar_producto.html', {'producto': producto})   

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Bienvenido {username}')
            # Redirigir a la lista de productos después de iniciar sesión
            return redirect('lista_productos')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
            return redirect('login')
    return render(request, 'crud_app/login.html')

def logout_user(request):
    logout(request)
    messages.info(request, 'Sesión cerrada correctamente')
    return redirect('login')
def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, 'Las contraseñas no coinciden')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'El usuario ya existe')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'El correo ya está en uso')
            return redirect('register')

        User.objects.create_user(username=username, email=email, password=password1)
        messages.success(request, 'Cuenta creada con éxito. Ahora puedes iniciar sesión')
        return redirect('login')

    return render(request, 'crud_app/register.html')

# Vista de detalle de producto
@staff_member_required(login_url='login')
def producto_detalle(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'crud_app/producto_detalle.html', {'producto': producto})


def index(request):
    # Mostrar cuentas de streaming organizadas por categorías
    productos_streaming = Producto.objects.filter(categoria='streaming', activo=True).order_by('servicio', 'duracion_dias')[:20]
    
    # Deportes: excluir los combos Win+ que tienen su propia sección
    productos_deportes = Producto.objects.filter(
        categoria='deportes', 
        activo=True
    ).exclude(
        servicio__in=['profenet_win', 'directv_win', 'claro_win', 'magis_win', 'telelatino_win', 'win_sports']
    ).order_by('servicio')[:12]
    
    productos_musica = Producto.objects.filter(categoria='musica', activo=True).order_by('servicio', 'duracion_dias')[:8]
    
    # Separar productos IPTV regulares de combos Win+
    productos_iptv = Producto.objects.filter(
        categoria='iptv', 
        activo=True
    ).exclude(
        servicio__in=['profenet_win', 'directv_win', 'claro_win', 'magis_win', 'telelatino_win']
    ).order_by('servicio')[:12]
    
    # Productos combos Win+ (sección exclusiva)
    productos_combos_win = Producto.objects.filter(
        servicio__in=['profenet_win', 'directv_win', 'claro_win', 'magis_win', 'telelatino_win', 'win_sports'],
        activo=True
    ).order_by('servicio')[:10]
    
    productos_otros = Producto.objects.filter(categoria='otros', activo=True).order_by('servicio')[:8]
    
    return render(request, 'crud_app/index.html', {
        'productos_streaming': productos_streaming,
        'productos_deportes': productos_deportes,
        'productos_musica': productos_musica,
        'productos_iptv': productos_iptv,
        'productos_combos_win': productos_combos_win,
        'productos_otros': productos_otros,
    })