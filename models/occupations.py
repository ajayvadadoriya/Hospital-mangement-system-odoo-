from odoo import api, fields, models

class HospitalOccupations(models.Model):
    _name = "hospital.occupations"

    name = fields.Char(string="Medicine Name", tracking=True)