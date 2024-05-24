from odoo import api, fields, models


class HospitalPediatric(models.Model):
    _name = "hospital.pediatric"


    patient_id = fields.Many2one('hospital.patient', string="Patient")
    health_professional = fields.Many2one('res.users', string="Health Professional")
    pediatric_date=fields.Datetime(string="Date")
    complain=fields.Char(string="Complains of aches and pains")
    spends=fields.Char(string="Spends more time alone")
    times_easily=fields.Char(string="Times easily, has little energy")
    fidgety=fields.Char(string="Fidgety, unable sit still")
    teacher=fields.Char(string="Has trouble with teacher")
    apt_date=fields.Datetime(string="Date")
    appointment_id=fields.Many2one('hospital.appointment',string="Appointment")
    note=fields.Text(string="Note")