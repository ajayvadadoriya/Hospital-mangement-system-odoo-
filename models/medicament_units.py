from odoo import api, fields, models

class HospitalMedicamentunits(models.Model):
    _name = "hospital.medicamentunits"

    name = fields.Char(string="Medicine Name", tracking=True)