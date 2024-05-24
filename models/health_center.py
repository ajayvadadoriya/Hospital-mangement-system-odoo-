from odoo import api, fields, models

class HospitalHelathcenter(models.Model):
    _name = "hospital.helathcenter"
    _description ="Hospital helathcenter type Detail"

    name = fields.Char(string="Medicine Name", tracking=True)