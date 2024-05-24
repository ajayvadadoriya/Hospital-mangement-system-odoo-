from odoo import api, fields, models

class HospitalRoutes(models.Model):
    _name = "hospital.routes"

    name = fields.Char(string="Medicine Name", tracking=True)