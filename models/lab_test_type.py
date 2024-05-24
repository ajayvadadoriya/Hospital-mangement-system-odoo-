from odoo import api, fields, models

class HospitalLabtest(models.Model):
    _name = "hospital.labtest"
    _description ="Hospital lab test type Detail"

    patient_name = fields.Many2one('hospital.patient', string="Patient")
    patient_id = fields.Char(related='patient_name.ref', string="Patient ID")
    patient_age = fields.Integer(related='patient_name.age', string="Age")
    date = fields.Datetime(string="Date")
    sex = fields.Selection(related='patient_name.gender', string="Sex")
    name = fields.Char(string="Test Type", tracking=True)
    doctor = fields.Many2one('hospital.doctor',string="Doctor")
    state=fields.Selection([('tested','Tested'),('complete','Complete')],string="State")
    patients_id = fields.Many2one('hospital.patient')