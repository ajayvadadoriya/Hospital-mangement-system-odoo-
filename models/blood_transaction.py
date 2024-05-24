from odoo import api, fields, models, _


class BloodTransaction(models.Model):
    _name = "blood.transaction"
    _rec_name="donors_id"


    # partner_id=fields.Many2one('res.partner',string="Partner")
    donors_id = fields.Many2one('blood.donors', string="Donors")
    blood_group = fields.Char(related='donors_id.blood_group', string="Blood Group")
    blood_type = fields.Selection([('in', 'In'), ('out', 'Out')], string="Type", default="in")
    transfer_date = fields.Datetime(string="Date")
    quantity = fields.Float(string="Quantity")