from odoo import api, fields, models

class HospitalRecreationaldrugs(models.Model):
    _name = "hospital.recreationaldrugs"

    name = fields.Char(string="Medicine Name", tracking=True)