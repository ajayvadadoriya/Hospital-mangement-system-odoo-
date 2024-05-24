from odoo import api, fields, models

class HospitalAreas(models.Model):
    _name = "hospital.areas"

    name = fields.Char(string="Medicine Name", tracking=True)