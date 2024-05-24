from odoo import api, fields, models

class HospitalMedical(models.Model):
    _name = "hospital.medical"

    name = fields.Char(string="Medicine Name", tracking=True)