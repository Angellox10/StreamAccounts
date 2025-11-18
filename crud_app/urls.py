#crud_app /forms.py
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('registrarse/', views.register_user, name='register'),
    path('productos', views.listar_productos, name='lista_productos'),
    path('crear/', views.crear_producto, name='crear_producto'),
    path('actualizar/<int:pk>/', views.actualizar_producto, name='actualizar_producto'),
    path('eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    path('producto/<int:pk>/', views.producto_detalle, name='producto_detalle'),
    path('carrito/agregar/<int:pk>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/aumentar/<int:pk>/', views.aumentar_cantidad, name='aumentar_cantidad'),
    path('carrito/disminuir/<int:pk>/', views.disminuir_cantidad, name='disminuir_cantidad'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.orders, name='orders'),
    
    # URLs de administración
    path('admin-panel/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-panel/orders/', views.admin_orders, name='admin_orders'),
    path('admin-panel/order/<int:pk>/update/', views.admin_order_update, name='admin_order_update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


