from odoo import api, fields, models

class HospitalPathology(models.Model):
    _name = "hospital.pathology"

    name = fields.Char(string="Medicine Name", tracking=True)