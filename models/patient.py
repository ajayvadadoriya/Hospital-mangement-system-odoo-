from datetime import date
from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description ="Hospital Patients Details"

    name = fields.Char(compute='patient_full_name', tracking=True)
    first_name = fields.Char(string="First Name", tracking=True)
    middle_name = fields.Char(string="Middle Name", tracking=True)
    last_name = fields.Char(string="Last Name", tracking=True)
    date_of_birth = fields.Date(string="Birth Date", tracking=True)
    age = fields.Integer(string="Patient Age", compute="age_count", tracking=True, store=True)
    gender = fields.Selection([('male','Male'),('female','Female')], string="Gender", tracking=True)
    phone = fields.Char(string="Contact Number", tracking=True)
    email = fields.Char(string="Email", tracking=True)
    address = fields.Char(string="Address", tracking=True)
    city = fields.Char(string="City", tracking=True)
    pin_code = fields.Char(string="Pin Code", tracking=True)
    ref = fields.Char(string="Ref Code", tracking=True)
    active = fields.Boolean(string="Active", default=True, tracking=True)
    appointment_count = fields.Integer(string="Visited Count", compute="appointment_count_fun")
    marital_status = fields.Selection([('married', 'Married'),('unmarried', 'Unmarried')], string="Marital Status")
    patient_image = fields.Image(string="Patient Image")
    partner_name = fields.Char(string="Partner Name")
    blood = fields.Selection([('a+', 'A+'),('o+', 'O+'),('b+', 'B+'),('ab+', 'AB+'),('a-', 'A-'),('o-', 'O-'),('b-', 'B-'),('ab-', 'AB-')], string="Blood Group")
    ethnic=fields.Char(string="Ethnic Group")
    insurance=fields.Char(string="Insurance")
    recive=fields.Integer(string="Receivable")
    family= fields.Char(string="Family")
    dece=fields.Boolean(string="Deceased")
    note=fields.Text(string="")
    dr=fields.Many2one('hospital.doctor',string="Primary Care Doctor")
    disease_ids=fields.One2many('hospital.diseases','patient_id',string="Diseases")
    medicament_ids=fields.One2many('hospital.form','patients_id',string="Medication")
    vaccination_ids=fields.One2many('hospital.vaccination','patients_id',string="Vaccination")
    labtest_ids=fields.One2many('hospital.labtest','patients_id',string="Labtest")


    _sql_constraints = [
        ('name_unique', 'unique (first_name,last_name,phone)', 'Name and Phone is already exists...!')
    ]

    @api.depends('first_name','last_name')
    def patient_full_name(self):
        for rec in self:
            rec.name = (rec.first_name or '')+' '+(rec.last_name or '')

    @api.model
    def create(self, vals):
        vals['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence')
        return super(HospitalPatient, self).create(vals)
    
    
    @api.depends('appointment_count')
    def appointment_count_fun(self):
        for rec in self:
            rec.appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', rec.id)])

    @api.depends('date_of_birth')
    def age_count(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0

    def name_get(self):
        return [(rec.id, "[%s] %s" %(rec.ref, rec.name)) for rec in self]
        # patient_list = []
        # for rec in self:
        #     name = rec.ref + ' ' + rec.name
        #     patient_list.append((rec.id, rec.first_name))
        # return patient_list

    def send_ref_by_email(self):
       template = self.env.ref('Ramsam_Multispeciality_Hospital.patient_reg_temp')
       for rec in self:
           template.send_mail(rec.id, force_send=True)