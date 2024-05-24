from odoo import api, fields, models

class HospitalDiseasecategories(models.Model):
    _name = "hospital.diseasecategories"

    name = fields.Char(string="Medicine Name", tracking=True)