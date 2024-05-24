from datetime import date
from odoo import api, fields, models

class HospitalAppointmentPharmacy(models.Model):
    _name = "hospital.appointment.pharmacy"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description ="Hospital Appointment Pharmacy Detail"

    medicine_id = fields.Many2one("hospital.pharmacy")
    morning_qty = fields.Integer(string="Mornong", default=1)
    afternoon_qty = fields.Integer(string="Afternoon", default=1)
    night_qty = fields.Integer(string="Night", default=1)
    prec_time = fields.Char(string="Prescribe Time")
    prec_days = fields.Integer(string="Prescribe Days")
    appointment_pharmacy_id = fields.Many2one("hospital.appointment", string="Appointment Pharmacy")

    
    
           