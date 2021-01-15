# -*- coding: utf-8 -*-
from odoo import http


class Bug(http.Controller):
    @http.route('/bug/', auth='public')
    def bug_manage(self, **kw):
        bugs = http.request.env['bug.bug']
        domain_bug = [('is_closed', '=', False)]
        bugs_open = bugs.search(domain_bug)
        return http.request.render('bug-manage.bugs_template', {'bugs_open': bugs_open})

    @http.route('/bug-manage/bug-manage/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('bug-manage.listing', {
            'root': '/bug-manage/bug-manage',
            'objects': http.request.env['bug-manage.bug-manage'].search([]),
        })

#     @http.route('/bug-manage/bug-manage/objects/<model("bug-manage.bug-manage"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bug-manage.object', {
#             'object': obj
#         })
