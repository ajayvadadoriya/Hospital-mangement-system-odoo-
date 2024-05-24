from odoo import api, fields, models

class HospitalGeneticrisks(models.Model):
    _name = "hospital.geneticrisks"

    name = fields.Char(string="Medicine Name", tracking=True)