from datetime import date
from odoo import api, fields, models

class HospitalPharmacy(models.Model):
    _name = "hospital.pharmacy"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description ="Hospital Pharmacy Detail"

    name = fields.Char(string="Medicine Name", tracking=True)
    manufacturer = fields.Char(string="Manufactur Company Name", tracking=True)
    batch_no = fields.Char(string="Batch No", tracking=True)
    mfg_date = fields.Date(string="Manufacture Date", tracking=True)
    exp_date = fields.Date(string="Expiration Date", tracking=True)
    quantity = fields.Integer(string="Quantity", tracking=True)
    unit_price = fields.Float(string="Unit Price", tracking=True)
    
           