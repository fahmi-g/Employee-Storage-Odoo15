from odoo import fields, models, api
import uuid


class Employee(models.Model):
    _name = 'employee_storage.employee'
    _description = 'Employee Model'
    _rec_name = 'employee_id'

    employee_id = fields.Char(
        string='Employee ID',
        required=False,
        readonly=True)

    employee_name = fields.Char(
        string='Employee Name',
        required=True)

    employee_position = fields.Selection(
        string='Employee Position',
        selection=[('sp', 'Software Programmer'),
                   ('m', 'Manager'), ],
        required=True, )

    storage_ids = fields.One2many(
        comodel_name='employee_storage.employee_storage',
        inverse_name='employee_id',
        string='Storages',
        required=False)



    # Functions

    @api.model
    def create(self, vals):
        rec = super(Employee, self).create(vals)

        rec.employee_id = uuid.uuid1()

        return rec