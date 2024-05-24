from odoo import api, fields, models

class DraftLabRequest(models.Model):
    _name = "draft.lab.test"
    _rec_name="test_type"

    test_type=fields.Char(string="Test Type")
    test_date=fields.Datetime(string="Date")
    invoice_to_insurance=fields.Boolean(string="Invoice to Insurance")
    patient_id=fields.Many2one('hospital.patient',string="Patient")
    doctor_id=fields.Many2one('hospital.doctor',string="Doctor")
    pathology=fields.Char(string="Pathology")
    insure=fields.Many2one('hospital.company',string="Insure")
    policy_number=fields.Char(string="Policy Number")

    state = fields.Selection([
        ('draft', "Draft"), ('tested', "Tested"),  ('canceled', 'Canceled'),
        ], string="Status",
        default='draft', tracking=True)

    def action_tested(self):
        self.state = 'tested'

    def action_cancel(self):
        self.state = 'canceled'

