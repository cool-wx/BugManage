# -*- coding: utf-8 -*-
# from odoo import http


# class Bug-manage(http.Controller):
#     @http.route('/bug-manage/bug-manage/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bug-manage/bug-manage/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bug-manage.listing', {
#             'root': '/bug-manage/bug-manage',
#             'objects': http.request.env['bug-manage.bug-manage'].search([]),
#         })

#     @http.route('/bug-manage/bug-manage/objects/<model("bug-manage.bug-manage"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bug-manage.object', {
#             'object': obj
#         })
