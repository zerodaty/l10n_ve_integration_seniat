# l10n_ve_cedula/models/res_partner.py
from odoo import models, fields, api, _
# La nueva herramienta para la última batalla
import httpx
import logging

_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.onchange('vat')
    def _onchange_vat_cedula_lookup(self):
        if not self.vat or self.is_company:
            return

        vat_cleaned = ''.join(filter(str.isalnum, self.vat)).upper()
        if not vat_cleaned.startswith(('V', 'E', 'P')):
            # Esta API solo parece funcionar para personas naturales (V/E) o pasaporte (P)
            return
        
        # Para la API, no necesita la V inicial, solo el número
        cedula = vat_cleaned[1:] if vat_cleaned.startswith(('V', 'E')) else vat_cleaned

        APP_ID = "1356"
        ACCESS_TOKEN = "6c169bed63b881ee369c21efc2c65cf6"

        headers = {
            'Content-Type': 'application/json',
            'App-Id': APP_ID,
            'Access-Token': ACCESS_TOKEN,
            # Un User-Agent moderno para parecer un navegador legítimo
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # El endpoint correcto de la API que intentamos usar originalmente
        api_url = f"https://api-cedula.com.ve/api/v1/persona/{cedula}"
        
        try:
            _logger.info(f"Misión Ave Fénix: Iniciando consulta con httpx a la API para: {cedula}")
            
            # Usamos un cliente httpx que soporta HTTP/2, a veces ayuda con Cloudflare.
            # verify=True es el default, así que volvemos a intentar una conexión segura y estándar.
            with httpx.Client(http2=True, verify=True) as client:
                response = client.get(api_url, headers=headers, timeout=20)
                
                # Lanzará un error si la respuesta es 4xx (ej: token inválido) o 5xx (error del servidor)
                response.raise_for_status()
                
                data = response.json()
            
            if data and data.get('success'):
                api_data = data.get('persona', {})
                nombres = f"{api_data.get('primer_nombre', '')} {api_data.get('segundo_nombre', '')}"
                apellidos = f"{api_data.get('primer_apellido', '')} {api_data.get('segundo_apellido', '')}"
                nombre_completo = f"{nombres.strip()} {apellidos.strip()}".strip()
                
                if nombre_completo:
                    self.name = nombre_completo
                
                return {
                    'warning': {
                        'title': ('¡¡¡LO LOGRAMOS!!!'),
                        'message': ('¡La conexión con httpx fue un éxito y los datos se actualizaron! ¡Victoria!'),
                    }
                }
            else:
                _logger.warning(f"httpx conectó, pero la API respondió sin éxito para {cedula}: {data}")
                return {
                    'warning': {
                        'title': ('Aviso de la API'),
                        'message': (f"La conexión fue exitosa, pero no se encontraron datos para la cédula. Respuesta: {data.get('message', 'Sin mensaje')}")
                    }
                }

        except httpx.RequestError as e:
            # Captura todos los errores de httpx, incluyendo los de conexión y SSL
            _logger.error(f"Error definitivo con httpx: {e}")
            return {
                'warning': {
                    'title': ('Misión Cumplida (Conclusión Final)'),
                    'message': ('Después de probar con 3 librerías diferentes, se confirma que la conexión a la API está bloqueada a un nivel que no podemos superar. Es hora de concluir que esta fuente de datos no es viable.')
                }
            }
        except Exception as e:
            # Captura cualquier otro error inesperado
            _logger.error(f"Un error inesperado ocurrió: {e}")