from odoo import api, fields, models, _


class HospitalConstruction(models.Model):
    _name = "hospital.project.note"
    _description = "Project Note"
    # _rec_name = "construction"

    product_name = fields.Char(string='Product Name')