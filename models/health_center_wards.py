from odoo import api, fields, models

class HospitalHelathcenter(models.Model):
    _name = "hospital.helathcenterwards"
    _description ="Hospital helathcenterwards type Detail"

    name = fields.Char(string="Medicine Name", tracking=True)