from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
#---------------CLASS AND IT'S ATTRIBUTES------------------
class Hospitalpatient(models.Model):
    _name = "hospital.patient"
    _inherit = 'mail.thread'
    _description = "Patient Records"
#---------------ATTRIBUTE OF PATIENT-----------------------------------------
    image = fields.Image(string="Image")
    name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string="Age", tracking=True)
    is_child = fields.Boolean(string="Is child ?", tracking=True)
    notes = fields.Text(string="Notes")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender", tracking=True)
    capitalize_name = fields.Char(string='Capitalize Name', compute='_compute_capitalize_name', store=True)
    ref = fields.Char(string="Sequence Number",  required=True, copy=False, readonly=True,  default=lambda self: _('New'))
    state = fields.Selection([
        ('draft', "Draft"), ('confirm', "Confirm"), ('done', "Done"), ('canceled', "Canceled")], string="Status", default='draft', tracking=True)
    parent_detail = fields.Many2one('res.partner', string="Parent Detail")
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor")
    tag_ids = fields.Many2many('res.partner.category', 'hospital_patient_tag_rel', 'patient_id', 'tag_id', string="Tags")
    appointment_ids = fields.One2many('hospital.appointment', 'patient_id', string="Appointment")
    appointment_count=fields.Integer(string="Appointment Count", compute='compute_appointment_count')
# --------FOR CREATE MOVE TO STATUSBAR--------------------------------
    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'canceled'
# --------FOR CREATE SEQUENCE--------------------------------
    @api.model_create_multi
    def create(self, vls_list):
        for vls in vls_list:
            vls['ref'] = self.env['ir.sequence'].next_by_code('hospital.patient')
        return super(Hospitalpatient, self).create(vls_list)


    #--------FOR CAPITALIZATION--------------------------------
    @api.depends('name')
    def _compute_capitalize_name(self):
        if self.name:
            self.capitalize_name = self.name.upper()
        else:
            self.capitalize_name = ''

#------------FOR VALIDATION----------------------------------
    @api.constrains('is_child', 'age')
    def _check_child_age(self):
        for rec in self:
            if rec.is_child and rec.age == 0:
                raise ValidationError(_("Age has to be recorded!"))

#-----------FOR AUTO CLICK ON IS CHILD , IF AGE <=10------------------------------
    @api.onchange('age')
    def _onchange_age(self):
        if self.age <= 10:
            self.is_child = True
        else:
            self.is_child = False

    @api.depends('name')
    def _compute_capitalize_name(self):
        if self.name:
            self.capitalize_name = self.name.upper()
        else:
            self.capitalize_name = ''

    @api.depends('appointment_count')
    def compute_appointment_count(self):
        for rec in self:
            appointment_count = self.env['hospital.appointment'].search_count([('patient_id','=',rec.id)])
            rec.appointment_count = appointment_count

    def action_open_appointment(self):
        return {
            'name': 'Appointment',
            'type': 'ir.actions.act_window',
            'res_model': 'hospital.appointment',
            'view_mode': 'tree,form',
            'domain': [('patient_id', '=', self.id)],
            'target': 'current'
        }
