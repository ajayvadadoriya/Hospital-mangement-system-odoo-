from odoo import api, fields, models, _


class HospitalSurgery(models.Model):
    _name = "hospital.surgery"
    _rec_name="code_surgery"

    code_surgery = fields.Char(string="Code")
    patient_id = fields.Many2one('hospital.patient',string="Patient")
    description = fields.Char(string="Description")
    base_condition = fields.Char(string="Base Condition")
    classification = fields.Char(string="Surgery Classification")
    operating_room = fields.Char(string="Operating Room")
    dos = fields.Datetime(string="Date of the Surgery")
    eos=fields.Datetime(string="End of the Surgery")
    patient_age=fields.Integer(related="patient_id.age",string="Patient Age")
    doctor=fields.Many2one('hospital.doctor',string="Surgeon")
    extra_info=fields.Text(string="Extra Info")
