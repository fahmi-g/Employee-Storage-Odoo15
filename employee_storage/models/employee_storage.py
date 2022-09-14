from odoo import fields, models, api
import uuid


class EmployeeStorage(models.Model):
    _name = 'employee_storage.employee_storage'
    _description = 'Employee Storage Model'
    _rec_name = 'storage_id'

    storage_id = fields.Char(
        string='Storage_id',
        required=False,
        readonly=True)

    storage_type = fields.Selection(
        string='Storage Type',
        selection=[('basic', 'Basic'),
                   ('premium', 'Premium')],
        required=True)

    storage_size = fields.Float(
        string='Storage Size (GB)',
        required=False,
        compute='_compute_storage_size',
        readonly=True)

    storage_capacity = fields.Char(
        string='Storage Capacity',
        required=False,
        readonly=True,
        compute='_compute_storage_capacity')

    employee_id = fields.Many2one(
        comodel_name='employee_storage.employee_storage',
        string='Employee ID',
        required=False)

    data_ids = fields.One2many(
        comodel_name='employee_storage.employee_data',
        inverse_name='storage_id',
        string='Data IDs',
        required=False)


    # Functions

    @api.depends('storage_type')
    def _compute_storage_size(self):
        for rec in self:
            if (rec.storage_type == 'basic'):
                rec.storage_size = 100
            elif (rec.storage_type == 'premium'):
                rec.storage_size = 500
            else:
                rec.storage_size = 0


    @api.depends('data_ids')
    def _compute_storage_capacity(self):
        for rec in self:
            if(len(rec.data_ids) == 0):
                rec.storage_capacity = '100.0%'
            else:
                sizeSum = 0
                for data in rec.data_ids:
                    sizeSum += data.data_size

                currentCapacity = 100-((sizeSum/rec.storage_size)*100)
                rec.storage_capacity = str(currentCapacity)+'%'



    @api.model
    def create(self, vals):
        rec = super(EmployeeStorage, self).create(vals)

        rec.storage_id = uuid.uuid1()

        return rec


    # def write(self, vals):
    #
    #     rec = super(EmployeeStorage, self).write(vals)
    #
    #     return rec