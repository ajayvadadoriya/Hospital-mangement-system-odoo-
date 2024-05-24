from odoo import api, fields, models

class HospitalHelathcenterunits(models.Model):
    _name = "hospital.helathcenterunits"
    _description ="Hospital helathcenterunits type Detail"

    name = fields.Char(string="Medicine Name", tracking=True)