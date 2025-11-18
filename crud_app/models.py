from django.db import models
from django.contrib.auth import get_user_model
from datetime import timedelta
from django.utils import timezone

class Producto(models.Model):
    CATEGORIA_CHOICES = [
        ('streaming', 'Streaming'),
        ('deportes', 'Deportes'),
        ('musica', 'Música'),
        ('iptv', 'IPTV'),
        ('otros', 'Otros Servicios'),
    ]
    
    SERVICIO_CHOICES = [
        # Streaming
        ('netflix', 'Netflix'),
        ('disney', 'Disney+'),
        ('hbo_max', 'HBO Max'),
        ('jellyfin', 'Jellyfin'),
        ('prime_video', 'Prime Video'),
        ('youtube_premium', 'YouTube Premium'),
        ('vix', 'Vix Premium'),
        ('paramount', 'Paramount+'),
        ('plex', 'Plex'),
        ('canva', 'Canva Premium'),
        ('crunchyroll', 'Crunchyroll Premium'),
        ('spotify', 'Spotify Premium'),
        ('apple_tv', 'Apple TV+'),
        ('emby', 'Emby'),
        ('universal', 'Universal+'),
        ('shadowz', 'Shadowz'),
        ('telelatino', 'Telelatino'),
        ('gaia_tv', 'Gaia TV'),
        ('magis_tv', 'Magis TV'),
        # IPTV
        ('directv_go', 'DirecTV Go'),
        ('rakuten_viki', 'Rakuten Viki'),
        ('iptv_smarters', 'IPTV Smarters Pro'),
        ('win_sports', 'Win Sports Online'),
        ('flujo', 'Flujo'),
        ('profenet_win', 'ProfeNet + Win+'),
        ('directv_win', 'DirecTV Go + Win'),
        ('claro_win', 'Claro Video + Win'),
        ('magis_win', 'Magis TV + Win'),
        ('telelatino_win', 'Telelatino + Win'),
        # Deportes
        ('mlb_pass', 'MLB Pass'),
        ('nba_pass', 'NBA Pass'),
        ('wwe_network', 'WWE Network'),
        # Otros
        ('chatgpt_pro', 'ChatGPT Pro'),
    ]
    
    nombre = models.CharField(max_length=100, help_text="Nombre del servicio y tipo de pantalla")
    servicio = models.CharField(max_length=50, choices=SERVICIO_CHOICES, default='netflix', help_text="Tipo de servicio")
    categoria = models.CharField(max_length=50, choices=CATEGORIA_CHOICES, default='streaming')
    descripcion = models.TextField(blank=True, help_text="Descripción adicional del servicio")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    duracion_dias = models.PositiveIntegerField(default=30, help_text="Duración en días (27, 30, 33, 60, 90, 180, 365)")
    tipo_pantalla = models.CharField(max_length=100, blank=True, default='', help_text="Ej: Original, Premium, Estándar, Platino, etc.")
    stock = models.PositiveIntegerField(default=0, help_text="Cantidad de cuentas disponibles")
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    activo = models.BooleanField(default=True)
    creado_el = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['servicio', 'duracion_dias']
        verbose_name = 'Cuenta de Streaming'
        verbose_name_plural = 'Cuentas de Streaming'

    def __str__(self):
        return f"{self.get_servicio_display()} - {self.tipo_pantalla} ({self.duracion_dias} días)"
    
    def get_logo(self):
        """Retorna la ruta del logo según el servicio"""
        logos = {
            # Streaming
            'netflix': 'productos/netflix-3.svg',
            'disney': 'productos/disney-wbackground.svg',
            'prime_video': 'productos/amazon-prime-video-1.svg',
            'hbo_max': 'productos/hbo-max-svgrepo-com.svg',
            'jellyfin': 'productos/jellyfin-logo.png',
            'youtube_premium': 'productos/youtube-premiun-logo.png',
            'vix': 'productos/vix-video-streaming-icon.svg',
            'paramount': 'productos/paramount-3.svg',
            'plex': 'productos/plex-white.svg',
            'canva': 'productos/canva-wordmark-2.svg',
            'crunchyroll': 'productos/crunchyroll-logo.svg',
            'apple_tv': 'productos/apple-tv-plus-logo.svg',
            'universal': 'productos/universal-3.svg',
            'shadowz': 'productos/shadowz-logo.png',
            'telelatino': 'productos/tele-latino-logo.png',
            'gaia_tv': 'productos/gaia-tv-logo.png',
            'magis_tv': 'productos/magistv-logo.png',
            # IPTV
            'directv_go': 'productos/directv-go.svg',
            'rakuten_viki': 'productos/rakuten-viki-01.svg',
            'iptv_smarters': 'productos/IPTV-Smarters-logo.png',
            'win_sports': 'productos/win-sports-online-logo.png',
            # Deportes
            'mlb_pass': 'productos/mlb-1.svg',
            'nba_pass': 'productos/nba-league-pass.svg',
            'wwe_network': 'productos/wwe.svg',
            # Otros
            'chatgpt_pro': 'productos/chatgpt-3.svg',
        }
        return logos.get(self.servicio, None)
    
    def is_combo_win(self):
        """Verifica si es un combo con Win+"""
        return self.servicio in ['profenet_win', 'directv_win', 'claro_win', 'magis_win', 'telelatino_win']
    
    def get_combo_logo_main(self):
        """Retorna el logo principal del combo"""
        combo_logos = {
            'profenet_win': 'productos/profenet-logo.png',
            'directv_win': 'productos/directv-go.svg',
            'claro_win': 'productos/win-claro-video-logo.png',
            'magis_win': 'productos/magistv-logo.png',
            'telelatino_win': 'productos/tele-latino-logo.png',
        }
        return combo_logos.get(self.servicio, None)
    
    def get_combo_logo_win(self):
        """Retorna el logo de Win+ para combos"""
        if self.is_combo_win():
            return 'productos/win-logo.png'
        return None

class Order(models.Model):
    STATUS_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('procesando', 'Procesando'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    )
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    creado_el = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendiente')

    def __str__(self):
        return f"Orden #{self.id} - {self.usuario.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} (Orden #{self.order.id})"
