# 🎬 StreamAccounts - Plataforma de Venta de Cuentas Premium

Plataforma e-commerce especializada en la venta de cuentas premium de servicios de streaming, música, deportes y más.

## 🚀 Características

### Servicios Disponibles

#### 🎬 Streaming
- Netflix (4 planes diferentes)
- Disney+ (Estándar y Premium)
- HBO Max / Max (3 planes)
- Prime Video
- Apple TV+ (incluye MLS)
- Paramount+
- Crunchyroll
- Plex
- Jellyfin
- Emby
- Universal+
- Shadowz (Terror)
- Telelatino
- Gaia TV
- Vix Premium
- Rakuten Viki

#### ⚽ Deportes
- DirecTV Go
- Win Sports Online
- MLB Pass
- NBA Pass
- WWE Network
- ProfeNet + Win+
- DirecTV Go + Win
- Claro Video + Win
- Magis TV + Win
- Telelatino + Win

#### 🎵 Música
- Spotify Premium (1, 2 y 3 meses)
- YouTube Premium (1 y 3 meses)

#### 📡 IPTV
- IPTV Smarters Pro (30, 90, 180 y 365 días)
- Magis TV
- Rakuten Viki

#### ✨ Otros Servicios
- ChatGPT Pro
- Canva Premium

## 💻 Tecnologías Utilizadas

- **Backend**: Django 5.2.7
- **Base de datos**: SQLite (desarrollo)
- **Frontend**: Bootstrap 5.3, CSS moderno con gradientes
- **Iconos**: Emojis nativos

## 📦 Instalación

### Requisitos Previos
- Python 3.8+
- pip

### Pasos de Instalación

1. **Clonar el repositorio**
```bash
cd "c:\Visual\Proyectos out\Mi_proyecto_UCC"
```

2. **Crear entorno virtual (recomendado)**
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
```

3. **Instalar dependencias**
```bash
pip install django pillow
```

4. **Ejecutar migraciones**
```bash
python manage.py migrate
```

5. **Poblar base de datos con productos**
```bash
python manage.py poblar_productos
```

6. **Crear superusuario (opcional)**
```bash
python manage.py createsuperuser
```

7. **Ejecutar servidor de desarrollo**
```bash
python manage.py runserver
```

8. **Abrir en navegador**
```
http://127.0.0.1:8000/
```

## 🎨 Características del Diseño

- **Gradientes modernos**: Purple-blue gradient background
- **Cards con glassmorphism**: Transparencias y blur effects
- **Animaciones sutiles**: Hover effects y transiciones suaves
- **Responsive**: Adaptado para móviles y tablets
- **Badges informativos**: Stock, duración y categorías visibles
- **Organización por categorías**: Fácil navegación

## 📊 Estructura del Proyecto

```
Mi_proyecto_UCC/
├── crud_app/
│   ├── management/
│   │   └── commands/
│   │       └── poblar_productos.py    # Script para poblar DB
│   ├── migrations/
│   ├── templates/
│   │   └── crud_app/
│   │       ├── base.html              # Template base
│   │       ├── index.html             # Página principal
│   │       ├── producto_detalle.html  # Detalle de cuenta
│   │       ├── carrito.html           # Carrito de compras
│   │       └── ...
│   ├── models.py                      # Modelo Producto, Order, OrderItem
│   ├── views.py                       # Vistas de la aplicación
│   ├── forms.py                       # Formularios
│   └── urls.py                        # URLs de la app
├── Mi_proyecto_UCC/
│   ├── settings.py                    # Configuración Django
│   └── urls.py                        # URLs principales
└── manage.py
```

## 🔧 Modelo de Datos

### Producto (Cuenta de Streaming)
- `nombre`: Nombre descriptivo
- `servicio`: Tipo de servicio (Netflix, Disney+, etc.)
- `categoria`: streaming, deportes, musica, iptv, otros
- `precio`: Precio en COP
- `duracion_dias`: Duración del acceso (27, 30, 60, 90, 180, 365)
- `tipo_pantalla`: Original, Premium, Estándar, etc.
- `stock`: Cantidad disponible
- `activo`: Estado del producto

### Order (Pedido)
- Usuario, total, estado, fecha

### OrderItem (Items del pedido)
- Order, producto, cantidad, precio unitario (snapshot)

## 🛒 Funcionalidades

✅ **Catálogo de productos** organizado por categorías
✅ **Detalle de producto** con información completa
✅ **Carrito de compras** basado en sesiones
✅ **Sistema de checkout** con validación de stock
✅ **Gestión de órdenes** para usuarios registrados
✅ **Autenticación** (login, registro, logout)
✅ **Panel de administración** Django
✅ **Gestión de stock** automática

## 📝 Uso del Panel Admin

1. Acceder a: `http://127.0.0.1:8000/admin/`
2. Iniciar sesión con superusuario
3. Gestionar productos, órdenes y usuarios

## 🎯 Próximas Mejoras

- [ ] Sistema de búsqueda funcional
- [ ] Filtros por categoría y precio
- [ ] Paginación de productos
- [ ] Pasarela de pagos (Mercado Pago, PayU)
- [ ] Notificaciones por email
- [ ] Panel de usuario mejorado
- [ ] Sistema de cupones/descuentos
- [ ] Historial de compras detallado
- [ ] Reviews y calificaciones

## 👤 Usuario de Prueba

Para testing, puedes crear un usuario con:
```bash
python manage.py createsuperuser
```

## 📄 Licencia

Proyecto educativo - UCC 2025

## 🤝 Contribuciones

Este es un proyecto académico. Para sugerencias o mejoras, contactar al desarrollador.

---

**Desarrollado con ❤️ para UCC - Herramientas Computacionales**

## 📥 Ejecución rápida (todo ya incluido)

Este repositorio incluye la base de datos (`db.sqlite3`), archivos en `media/` y un archivo `.env` configurado para desarrollo. Para ejecutar localmente, sigue solo estos pasos:

1. Crear y activar un entorno virtual:

```pwsh
python -m venv venv
.\venv\Scripts\Activate.ps1
```

2. Instalar dependencias desde `requirements.txt`:

```pwsh
pip install -r requirements.txt
```

3. Ejecutar el servidor de desarrollo:

```pwsh
python manage.py runserver
```

4. Abrir en el navegador:

```
http://127.0.0.1:8000/
```

Notas:
- No es necesario ejecutar migraciones ni poblar la base de datos: `db.sqlite3` ya contiene los datos de ejemplo.
- El archivo `.env` ya está incluido en el repo con valores para desarrollo. Si deseas generar tu propia clave secreta o cambiar `DEBUG`, modifica `.env`.
- Al incluir `db.sqlite3`, `media/` y `.env` en el repositorio, cualquier persona que clone obtendrá el mismo estado local que tienes actualmente.

## 🔐 Notas sobre seguridad y despliegue

- El proyecto actualmente incluye `SECRET_KEY` en `Mi_proyecto_UCC/settings.py`. Para producción **mueve** la clave a variables de entorno (`DJANGO_SECRET_KEY`) y elimina la clave del repositorio.
- En producción asegura `DEBUG=False` y configura `ALLOWED_HOSTS` apropiadamente.
- El archivo `.gitignore` del repositorio ya incluye `db.sqlite3`, `media/` y `.env` para evitar subir datos y credenciales por accidente.

## 🧪 Tests

Actualmente no hay tests automatizados en el proyecto. Se recomienda añadir tests unitarios para:

- Modelos (`Producto`, `Order`, `OrderItem`)
- Flujo de carrito y checkout

## 🛠️ Ficheros añadidos

- `requirements.txt` — lista mínima de dependencias.
- `.env.example` — plantilla para variables de entorno (no incluir `.env` en el repo).

Si quieres, puedo:

- Generar un `requirements.txt` más completo con versiones exactas (ejecutando `pip freeze` en un entorno virtual),
- Extraer `SECRET_KEY` a `settings` mediante `python-decouple`/`django-environ` y actualizar `settings.py` para leer `.env`,
- Añadir tests básicos y una CI (GitHub Actions) que valide la instalación.

¿Qué prefieres que haga a continuación?
