from odoo import api, fields, models

class HospitalVaccination(models.Model):
    _name = "hospital.vaccination"

    patient_name = fields.Many2one('hospital.patient', string="Patient")
    patient_id = fields.Char(related='patient_name.ref', string="Patient ID")
    patient_age = fields.Integer(related='patient_name.age', string="Age")
    date = fields.Date(string="Date")
    sex = fields.Selection(related='patient_name.gender', string="Sex")
    name = fields.Char(string="Vaccine", tracking=True)
    dose = fields.Selection([('none', 'None'),('1', '1'), ('2', '2'),('3', '3')], string="Dose")
    observation=fields.Char(string="Observation")
    patients_id=fields.Many2one('hospital.patient')