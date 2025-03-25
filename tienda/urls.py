from django.urls import path
from . import views
from .views import adminC, editar_producto, eliminar_producto,eliminar_del_carrito,hacer_pedido
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('catalogo/', views.catalogo_view, name='catalogo'),
    path('catalogov2/', views.catalogo_v2, name='catalogov2'),
    path('adminC/', adminC, name='adminC'),
    path('editar_producto/<int:producto_id>/', editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:producto_id>/', eliminar_producto, name='eliminar_producto'),
    path('agregar_al_carrito/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('ver_carrito/', views.ver_carrito, name='ver_carrito'),
    path('obtener_cantidad_carrito/', views.obtener_cantidad_carrito, name='obtener_cantidad_carrito'),
    path('eliminar_del_carrito/<int:item_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
    path('hacer_pedido/', hacer_pedido, name='hacer_pedido'),
    path('aceptar_pedido/<int:pedido_id>/', views.aceptar_pedido, name='aceptar_pedido'),
    path('rechazar_pedido/<int:pedido_id>/', views.rechazar_pedido, name='rechazar_pedido'),
    path('confirmar_entrega/<int:pedido_id>/', views.confirmar_entrega, name='confirmar_entrega'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)