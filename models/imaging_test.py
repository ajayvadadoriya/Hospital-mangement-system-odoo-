from odoo import api, fields, models, _


class HospitalImagingtest(models.Model):
    _name = "hospital.imagingtest"
    _description = "Hospital imagingtest type Detail"
    _rec_name = "ref"
    name = fields.Char(string="Test", tracking=True)
    ref = fields.Char(string="Request", copy=False, readonly=True, default=lambda self: _('New'))
    date = fields.Datetime(string="Test Date")
    patient = fields.Many2one('hospital.patient', string="Patient")
    physician = fields.Many2one('hospital.doctor', string="Physician")
    urgent = fields.Boolean(string="Urgent")
    state = fields.Selection([
        ('draft', "Draft"), ('confirm', "Confirm"), ('done', "Done"), ('canceled', "Canceled")], string="Status",
        default='draft', tracking=True)
    comment = fields.Text(string="Comments")
    img_id = fields.Many2one('patient.prescription', string="")

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'canceled'

    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.imagingtest.sequence')
        return super(HospitalImagingtest, self).create(vals)
