# -*- coding: utf-8 -*-
from odoo import models, fields

class Estado(models.Model):
    _name = 'l10n_ve.estado'
    _description = 'Estado de Venezuela'
    _order = 'name'

    name = fields.Char(string='Estado', required=True)

class Municipio(models.Model):
    _name = 'l10n_ve.municipio'
    _description = 'Municipio de Venezuela'
    _order = 'name'

    name = fields.Char(string='Municipio', required=True)
    estado_id = fields.Many2one('l10n_ve.estado', string='Estado', required=True)

class Parroquia(models.Model):
    _name = 'l10n_ve.parroquia'
    _description = 'Parroquia de Venezuela'
    _order = 'name'

    name = fields.Char(string='Parroquia', required=True)
    municipio_id = fields.Many2one('l10n_ve.municipio', string='Municipio', required=True)

class CentroCNE(models.Model):
    _name = 'l10n_ve.centro_cne'
    _description = 'Centro Electoral CNE'
    _order = 'name'

    name = fields.Char(string='Nombre del Centro', required=True)
    direccion = fields.Text(string='Dirección')
    parroquia_id = fields.Many2one('l10n_ve.parroquia', string='Parroquia', required=True)