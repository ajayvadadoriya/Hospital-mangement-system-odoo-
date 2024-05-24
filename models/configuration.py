from odoo import api, fields, models

class HospitalConfiguration(models.Model):
    _name = "hospital.configuration"
    _description ="Hospital configuration Details"

    name = fields.Char(string="Medicine Name", tracking=True)

