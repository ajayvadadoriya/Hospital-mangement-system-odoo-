from odoo import api, fields, models, _


class HospitalConstruction(models.Model):
    _name = "hospital.construction"
    _description = "Construction Type"
    _rec_name = "construction"

    construction = fields.Char(string='Construction')


    def name_get(self):
        result = []
        for rec in self:
            result.append((rec.id, f'{rec.construction}'))
        return result