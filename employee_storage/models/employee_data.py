from odoo import fields, models, api
from odoo.exceptions import ValidationError
import uuid

class EmployeeData(models.Model):
    _name = 'employee_storage.employee_data'
    _description = 'Employee Data Model'
    _rec_name = 'data_id'

    data_id = fields.Char(
        string='Data Id',
        required=False,
        readonly=True)

    data_date = fields.Datetime(
        string='Data Date',
        required=False,
        readonly=True,
        default=fields.Datetime.now())

    storage_id = fields.Many2one(
        comodel_name='employee_storage.employee_storage',
        string='Storage ID',
        required=True)

    data_size = fields.Float(
        string='Data Size',
        required=False)



    # Functions

    @api.model
    def create(self, vals):
        rec = super(EmployeeData, self).create(vals)

        rec.data_id = uuid.uuid4()

        return rec


    @api.constrains('data_size')
    def check_data_size(self):
        for rec in self:
            recStorage = rec.storage_id
            totalDataSize = 0
            for data in recStorage.data_ids:
                totalDataSize += data.data_size

            totalDataSize-=rec.data_size

            currentCapacity = recStorage.storage_size - totalDataSize
            if(rec.data_size>currentCapacity):
                raise ValidationError('Data Melebihi Kapasitas.')