# -*- coding: utf-8 -*-
# from odoo import http


# class PagosWater(http.Controller):
#     @http.route('/pagos_water/pagos_water/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pagos_water/pagos_water/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pagos_water.listing', {
#             'root': '/pagos_water/pagos_water',
#             'objects': http.request.env['pagos_water.pagos_water'].search([]),
#         })

#     @http.route('/pagos_water/pagos_water/objects/<model("pagos_water.pagos_water"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pagos_water.object', {
#             'object': obj
#         })
