from odoo import api, fields, models

class HospitalInsurances(models.Model):
    _name = "hospital.insurances"

    name = fields.Char(string="Medicine Name", tracking=True)