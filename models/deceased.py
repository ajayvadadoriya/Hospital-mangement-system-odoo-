from datetime import date
from odoo import api, fields, models


class HospitalDeceasedPatient(models.Model):
    _name = "hospital.deceased.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Patients Details"
    _rec_name = "rref"

    p_id=fields.Many2one('hospital.patient',string="Patient")
    dob = fields.Date(string="Birth Date", related="p_id.date_of_birth",tracking=True)
    rage = fields.Integer(string="Patient Age",related="p_id.age" , tracking=True, store=True)
    rgender = fields.Selection(related="p_id.gender", string="Gender", tracking=True)
    rphone = fields.Char(related="p_id.phone",string="Contact Number", tracking=True)
    remail = fields.Char(related="p_id.email",string="Email", tracking=True)
    raddress = fields.Char(related="p_id.address",string="Address", tracking=True)
    rcity = fields.Char(related="p_id.city",string="City", tracking=True)
    rpin_code = fields.Char(related="p_id.pin_code",string="Pin Code", tracking=True)
    rref = fields.Char(related="p_id.ref",string="Ref Code", tracking=True)
    ractive = fields.Boolean(related="p_id.active",string="Active", default=True, tracking=True)
    rappointment_count = fields.Integer(related="p_id.appointment_count",string="Visited Count")
    rmarital_status = fields.Selection(related="p_id.marital_status",string="Marital Status")
    rpatient_image = fields.Image(related="p_id.patient_image",string="Patient Image")
    rpartner_name = fields.Char(related="p_id.partner_name",string="Partner Name")
    rblood = fields.Selection(related="p_id.blood", string="Blood Group")
    rethnic = fields.Char(related="p_id.ethnic",string="Ethnic Group")
    rinsurance = fields.Char(related="p_id.insurance",string="Insurance")
    rrecive = fields.Integer(related="p_id.recive",string="Receivable")
    rfamily_id = fields.Char(related="p_id.family",string="Family")
    rdece = fields.Boolean(related="p_id.dece",string="Deceased")
    rnote = fields.Text(related="p_id.note",string="")
    rdr = fields.Many2one(related="p_id.dr", string="Primary Care Doctor")
    date_od_deth=fields.Date(string="Date of Death")
    cause=fields.Char(string="Cause of Death")



