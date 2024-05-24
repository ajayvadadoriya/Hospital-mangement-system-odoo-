from odoo import api, fields, models, _


class HospitalNewborn(models.Model):
    _name = "hospital.newborn"
    _description = "Hospital New Born Details"
    _rec_name = "ref"

    ref = fields.Char(string="Ref Code")
    image = fields.Image(string="Image")
    baby_name = fields.Char(string="Baby's Name")
    patient = fields.Char(related="baby_name", string="Patient")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Sex", tracking=True)
    discharge = fields.Datetime(string="Discharge")
    dob = fields.Datetime(string="Date of Birth")
    mother = fields.Char(string="Mother")
    weight = fields.Float(string="Weight")
    length = fields.Float(string="Length")
    blood = fields.Char(string="Blood Type")
    cephalic = fields.Integer(string="Cephalic Perimeter")
    hospital_bed = fields.Char(string="Hospital Bed")
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor in Charge")
    ward = fields.Selection([('general ward', 'General ward'), ('icu', 'ICU'), ('surgery', 'Surgery'),
                             ('outpatient services', 'Outpatient services')], string="Ward")
    state = fields.Selection([
        ('draft', "Draft"), ('confirmed', "Confirmed"), ('hospitalize', "Hospitalize"), ('canceled', 'Canceled'),
        ('discharge', 'Discharge')], string="Status",
        default='draft', tracking=True)

    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.newborn.sequence')
        return super(HospitalNewborn, self).create(vals)

    def action_confirm(self):
        self.state = 'confirmed'

    def action_patient_admission(self):
        self.state = 'hospitalize'

    def action_cancel(self):
        self.state = 'canceled'

    def action_discharge(self):
        self.state = 'discharge'
