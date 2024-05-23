from odoo import api, fields, models, _


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _inherit = 'mail.thread'
    _description = "Doctor Records"


    name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string="Age")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender", tracking=True)
    capitalize_name = fields.Char(string='Capitalize Name', compute='_compute_capitalize_name', store=True)
    active = fields.Boolean(default=True)
    @api.depends('name')
    def _compute_capitalize_name(self):
        if self.name:
            self.capitalize_name = self.name.upper()
        else:
            self.capitalize_name = ' '

    # def name_get(self):
    #     result = []
    #     for rec in self:
    #         result.append((rec.id, f'{rec.ref} - {rec.name}'))
    #     return result

