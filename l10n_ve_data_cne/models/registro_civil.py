# -*- coding: utf-8 -*-
from odoo import models, fields

class RegistroCivil(models.Model):
    _name = 'l10n_ve.registro_civil'
    _description = 'Registro Civil de Ciudadanos (Basado en CNE)'
    _order = 'cedula'
    
    nacionalidad = fields.Selection([('V', 'Venezolano'), ('E', 'Extranjero')], string='Nacionalidad')
    cedula = fields.Char(string='Cédula de Identidad', required=True, index=True)
    rif = fields.Char(string='RIF', index=True)
    primer_nombre = fields.Char(string='Primer Nombre')
    segundo_nombre = fields.Char(string='Segundo Nombre')
    primer_apellido = fields.Char(string='Primer Apellido')
    segundo_apellido = fields.Char(string='Segundo Apellido')
    
    centro_cne_id = fields.Many2one('l10n_ve.centro_cne', string='Centro de Votación')