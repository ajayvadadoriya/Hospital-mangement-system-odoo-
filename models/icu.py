from odoo import api, fields, models, _


class Icu(models.Model):
    _name = "patient.icu"
    _description = "Patient ICU"
    _rec_name = "registration_code"

    registration_code = fields.Char(string="Registration Code")
    icu_admission = fields.Datetime(string="ICU Admission")
    discharge_date = fields.Datetime(string="Discharge Date")
    duration = fields.Float(string='Duration', compute='_compute_duration', store=True)
    deceased = fields.Boolean(string="Deceased")
    ventilation_ids = fields.One2many('mechanical.ventilation', 'icu_id', string="")
    state = fields.Selection([
        ('draft', "DRAFT"), ('admitted', "ADMITTED"), ('cancel', 'CANCEL'), ('discharge', 'DISCHARGE')],
        string="Status",
        default='draft')


    @api.depends('icu_admission', 'discharge_date')
    def _compute_duration(self):
        for record in self:
            if record.icu_admission and record.discharge_date:
                duration = (record.icu_admission - record.discharge_date).days
                record.duration = duration
            else:
                record.duration = 0.0

    def action_admitted(self):
        self.state = 'admitted'

    def action_discharge(self):
        self.state = 'discharge'

    def action_cancel(self):
        self.state = 'cancel'
