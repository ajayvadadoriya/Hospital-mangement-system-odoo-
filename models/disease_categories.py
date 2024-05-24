from odoo import api, fields, models

class HospitalDiseasecate(models.Model):
    _name = "hospital.diseasecate"

    name = fields.Char(string="Medicine Name", tracking=True)