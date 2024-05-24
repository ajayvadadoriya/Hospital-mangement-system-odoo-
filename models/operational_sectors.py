from odoo import api, fields, models

class HospitalSectors(models.Model):
    _name = "hospital.sectors"

    name = fields.Char(string="Medicine Name", tracking=True)