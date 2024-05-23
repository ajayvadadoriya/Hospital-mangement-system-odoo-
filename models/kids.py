from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
class Hospitalkids(models.Model):
    _name = "hospital.kids"
    _inherit = 'mail.thread'
    _description = "Kids Records"
#---------------ATTRIBUTE OF PATIENT-----------------------------------------
    name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string="Age", tracking=True)
    notes = fields.Text(string="Notes")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender", tracking=True)
    capitalize_name = fields.Char(string='Capitalize Name', compute='_compute_capitalize_name', store=True)
    ref = fields.Char(string="Reference", default=lambda self: _('New'))
    state = fields.Selection([
        ('draft', "Draft"), ('confirm', "Confirm"), ('done', "Done"), ('canceled', "Canceled")], string="Status", default='draft', tracking=True)
    parent_detail = fields.Many2one('res.partner', string="Parent Detail")
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor")

# --------FOR CREATE SEQUENCE--------------------------------
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
            vls['ref'] = self.env['ir.sequence'].next_by_code('hospital.kids')
        return super(Hospitalkids, self).create(vls_list)

#--------FOR CAPITALIZATION--------------------------------
    @api.depends('name')
    def _compute_capitalize_name(self):
        if self.name:
            self.capitalize_name = self.name.upper()
        else:
            self.capitalize_name = ' '

#------------FOR VALIDATION----------------------------------
    @api.constrains('age')
    def _check_child_age(self):
        if self.age > 15:
            raise ValidationError(_("YOU ARE NOT KID!"))
