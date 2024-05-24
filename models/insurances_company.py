from odoo import api, fields, models

class HospitalCompany(models.Model):
    _name = "hospital.company"

    name = fields.Char(string="Medicine Name", tracking=True)