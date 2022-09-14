# -*- coding: utf-8 -*-
# from odoo import http


# class EmployeeStorage(http.Controller):
#     @http.route('/employee_storage/employee_storage', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/employee_storage/employee_storage/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('employee_storage.listing', {
#             'root': '/employee_storage/employee_storage',
#             'objects': http.request.env['employee_storage.employee_storage'].search([]),
#         })

#     @http.route('/employee_storage/employee_storage/objects/<model("employee_storage.employee_storage"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('employee_storage.object', {
#             'object': obj
#         })
