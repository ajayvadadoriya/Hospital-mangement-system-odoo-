from odoo import api, fields, models, _


class Ventilation(models.Model):
    _name = "mechanical.ventilation"
    _description = "Patient Ventilation Detail"

    situation = fields.Boolean(string="Current")
    from_date = fields.Datetime(string="From")
    duration = fields.Float(related='icu_id.duration',string="Duration")
    ventilation_type = fields.Selection(
        [('tracheostomy', 'Tracheostomy'), ('non-inasive psitive pressure', 'Non-inasive Psitive Pressure')],
        string="Type")
    remarks = fields.Char(string="Remarks")
    icu_id = fields.Many2one('patient.icu', string="")
