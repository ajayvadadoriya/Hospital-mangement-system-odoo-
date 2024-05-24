from odoo import api, fields, models

class HospitalHelathcenterbeds(models.Model):
    _name = "hospital.helathcenterbeds"
    _description ="Hospital helathcenterbeds type Detail"

    name = fields.Char(string="Medicine Name", tracking=True)