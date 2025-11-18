# 🔐 Credenciales de Acceso - StreamAccounts

## Usuario Administrador

Para acceder al panel de administración, utiliza las siguientes credenciales:

### Panel de Administración Personalizado
```
URL: http://127.0.0.1:8000/admin-panel/
Usuario: admin
Contraseña: (la que configuraste al crear el superusuario)
```

### Django Admin (Panel Original)
```
URL: http://127.0.0.1:8000/admin/
Usuario: admin
Contraseña: (la misma que arriba)
```

## Características del Panel Admin

### 🎯 Panel de Control (Dashboard)
- **Estadísticas en tiemp o real**
  - Total de productos y estado de stock
  - Total de órdenes por estado
  - Ingresos totales
  - Usuarios registrados

- **Productos más vendidos**
  - Top 5 productos con más ventas

- **Alertas de stock**
  - Productos con menos de 5 unidades

- **Órdenes recientes**
  - Últimas 10 órdenes realizadas

- **Acciones rápidas**
  - Acceso directo a gestión de órdenes
  - Gestión de productos
  - Crear nuevo producto
  - Link directo a Django Admin

### 📦 Gestión de Órdenes
- **Ver todas las órdenes**
  - Lista completa de pedidos

- **Filtros por estado**
  - Pendientes
  - Procesando
  - Completadas
  - Canceladas

- **Cambiar estado de órdenes**
  - Modal interactivo para actualizar estado
  - Actualización en tiempo real

- **Ver detalles de orden**
  - Productos incluidos
  - Cantidad y precios
  - Información del cliente

### 🛡️ Permisos Necesarios

Para acceder al panel de administración, el usuario debe tener:
- `is_staff = True` (Miembro del staff)
- O `is_superuser = True` (Superusuario)

## 🔧 Configurar Nuevos Administradores

### Desde Django Shell
```python
python manage.py shell

from django.contrib.auth.models import User

# Crear nuevo usuario admin
user = User.objects.create_user(
    username='nombre_admin',
    email='admin@email.com',
    password='contraseña_segura'
)
user.is_staff = True
user.is_superuser = True
user.save()
```

### Desde Django Admin
1. Acceder a http://127.0.0.1:8000/admin/
2. Ir a "Users" (Usuarios)
3. Hacer clic en "Add user" (Agregar usuario)
4. Completar el formulario
5. Marcar las casillas:
   - ✅ Staff status
   - ✅ Superuser status
6. Guardar

## 🎨 Interfaz del Panel Admin

El panel de administración tiene un diseño moderno con:
- **Gradientes purple-blue** para mantener la identidad visual
- **Cards con glassmorphism** para estadísticas
- **Tablas interactivas** con hover effects
- **Modales personalizados** para acciones
- **Badges de estado** con colores distintivos
- **Botones de acción** con animaciones

## 📱 Acceso desde el Navbar

Cuando un usuario con permisos de staff inicia sesión:
- Aparece el botón **"⚙️ Panel Admin"** en el navbar
- Color dorado para destacarlo
- Acceso directo al dashboard

## 🔄 Flujo de Trabajo Admin

1. **Iniciar sesión** con usuario admin
2. **Ver dashboard** con estadísticas generales
3. **Revisar órdenes pendientes**
4. **Cambiar estados** según el proceso
5. **Verificar stock** de productos
6. **Acceder a Django Admin** para configuraciones avanzadas

## ⚠️ Seguridad

- ✅ Decorador `@staff_member_required` en todas las vistas admin
- ✅ Redirección automática a login si no autorizado
- ✅ No exponer credenciales en el código
- ✅ Cambiar contraseña por defecto en producción
- ✅ Usar HTTPS en producción
- ✅ Configurar `ALLOWED_HOSTS` apropiadamente

## 🚀 URLs del Panel Admin

```
/admin-panel/                    # Dashboard principal
/admin-panel/orders/             # Gestión de órdenes
/admin-panel/order/<id>/update/  # Actualizar estado de orden
/admin/                          # Django Admin original
```

## 💡 Tips

- El panel muestra datos en tiempo real
- Los filtros de órdenes se aplican instantáneamente
- Los colores de badges ayudan a identificar estados rápidamente
- El botón de Django Admin abre en nueva pestaña
- Todas las acciones muestran mensajes de confirmación

---

**Última actualización**: Noviembre 2025
**Versión**: 1.0
