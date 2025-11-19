# StreamAccounts — Presentación

---

# 1. Portada

**StreamAccounts**

- Logo: `media/logo.png` (si aplica) — si no tienes logo, deja el espacio en blanco o inserta una captura del `static`.
- Integrantes: [NOMBRE1], [NOMBRE2], [NOMBRE3]  
- Curso: Herramientas Computacionales / UCC
- Fecha: 19/11/2025

**Notas del orador:**
- Saludo y presentación breve del equipo.
- Mencionar que la demo corre localmente y que el repo contiene `db.sqlite3`, `media/` y `.env` para reproducir el entorno.

---

# 2. Objetivo del Proyecto

**Objetivo:**
- Desarrollar una plataforma e-commerce sencilla para la venta de cuentas premium (streaming, música, deportes, IPTV y otros).

**Problema que resuelve:**
- Facilita la gestión y venta de cuentas con control de stock, carrito de compras y registro de órdenes.

**Público objetivo:**
- Pequeños comercios digitales, vendedores de cuentas/promociones y usuarios finales que buscan compras rápidas y soporte básico.

**Notas del orador:**
- Explicar un caso de uso: un cliente compra una cuenta y el administrador gestiona stock y órdenes desde el panel.

---

# 3. Tecnologías Utilizadas

- Lenguaje: **Python 3.8+**
- Framework: **Django 5.2.7**
- Frontend: **Bootstrap 5.3**, CSS personalizado (`crud_app/static/crud_app/css/styles.css`)
- Base de datos: **SQLite** (`db.sqlite3`, incluido para demo)
- Librerías: **Pillow**, **python-decouple**
- Tools: comando de administración personalizado (`poblar_productos`) para poblar datos

**Notas del orador:**
- Mencionar que en producción se recomienda usar PostgreSQL, configurar `DEBUG=False` y usar almacenamiento de media externo.

---

# 4. Funcionalidades Principales

- **Catálogo por categorías:** streaming, deportes, música, IPTV, otros.
- **Detalle de producto:** logo, duración, tipo de pantalla, precio y stock.
- **Carrito de compras en sesión:** agregar, aumentar/disminuir cantidad, eliminar.
- **Checkout:** valida stock, crea `Order` y `OrderItem`, descuenta stock.
- **Autenticación y roles:** registro, login, logout; vistas de administración (`staff_member_required`).
- **Panel de administración personalizado:** estadísticas, órdenes, productos más vendidos, bajo stock.
- **Comandos administrativos:** `python manage.py poblar_productos` para datos de ejemplo.

**Capturas sugeridas (placeholders):**
- `presentation/screenshots/index.png` (Página principal)
- `presentation/screenshots/producto_detalle.png` (Detalle de producto)
- `presentation/screenshots/carrito.png` (Carrito de compras)
- `presentation/screenshots/admin_dashboard.png` (Panel admin)

**Valor agregado:**
- Estructura simple y reproducible: `requirements.txt`, `.env.example` y `db.sqlite3` incluidos para demo.
- Helpers en modelos para manejo de logos y combos (ej. `Producto.get_logo()`, `is_combo_win`).

**Notas del orador:**
- Mostrar demo en vivo: navegar el index, agregar un producto al carrito y finalizar checkout.
- Indicar dónde se encuentran los archivos clave en el repo (`crud_app/models.py`, `crud_app/views.py`, `crud_app/templates/crud_app/`).

---

# Fin

- Preguntas y comentarios

**Notas del orador final:**
- Invitar a probar la app localmente con los comandos del `README.md`.
