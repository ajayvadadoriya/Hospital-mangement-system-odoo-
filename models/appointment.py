from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description ="Hospital Appointments Details"
    _rec_name = 'patient_id'

    patient_id = fields.Many2one('hospital.patient', string="Patient Name", ondelete="restrict")
    doctor_id=fields.Many2one('hospital.doctor',string="Physician")
    special_id=fields.Char(related="doctor_id.specialization",string="Specialization")
    appointment_date=fields.Datetime(string="Appointment Date")
    end_date=fields.Datetime(string="Appointment End")
    patient_status=fields.Selection([('outpatient','Outpatient'),('normal','Normal')],string="Patient Status")
    invoice_exempt=fields.Boolean(string="Invoice Exempt")
    status=fields.Selection([('to be invoiced','To Be Invoiced'),('invoiced','Invoiced')],string="Invoice exempt")
    validity =fields.Datetime(string="Validity")
    healthcenter =fields.Char(string="Health Center")
    duration=fields.Integer(string="Duration")
    urgency =fields.Selection([('urgent','Urgent'),('not urgent','Not Urgent')],string="Urgency level")
    invoice=fields.Boolean(string="Invoice To insurance")
    insurance=fields.Char(related="patient_id.insurance",string="Insurance")
    consultaion=fields.Selection([('doctor visit','Doctor Visit')],string="Consultaion Service")
    ref = fields.Char(string="Ref Code",readonly="True", tracking=True)
    file=fields.Binary(string="File")
    pf_file=fields.Binary(string="Pf file")
    bank_statement=fields.Binary(string="Bank Statement file")
    medical_bill=fields.Binary(string="Medical Bill file")
    policy_number=fields.Binary(string="Policy Number")
    note=fields.Text(string="Comments")






    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.appointment.sequence')
        return super(HospitalAppointment, self).create(vals)

    def whats_app_button(self):
        if not self.patient_id.phone:
            raise ValidationError(_("Patient Contact Number not Availble"))
        message = "Hi, %s Your Appointment Booked With Dr.%s On %s. Please Availble Before 15 Minute of Your Appointment Time" % (
        self.patient_id.name, self.doctor_id.name, self.appointment_date)
        whatsapp_api_url = 'https://api.whatsapp.com/send?phone=%s&text=%s' % (self.patient_id.phone, message)
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': whatsapp_api_url
        }