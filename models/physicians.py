from odoo import api, fields, models

class HospitalPhysicians(models.Model):
    _name = "hospital.physicians"
    _description ="Hospital physicians Detail"

    name = fields.Char(string="Medicine Name", tracking=True)