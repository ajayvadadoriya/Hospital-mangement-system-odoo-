from odoo import api, fields, models

class HospitalMedicaments(models.Model):
    _name = "hospital.medicaments"



    name = fields.Char(string="Medicament", tracking=True)