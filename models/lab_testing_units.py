from odoo import api, fields, models

class HospitalLabtesting(models.Model):
    _name = "hospital.labtesting"

    name = fields.Char(string="Medicine Name", tracking=True)