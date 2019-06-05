# -*- coding: utf-8 -*-
from odoo import http

# class InterkeyLock(http.Controller):
#     @http.route('/interkey_lock/interkey_lock/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/interkey_lock/interkey_lock/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('interkey_lock.listing', {
#             'root': '/interkey_lock/interkey_lock',
#             'objects': http.request.env['interkey_lock.interkey_lock'].search([]),
#         })

#     @http.route('/interkey_lock/interkey_lock/objects/<model("interkey_lock.interkey_lock"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('interkey_lock.object', {
#             'object': obj
#         })