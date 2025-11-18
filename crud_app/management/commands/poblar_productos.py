from django.core.management.base import BaseCommand
from crud_app.models import Producto

class Command(BaseCommand):
    help = 'Pobla la base de datos con cuentas de streaming'

    def handle(self, *args, **kwargs):
        # Limpiar productos existentes
        Producto.objects.all().delete()
        
        productos = [
            # NETFLIX
            {'nombre': 'Netflix - Pantalla Original 27 Días', 'servicio': 'netflix', 'categoria': 'streaming', 
             'precio': 8500, 'duracion_dias': 27, 'tipo_pantalla': 'Pantalla Original', 'stock': 10},
            {'nombre': 'Netflix - Pantalla Original 33 Días', 'servicio': 'netflix', 'categoria': 'streaming', 
             'precio': 9500, 'duracion_dias': 33, 'tipo_pantalla': 'Pantalla Original', 'stock': 10},
            {'nombre': 'Netflix - Pantalla Extra Original 27 Días', 'servicio': 'netflix', 'categoria': 'streaming', 
             'precio': 13000, 'duracion_dias': 27, 'tipo_pantalla': 'Pantalla Extra Original', 'stock': 10},
            {'nombre': 'Netflix - Pantalla Internacional 27 Días', 'servicio': 'netflix', 'categoria': 'streaming', 
             'precio': 8500, 'duracion_dias': 27, 'tipo_pantalla': 'Pantalla Internacional', 'stock': 10},
            
            # PRIME VIDEO
            {'nombre': 'Prime Video - Pantalla Original 30 Días', 'servicio': 'prime_video', 'categoria': 'streaming', 
             'precio': 4000, 'duracion_dias': 30, 'tipo_pantalla': 'Pantalla Original', 'stock': 15},
            
            # DISNEY+
            {'nombre': 'Disney+ - Pantalla Estándar 30 Días', 'servicio': 'disney', 'categoria': 'streaming', 
             'precio': 4500, 'duracion_dias': 30, 'tipo_pantalla': 'Pantalla Estándar', 'stock': 12},
            {'nombre': 'Disney+ - Pantalla Premium 30 Días', 'servicio': 'disney', 'categoria': 'streaming', 
             'precio': 6000, 'duracion_dias': 30, 'tipo_pantalla': 'Pantalla Premium', 'stock': 12},
            
            # HBO MAX
            {'nombre': 'Max (HBO Max) - Pantalla Original 30 Días', 'servicio': 'hbo_max', 'categoria': 'streaming', 
             'precio': 3500, 'duracion_dias': 30, 'tipo_pantalla': 'Pantalla Original', 'stock': 15},
            {'nombre': 'Max (HBO Max) - Pantalla Platino 30 Días', 'servicio': 'hbo_max', 'categoria': 'streaming', 
             'precio': 4000, 'duracion_dias': 30, 'tipo_pantalla': 'Pantalla Platino', 'stock': 15},
            {'nombre': 'Max (HBO Max) - Pantalla Platino 60 Días', 'servicio': 'hbo_max', 'categoria': 'streaming', 
             'precio': 7000, 'duracion_dias': 60, 'tipo_pantalla': 'Pantalla Platino', 'stock': 15},
            {'nombre': 'Max (HBO Max) - Pantalla Platino 90 Días', 'servicio': 'hbo_max', 'categoria': 'streaming', 
             'precio': 10000, 'duracion_dias': 90, 'tipo_pantalla': 'Pantalla Platino', 'stock': 15},
            
            # PARAMOUNT+
            {'nombre': 'Paramount+ - Pantalla 30 Días', 'servicio': 'paramount', 'categoria': 'streaming', 
             'precio': 2500, 'duracion_dias': 30, 'tipo_pantalla': 'Pantalla', 'stock': 20},
            
            # CRUNCHYROLL
            {'nombre': 'Crunchyroll - Pantalla 30 Días', 'servicio': 'crunchyroll', 'categoria': 'streaming', 
             'precio': 2500, 'duracion_dias': 30, 'tipo_pantalla': 'Pantalla', 'stock': 15},
            
            # VIX
            {'nombre': 'Vix Premium - Pantalla 30 Días', 'servicio': 'vix', 'categoria': 'streaming', 
             'precio': 2500, 'duracion_dias': 30, 'tipo_pantalla': 'Pantalla', 'stock': 15},
            
            # PLEX
            {'nombre': 'Plex - Pantalla 30 Días', 'servicio': 'plex', 'categoria': 'streaming', 
             'precio': 2500, 'duracion_dias': 30, 'tipo_pantalla': 'Pantalla', 'stock': 15},
            
            # RAKUTEN VIKI
            {'nombre': 'Rakuten Viki - Pantalla 30 Días', 'servicio': 'rakuten_viki', 'categoria': 'iptv', 
             'precio': 2500, 'duracion_dias': 30, 'tipo_pantalla': 'Pantalla', 'stock': 15},
            
            # APPLE TV+
            {'nombre': 'Apple TV+ (Incluye MLS) - Pantalla 30 Días', 'servicio': 'apple_tv', 'categoria': 'streaming', 
             'precio': 6000, 'duracion_dias': 30, 'tipo_pantalla': 'Pantalla', 'stock': 10},
            {'nombre': 'Apple TV+ (Incluye MLS) - Pantalla 90 Días', 'servicio': 'apple_tv', 'categoria': 'streaming', 
             'precio': 12000, 'duracion_dias': 90, 'tipo_pantalla': 'Pantalla', 'stock': 10},
            
            # EMBY
            {'nombre': 'Emby - Pantalla 30 Días', 'servicio': 'emby', 'categoria': 'streaming', 
             'precio': 8000, 'duracion_dias': 30, 'tipo_pantalla': 'Pantalla', 'stock': 8},
            
            # IPTV SMARTERS PRO
            {'nombre': 'IPTV Smarters Pro - Perfil 30 Días', 'servicio': 'iptv_smarters', 'categoria': 'iptv', 
             'precio': 5000, 'duracion_dias': 30, 'tipo_pantalla': 'Perfil', 'stock': 15},
            {'nombre': 'IPTV Smarters Pro - Perfil 90 Días', 'servicio': 'iptv_smarters', 'categoria': 'iptv', 
             'precio': 10000, 'duracion_dias': 90, 'tipo_pantalla': 'Perfil', 'stock': 15},
            {'nombre': 'IPTV Smarters Pro - Perfil 180 Días', 'servicio': 'iptv_smarters', 'categoria': 'iptv', 
             'precio': 18000, 'duracion_dias': 180, 'tipo_pantalla': 'Perfil', 'stock': 15},
            {'nombre': 'IPTV Smarters Pro - Perfil 365 Días', 'servicio': 'iptv_smarters', 'categoria': 'iptv', 
             'precio': 35000, 'duracion_dias': 365, 'tipo_pantalla': 'Perfil', 'stock': 15},
            
            # MAGIS TV
            {'nombre': 'Magis TV - Pantalla 30 Días', 'servicio': 'magis_tv', 'categoria': 'iptv', 
             'precio': 7000, 'duracion_dias': 30, 'tipo_pantalla': 'Pantalla', 'stock': 10},
            
            # UNIVERSAL+
            {'nombre': 'Universal+ - Pantalla 30 Días', 'servicio': 'universal', 'categoria': 'streaming', 
             'precio': 6000, 'duracion_dias': 30, 'tipo_pantalla': 'Pantalla', 'stock': 10},
            
            # SHADOWZ
            {'nombre': 'Shadowz (Terror) - Pantalla 30 Días', 'servicio': 'shadowz', 'categoria': 'streaming', 
             'precio': 5000, 'duracion_dias': 30, 'tipo_pantalla': 'Pantalla', 'stock': 10},
            
            # JELLYFIN
            {'nombre': 'Jellyfin - Pantalla 30 Días', 'servicio': 'jellyfin', 'categoria': 'streaming', 
             'precio': 5000, 'duracion_dias': 30, 'tipo_pantalla': 'Pantalla', 'stock': 10},
            
            # TELELATINO
            {'nombre': 'Telelatino - Pantalla 30 Días', 'servicio': 'telelatino', 'categoria': 'streaming', 
             'precio': 6000, 'duracion_dias': 30, 'tipo_pantalla': 'Pantalla', 'stock': 10},
            
            # GAIA TV
            {'nombre': 'Gaia TV - 1 Mes', 'servicio': 'gaia_tv', 'categoria': 'streaming', 
             'precio': 9000, 'duracion_dias': 30, 'tipo_pantalla': 'Cuenta', 'stock': 5},
            
            # DEPORTES
            {'nombre': 'MLB Pass - 30 Días', 'servicio': 'mlb_pass', 'categoria': 'deportes', 
             'precio': 5000, 'duracion_dias': 30, 'tipo_pantalla': 'Pass', 'stock': 10},
            {'nombre': 'NBA Pass - 30 Días', 'servicio': 'nba_pass', 'categoria': 'deportes', 
             'precio': 5000, 'duracion_dias': 30, 'tipo_pantalla': 'Pass', 'stock': 10},
            {'nombre': 'WWE Network - 30 Días', 'servicio': 'wwe_network', 'categoria': 'deportes', 
             'precio': 5000, 'duracion_dias': 30, 'tipo_pantalla': 'Red', 'stock': 10},
            {'nombre': 'DirecTV Go - 30 Días', 'servicio': 'directv_go', 'categoria': 'deportes', 
             'precio': 15000, 'duracion_dias': 30, 'tipo_pantalla': 'Cuenta', 'stock': 8},
            
            # WIN SPORTS
            {'nombre': 'ProfeNet + Win+ - 30 Días', 'servicio': 'profenet_win', 'categoria': 'deportes', 
             'precio': 8000, 'duracion_dias': 30, 'tipo_pantalla': 'Combo', 'stock': 10},
            {'nombre': 'Win Sports Online - 30 Días', 'servicio': 'win_sports', 'categoria': 'deportes', 
             'precio': 20000, 'duracion_dias': 30, 'tipo_pantalla': 'Cuenta', 'stock': 8},
            {'nombre': 'DirecTV Go + Win - 30 Días', 'servicio': 'directv_win', 'categoria': 'deportes', 
             'precio': 26000, 'duracion_dias': 30, 'tipo_pantalla': 'Combo', 'stock': 8},
            {'nombre': 'Claro Video + Win - 30 Días', 'servicio': 'claro_win', 'categoria': 'deportes', 
             'precio': 18000, 'duracion_dias': 30, 'tipo_pantalla': 'Combo', 'stock': 8},
            {'nombre': 'Magis TV + Win - 30 Días', 'servicio': 'magis_win', 'categoria': 'deportes', 
             'precio': 7000, 'duracion_dias': 30, 'tipo_pantalla': 'Combo', 'stock': 8},
            {'nombre': 'Telelatino + Win - 30 Días', 'servicio': 'telelatino_win', 'categoria': 'deportes', 
             'precio': 6000, 'duracion_dias': 30, 'tipo_pantalla': 'Combo', 'stock': 8},
            
            # MÚSICA
            {'nombre': 'YouTube Premium - 1 Mes (Correo del Cliente)', 'servicio': 'youtube_premium', 'categoria': 'musica', 
             'precio': 7000, 'duracion_dias': 30, 'tipo_pantalla': 'Cuenta Personal', 'stock': 20},
            {'nombre': 'YouTube Premium - 3 Meses', 'servicio': 'youtube_premium', 'categoria': 'musica', 
             'precio': 16000, 'duracion_dias': 90, 'tipo_pantalla': 'Cuenta', 'stock': 15},
            {'nombre': 'Spotify Premium - 1 Mes', 'servicio': 'spotify', 'categoria': 'musica', 
             'precio': 8000, 'duracion_dias': 30, 'tipo_pantalla': 'Cuenta', 'stock': 20},
            {'nombre': 'Spotify Premium - 2 Meses', 'servicio': 'spotify', 'categoria': 'musica', 
             'precio': 14000, 'duracion_dias': 60, 'tipo_pantalla': 'Cuenta', 'stock': 15},
            {'nombre': 'Spotify Premium - 3 Meses', 'servicio': 'spotify', 'categoria': 'musica', 
             'precio': 18000, 'duracion_dias': 90, 'tipo_pantalla': 'Cuenta', 'stock': 15},
            
            # OTROS
            {'nombre': 'ChatGPT Pro - 30 Días', 'servicio': 'chatgpt_pro', 'categoria': 'otros', 
             'precio': 20000, 'duracion_dias': 30, 'tipo_pantalla': 'Cuenta', 'stock': 5, 
             'descripcion': 'Acceso completo a ChatGPT Pro con todas las funcionalidades premium'},
            {'nombre': 'Canva Premium - 30 Días', 'servicio': 'canva', 'categoria': 'otros', 
             'precio': 5000, 'duracion_dias': 30, 'tipo_pantalla': 'Cuenta', 'stock': 10},
        ]
        
        for producto_data in productos:
            Producto.objects.create(**producto_data)
        
        self.stdout.write(self.style.SUCCESS(f'✅ Se crearon {len(productos)} productos exitosamente'))
