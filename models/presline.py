from odoo import api, fields, models, _


class Prescription(models.Model):
    _name = "patient.prescription_lines"
    _description = "Prescription of Patient"

    print = fields.Boolean(string="Print")
    medi_id = fields.Many2one('hospital.form',string="Medicament")
    indi = fields.Char(string="Indication")
    dose = fields.Float(string="Dose")
    doseuni = fields.Many2one('uom.uom', string="Dose Unit")
    form = fields.Char(string="Form")
    freq = fields.Char(string="Frequency")
    qtn = fields.Float(string="Quantity")
    time = fields.Float(string="Time duration(min)")
    allows = fields.Selection([('allow substitution','Allow Substitution'),('not allow substitution','Not Allow substitution')],string="Allow substitution")
    comment = fields.Text(string="Comment")
    p_id = fields.Many2one('patient.prescription', string="Prescription")
