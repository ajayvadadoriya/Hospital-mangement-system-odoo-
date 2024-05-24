from odoo import api, fields, models,_

class Prescription(models.Model):
    _name = "patient.prescription"
    _description ="Prescription of Patient"
    _rec_name="ref"

    patient=fields.Many2one('hospital.patient',string="Patient")
    presdate=fields.Datetime(string="Prescription Date")
    phar_id=fields.Many2one('hospital.pharmacy',string="Pharmacy")
    ref = fields.Char(string="Prescription ID", required=True, copy=False, readonly=True,  default=lambda self: _('New'))
    login=fields.Many2one('res.users',string="Login User")
    pd=fields.Many2one('hospital.doctor',string="Prescribing Doctor")
    iti=fields.Boolean(string="Invoice to Insurance")
    note=fields.Text(string="")
    p_ids=fields.One2many('patient.prescription_lines','p_id',string="")
    img_ids=fields.One2many('hospital.imagingtest','img_id',string="Image")



    @api.model_create_multi
    def create(self, vls_list):
        for vls in vls_list:
            vls['ref'] = self.env['ir.sequence'].next_by_code('patient.prescription.sequence')
        return super(Prescription, self).create(vls_list)





