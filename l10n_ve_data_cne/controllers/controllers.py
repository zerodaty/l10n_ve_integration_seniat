# -*- coding: utf-8 -*-
# from odoo import http


# class L10nVeIntegrationCedula(http.Controller):
#     @http.route('/l10n_ve_integration_cedula/l10n_ve_integration_cedula', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/l10n_ve_integration_cedula/l10n_ve_integration_cedula/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('l10n_ve_integration_cedula.listing', {
#             'root': '/l10n_ve_integration_cedula/l10n_ve_integration_cedula',
#             'objects': http.request.env['l10n_ve_integration_cedula.l10n_ve_integration_cedula'].search([]),
#         })

#     @http.route('/l10n_ve_integration_cedula/l10n_ve_integration_cedula/objects/<model("l10n_ve_integration_cedula.l10n_ve_integration_cedula"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('l10n_ve_integration_cedula.object', {
#             'object': obj
#         })

