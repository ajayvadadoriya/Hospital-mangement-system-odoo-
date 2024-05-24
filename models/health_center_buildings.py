from odoo import api, fields, models

class HospitalHelathcenterbuildings(models.Model):
    _name = "hospital.helathcenterbuildings"
    _description ="Hospital helathcenterbuildings type Detail"

    name = fields.Char(string="Medicine Name", tracking=True)