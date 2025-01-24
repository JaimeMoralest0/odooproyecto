# -*- coding: utf-8 -*-
# from odoo import http


# class Odooproyecto(http.Controller):
#     @http.route('/odooproyecto/odooproyecto/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odooproyecto/odooproyecto/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odooproyecto.listing', {
#             'root': '/odooproyecto/odooproyecto',
#             'objects': http.request.env['odooproyecto.odooproyecto'].search([]),
#         })

#     @http.route('/odooproyecto/odooproyecto/objects/<model("odooproyecto.odooproyecto"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odooproyecto.object', {
#             'object': obj
#         })
