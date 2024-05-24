from odoo import api, fields, models

class HospitalImagingtype(models.Model):
    _name = "hospital.imagingtype"
    _description ="Hospital imaging type Detail"

    name = fields.Char(string="Medicine Name", tracking=True)