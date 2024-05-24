from odoo import api, fields, models

class HospitalOperating(models.Model):
    _name = "hospital.operating"
    _description ="Hospital operating Detail"

    name = fields.Char(string="Medicine Name", tracking=True)