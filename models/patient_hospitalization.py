from odoo import api, fields, models

class Hospitalization(models.Model):
    _name = "patient.hospitalization"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description ="Hospitalize Patients Details"
    _rec_name="ref"
    ref = fields.Char(string="Ref Code", readonly="True",tracking=True)
    patient_id=fields.Many2one('hospital.patient',string="Patient")
    bed=fields.Selection([('bed one','Bed One'),('bed two','Bed Two'),('bed three','Bed Three'),('bed four','Bed Four'),('bed five','Bed Five')],string="Hospital Bed")
    hospitalization_date=fields.Datetime(string="Hospitalization Date")
    discharge_date=fields.Datetime(string="Discharge Date")
    extra=fields.Text(string="Extra Info")
    doctor_id=fields.Many2one('hospital.doctor',string="Attending Physician")
    operating_id=fields.Many2one('hospital.doctor',string="Operating Physician")
    admission_type=fields.Selection([('urgent','Urgent'),('not urgent','Not Urgent')])
    reason_admission=fields.Many2one('hospital.form',string="Reason for Admission")
    ward=fields.Selection([('general ward','General ward'),('icu','ICU'),('surgery','Surgery'),('outpatient services','Outpatient services')],string="Ward")
    nursing=fields.Selection([('assessment','Assessment'),('diagnosis','Diagnosis'),('outcomes','Outcomes'),('interventions','Interventions'),('rationales','Rationales'),('evaluation','Evaluation')],string="Nursing Plan")
    discharge=fields.Selection([('assessment','Assessment'),('diagnosis','Diagnosis'),('outcomes','Outcomes'),('interventions','Interventions'),('rationales','Rationales'),('evaluation','Evaluation')],string="Discharge Plan")
    state = fields.Selection([
        ('free', "Free"), ('confirmed', "Confirmed"), ('hospitalize', "Hospitalize"),('canceled','Canceled'),('discharge','Discharge')], string="Status",
        default='free', tracking=True)
    bed_ids=fields.One2many('create.bed.transfer.wizard','hospital_id',string="Bed Transfer")



    def action_confirm(self):
        self.state = 'confirmed'

    def action_patient_admission(self):
        for rec in self:
            rec.env['patient.icu'].create({
                'registration_code': self.ref,
                'icu_admission': self.hospitalization_date,
                'discharge_date': self.discharge_date
            })
        self.state='hospitalize'

    def action_cancel(self):
        self.state = 'canceled'

    def action_discharge(self):
        self.state = 'discharge'
    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('patient.hospitalization.sequence')
        return super(Hospitalization, self).create(vals)


