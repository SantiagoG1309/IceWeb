from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Producto, Profile  # Importa el modelo Profile
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductoForm
from django.http import JsonResponse
from .models import Producto, Carrito, ItemCarrito, Pedido, ItemPedido

def inicio(request):
    return render(request, 'inicio.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Verificar el rol del usuario
            try:
                profile = Profile.objects.get(user=user)
                if profile.role == 'admin':
                    return redirect("adminC")  # Redirige al panel de administrador
                else:
                    return redirect("catalogo")  # Redirige al catálogo para clientes
            except Profile.DoesNotExist:
                # Si no tiene perfil, redirige al catálogo por defecto
                return redirect("catalogo")
        else:
            messages.error(request, "Usuario o contraseña incorrectos")

    return render(request, "login.html")

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        role = request.POST["role"]  # Obtener el rol del formulario

        if User.objects.filter(username=username).exists():
            messages.error(request, "El usuario ya existe")
        else:
            # Crear el usuario
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            # Crear el perfil con el rol seleccionado
            Profile.objects.create(user=user, role=role)
            messages.success(request, "Registro exitoso, ahora puedes iniciar sesión")
            return redirect("login")  # Redirigir al login

    return render(request, "register.html")

def logout_view(request):
    logout(request)
    return redirect('/')

def catalogo_view(request):
    productos = Producto.objects.all()
    return render(request, 'catalogo.html', {'productos': productos})

def catalogo_v2(request):
    productos = Producto.objects.all()
    return render(request, 'catalogov2.html', {'productos': productos})

@login_required
@login_required
def adminC(request):
    # Verificar si el usuario es administrador
    profile = request.user.profile
    if profile.role != 'admin':
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('NO')

    # Obtener todos los productos
    productos = Producto.objects.all()

    # Obtener todos los pedidos
    pedidos = Pedido.objects.all()

    # Manejar la creación de un nuevo producto
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto creado exitosamente.")
            return redirect('adminC')  # Recargar la página después de guardar
    else:
        form = ProductoForm()
    return render(request, 'admin.html', {'form': form, 'productos': productos, 'pedidos': pedidos})
@login_required
def editar_producto(request, producto_id):
    profile = request.user.profile
    if profile.role != 'admin':
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('inicio')

    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, "Producto actualizado exitosamente.")
            return redirect('adminC')
    else:
        form = ProductoForm(instance=producto)

    return render(request, 'editar_producto.html', {'form': form})

@login_required
def eliminar_producto(request, producto_id):
    profile = request.user.profile
    if profile.role != 'admin':
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('inicio')

    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    messages.success(request, "Producto eliminado exitosamente.")
    return redirect('adminC')

@login_required
def agregar_al_carrito(request):
    if request.method == 'POST':
        product_id = request.POST.get('productId')
        quantity = int(request.POST.get('quantity'))
        producto = Producto.objects.get(id=product_id)
        carrito, created = Carrito.objects.get_or_create(usuario=request.user)
        item, item_created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
        
        if not item_created:
            item.cantidad += quantity
        else:
            item.cantidad = quantity
        item.save()

        # Redirigir al catálogo después de agregar el producto al carrito
        return redirect('catalogo')
    return JsonResponse({'success': False, 'error': 'Método no permitido'}, status=405)


@login_required
def ver_carrito(request):
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    items = carrito.itemcarrito_set.all()

    # Calcular el total a pagar sumando los totales de cada ítem
    total_a_pagar = sum(item.producto.precio * item.cantidad for item in items)

    return render(request, 'carrito.html', {'items': items, 'total_a_pagar': total_a_pagar})


@login_required
def obtener_cantidad_carrito(request):
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    count = carrito.itemcarrito_set.count()
    return JsonResponse({'count': count})

@login_required
def eliminar_del_carrito(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id, carrito__usuario=request.user)
    item.delete()
    return redirect('ver_carrito')

@login_required
def hacer_pedido(request):
    # Obtener o crear el carrito del usuario
    carrito, created = Carrito.objects.get_or_create(usuario=request.user)
    items_carrito = carrito.itemcarrito_set.all()

    if not items_carrito:
        messages.error(request, "Tu carrito está vacío. Agrega productos antes de hacer un pedido.")
        return redirect('ver_carrito')

    # Crear el pedido
    pedido = Pedido.objects.create(usuario=request.user)

    # Crear los ítems del pedido
    for item_carrito in items_carrito:
        ItemPedido.objects.create(
            pedido=pedido,
            producto=item_carrito.producto,
            cantidad=item_carrito.cantidad
        )
    items_carrito.delete()
    messages.success(request, "¡Pedido realizado con éxito! Gracias por tu compra.")
    return redirect('catalogo')

@login_required
def aceptar_pedido(request, pedido_id):
    if not request.user.profile.role == 'admin':
        messages.error(request, "No tienes permiso para realizar esta acción.")
        return redirect('inicio')

    pedido = get_object_or_404(Pedido, id=pedido_id)
    pedido.estado = 'aceptado'
    pedido.save()
    messages.success(request, f"Pedido {pedido_id} aceptado.")
    return redirect('adminC')

@login_required
def rechazar_pedido(request, pedido_id):
    if not request.user.profile.role == 'admin':
        messages.error(request, "No tienes permiso para realizar esta acción.")
        return redirect('inicio')

    pedido = get_object_or_404(Pedido, id=pedido_id)
    pedido.delete()  # Eliminar el pedido de la base de datos
    messages.success(request, f"Pedido {pedido_id} rechazado y eliminado.")
    return redirect('adminC')
@login_required
def confirmar_entrega(request, pedido_id):
    if not request.user.profile.role == 'admin':
        messages.error(request, "No tienes permiso para realizar esta acción.")
        return redirect('inicio')

    pedido = get_object_or_404(Pedido, id=pedido_id)
    pedido.estado = 'entregado'
    pedido.save()
    messages.success(request, f"Pedido {pedido_id} marcado como entregado.")
    return redirect('adminC')



