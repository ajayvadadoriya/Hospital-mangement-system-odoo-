from odoo import api, fields, models

class HospitalMedicamentcategories(models.Model):
    _name = "hospital.medicamentcategories"

    name = fields.Char(string="Medicine Name", tracking=True)