from odoo import api, fields, models,_


class ApacheIIScore(models.Model):
    _name = "patient.apache"
    _rec_name = "registration_cod"


    registration_cod = fields.Many2one('patient.icu', string="Registration Code")
    icu_admission=fields.Datetime(string="Date")
    age=fields.Integer(string="Age")
    temp=fields.Float(string="Temperature")
    heart_rate=fields.Float(string="Heart Rate")
    fio2=fields.Float(string="Fio2")
    paco2=fields.Float(string="paCo2")
    ph=fields.Float(string="pH")
    potassium=fields.Float(string="Potassium")
    hematcocrit=fields.Float(string="Hematcocrit")
    arf=fields.Boolean(string="ARF")
    map=fields.Integer(string="MAP")
    respiratory_rate=fields.Integer(string="Respiratory Rate")
    pao2=fields.Integer(string="PaO2")
    A_ado2=fields.Integer(string="Heart Rate")
    sodium=fields.Float(string="Sodium")
    creatinine=fields.Float(string="Creatinine")
    wbc=fields.Float(string="WBC")
    chronic_condition=fields.Boolean(string="Chronic Condition")
    score=fields.Integer(string="Score")
    hospital_admit_type=fields.Char(string="Hospital Admission Type")


