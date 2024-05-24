from odoo import api, fields, models

class HospitalForm(models.Model):
    _name = "hospital.form"

    patient_name = fields.Many2one('hospital.patient', string="Patient")
    patient_id = fields.Char(related='patient_name.ref', string="Patient ID")
    patient_age = fields.Integer(related='patient_name.age', string="Age")
    date = fields.Date(string="Date")
    sex = fields.Selection(related='patient_name.gender', string="Sex")
    name = fields.Char(string="Medicament", tracking=True)
    indication = fields.Many2one('hospital.diseases', string="Indication")
    start_date = fields.Datetime(string="Start")
    end_date = fields.Datetime(string="End")
    act = fields.Selection([('true', 'True'), ('false', 'False')], string="Act")
    doctor = fields.Many2one('hospital.doctor', string="Doctor")
    patients_id=fields.Many2one('hospital.patient')