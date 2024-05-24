from odoo import api, fields, models, _


class BloodBuy(models.Model):
    _name = "blood.buy"
    _rec_name="patient_id"


    patient_id=fields.Many2one('res.partner',string="Patient")
    buy_date=fields.Datetime(string="Date")
    blood_group=fields.Char(string="Blood Group")
    qty=fields.Float(string="Quantity")
    blood_type = fields.Selection([('in', 'In'), ('out', 'Out')], string="Type", default="out")
