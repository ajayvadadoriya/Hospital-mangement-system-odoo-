from odoo import api, fields, models

class HospitalDiseases(models.Model):
    _name = "hospital.diseases"


    patient_name=fields.Many2one('hospital.patient',string="Patient")
    patient_ref=fields.Char(related="patient_name.ref",string="Patient ID")
    patient_age=fields.Integer(related="patient_name.age",string="Patient Age")
    date=fields.Date(string="Date")
    sex=fields.Selection(related="patient_name.gender",string="Gender")
    name = fields.Char(string="Name", tracking=True)
    status = fields.Selection([('statusquo', 'Status Quo'),('chronic', 'Chronic')], string="Status")
    active = fields.Selection([('yes', 'Yes'),('no', 'No')], string="Active")
    infection = fields.Selection([('yes', 'Yes'),('no', 'No')], string="Infection")
    remark = fields.Char(string="Remarks")
    physician=fields.Many2one('hospital.doctor',string="Physician")
    patient_id=fields.Many2one('hospital.patient',string="")
    severity =fields.Char(string="Severity")
    diagnosed=fields.Date(string="Diagnosed")