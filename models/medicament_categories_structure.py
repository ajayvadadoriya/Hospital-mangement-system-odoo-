from odoo import api, fields, models

class HospitalStructure(models.Model):
    _name = "hospital.structure"

    name = fields.Char(string="Medicine Name", tracking=True)