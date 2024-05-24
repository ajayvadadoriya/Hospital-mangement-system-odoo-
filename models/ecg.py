from odoo import api, fields, models, _


class ECG(models.Model):
    _name = "patient.ecg"

    ecg_date = fields.Datetime(string="Date")
    registration_cod = fields.Many2one('patient.apache', string="Registration Code")
    lead = fields.Selection([('avr', 'aVR'), ('avf', 'aVF'), ('avl', 'aVL')], string="Lead")
    axis = fields.Selection([('normal axis', 'Normal Axis'), ('left axis deviation', 'Left Axis Deviation'),
                             ('right axis deviation', 'Right Axis Deviation'),
                             ('extreme axis deviation', 'Extreme Axis Deviation')], string="Axis")
    rate = fields.Float(string="Rate")
    pacemaker = fields.Char(string="Pacemaker")
    rhythm = fields.Char(string="Rhythm")
    pr = fields.Integer(string="PR")
    qrs = fields.Integer(string="QRS")
    qt = fields.Integer(string="QT")
    segment = fields.Selection([('elevation', 'Elevation'), ('depression', 'Depression')], string="ST segment")
    t_wave = fields.Boolean(string="T Wave Inversion")
    interpretation = fields.Char(string="Interpretation")
