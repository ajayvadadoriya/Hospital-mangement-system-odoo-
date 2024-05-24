
from odoo import api, fields, models

class HospitalEmployee(models.Model):
    _name = "hospital.employee"
    _description ="Hospital Employee Details"
    _rec_name="emp_name"

    emp_name=fields.Char(string="Name")
    ordering_dr=fields.Many2one('hospital.doctor',string="Ordering Doctor")
    health_professional=fields.Many2one('hospital.doctor',string="Health Professional")
    patient_id=fields.Many2one('hospital.patient',string="Patient")
    condition=fields.Char(string="Base Condition")
    related_evaluations=fields.Char(string="Related Evaluation")
    session=fields.Integer(string="Session#")
    start_date=fields.Datetime(string="Start")
    stable=fields.Text(string="Stable")
    warning_emp=fields.Boolean(string="Warning")
    end_date=fields.Datetime(string="End")
    next_session=fields.Datetime(string="Next Session")
    nursing_ids=fields.One2many('hospital.nursing.lines','emp_id',string="PROCEDURES")





class HospitalNursing(models.Model):
    _name = "hospital.nursing.lines"

    n_code=fields.Char(string="Code")
    comments=fields.Text(string="Comments")

    emp_id=fields.Many2one('hospital.employee',string="")